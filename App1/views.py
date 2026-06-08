from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .tokenn import generateToken
from django.core.mail import EmailMessage
from PFE import settings
from keras.preprocessing import image
import os
from django.http import JsonResponse
import numpy as np
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Diabetes,PredictCardio,Pneumonia
from django.contrib.auth.decorators import login_required
from tensorflow import keras
from keras.models import load_model
from .chatbot import *

# ,compile=False
heart_model = load_model("App1/models/heart_prediction.h5")
diabetes_model = load_model("App1/models/diabetes_prediction.h5")
pneumonia_model = load_model("App1/models/Pneumonia_prediction.h5")
model = load_model('App1\models\chatbot_model.h5')

def home(request):
    if request.user.is_authenticated:
        # Obtenir l'ID de l'utilisateur authentifié
        user_id = request.user.id
    else:
        user_id = 'not found'
    return render(request,'App/dashbord.html',{'user_id': user_id})

@login_required
def chatbot(request):
    if request.method == "POST":
        msg = request.POST['msg']
        ints = predict_class (msg)
        res = get_response (ints, intents)
        return JsonResponse({'response': res})
    return render(request,'App/chatbot.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf_password']
        
        if User.objects.filter(username=username):
            messages.error(request, 'username already taken please try another.')
            return redirect('register')
        if User.objects.filter(email=email):
            messages.error(request, 'Cet e-mail est associé à un compte.')
            return redirect('register')
        if len(username)>30:
            messages.error(request, 'Le nom d\'utilisateur ne doit pas dépasser 30 caractères.')
            return redirect('register')
        if len(username)<5:
            messages.error(request, "Le nom d'utilisateur doit comporter au moins 5 caractères.")
            return redirect('register')
        if password != conf_password:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
            return redirect('register')

        my_user = User.objects.create_user(username, email, password)
        my_user.is_active = False
        my_user.save()
        messages.success(request, 'Votre compte a été créé avec succès')
        # send the the confirmation email
        current_site = get_current_site(request) 
        email_suject = "Confirmation de votre adresse e-mail"
        messageConfirm = render_to_string("autentification/confirmation_email.html", {
            'name': my_user.username,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(my_user.pk)),
            'token': generateToken.make_token(my_user)
        })
        
        email = EmailMessage(
            email_suject,
            messageConfirm,
            settings.EMAIL_HOST_USER,
            [my_user.email]
        )

        email.fail_silently = False
        email.send()
        return redirect('login')
    
    return render(request, 'autentification/register.html')


def login_function(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            my_user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'L\'utilisateur n\'existe pas.')
            return render(request, 'autentification/login.html')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        elif my_user.is_active == False:
            messages.error(request, 'Vous n\'avez pas encore confirmé votre adresse e-mail. Veuillez vérifier votre messagerie et cliquer sur le lien de confirmation pour activer votre compte')
            return redirect('login')
        else:
            messages.error(request, 'Oups ! Il semble que le mot de passe saisi soit incorrect.')
            return redirect('login')

    return render(request,'autentification/login.html')

def logout_fonction(request):
    logout(request)
    messages.success(request,'Vous avez été déconnecté avec succès. À bientôt !')
    return redirect('login')

@login_required
def diabetes(request):
    affiche = 0
    if request.method == "POST":
        affiche = 1
        save_data = request.POST.get('save') == 'on'
        age = request.POST['age']
        Pregnancies = Pregnancies = request.POST.get('Pregnancies', 0)
        Glucose = request.POST['Glucose']
        BloodPressure = request.POST['BloodPressure']
        SkinThickness = request.POST['SkinThickness']
        Insulin = request.POST['Insulin']
        BMI = request.POST['BMI']
        user_id = request.user.id
        DiabetesPedigreeFunction = request.POST['DiabetesPedigreeFunction']
        
        user_username = request.user.username
        input_data = np.array([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,age]])
        print(input_data)
        input_data = np.array(input_data, dtype=np.float32)
        print(input_data)
        prediction = diabetes_model.predict(input_data)
        prediction = round(float(prediction[0][0]), 2)
        print(prediction)
        if save_data:
            diabetes = Diabetes(pregnancies=Pregnancies,
                                glucose=Glucose,
                                blood_pressure=BloodPressure,
                                skin_thickness=SkinThickness,
                                insulin=Insulin,
                                bmi=BMI,
                                diabetes_pedigree_function=DiabetesPedigreeFunction,
                                age=age,
                                outcome = prediction,
                                user_id=user_id)
            diabetes.save()
        return render(request,'App/diabetes.html',{'age':11,'username':user_username,'prediction':prediction,'affiche':affiche})
    return render(request,'App/diabetes.html')

@login_required
def cardio(request):
    affiche = 0
    if request.method == 'POST':
        affiche = 1
        save_data = request.POST.get('save') == 'on'
        age = request.POST.get('age')
        Sexe = request.POST.get('Sexe')
        chest_pain = request.POST.get('chest_pain')
        blood_pressure = request.POST.get('blood_pressure')
        cholestoral = request.POST.get('cholestoral')
        blood_sugar = request.POST.get('blood_sugar')
        electrocardiographic = request.POST.get('electrocardiographic')
        heart_rate = request.POST.get('heart_rate')
        exercise = request.POST.get('exercise')
        slope = request.POST.get('slope')
        Oldpeak = request.POST.get('Oldpeak')
        major_vessels = request.POST.get('major_vessels')
        Thalassemia = request.POST.get('Thalassemia')
        user_id = request.user.id
        user_username = request.user.username
        input_data = np.array([[age,Sexe,chest_pain,blood_pressure,cholestoral,blood_sugar,electrocardiographic,heart_rate,exercise,Oldpeak,slope,major_vessels,Thalassemia]])
        # print(input_data)
        input_data = np.array(input_data, dtype=np.float32)
        # print(input_data)
        prediction = heart_model.predict(input_data)
        prediction = round(float(prediction[0][0]), 2)*100
        # print(prediction)
        if save_data:
            Cardio = PredictCardio( age=age,
                                    Sexe=Sexe,
                                    chest_pain=chest_pain,
                                    blood_pressure=blood_pressure,
                                    blood_sugar=blood_sugar,
                                    electrocardiographic=electrocardiographic,
                                    heart_rate=heart_rate,
                                    cholestoral=cholestoral,
                                    exercise=exercise,
                                    slope=slope,
                                    Oldpeak=Oldpeak,
                                    major_vessels=major_vessels,
                                    Thalassemia=Thalassemia,
                                    target = prediction,
                                    user_id = user_id)
            Cardio.save()
        return render(request,'App/cardio.html',{'age':age,'username':user_username,'prediction':prediction,'affiche':affiche})
    return render(request,'App/cardio.html')
from django.core.files.uploadedfile import InMemoryUploadedFile
import io
@login_required
def pneumonia(request):
    affiche = 0
    if request.method == 'POST' and request.FILES['pneumonia']:
        affiche = 1
        fichier_telecharge = request.FILES['pneumonia']
        # Convertir le fichier téléchargé en bytes
        if isinstance(fichier_telecharge, InMemoryUploadedFile):
            fichier_bytes = fichier_telecharge.read()
            img_stream = io.BytesIO(fichier_bytes)
        else:
            img_stream = fichier_telecharge
        
        # Traiter l'image pour la prédiction
        img = image.load_img(img_stream, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array/255
        img_array = np.array(img_array)
        prediction = pneumonia_model.predict(img_array)
        prediction = round(float(prediction[0][0]), 2)*100
        print(prediction)
        # Enregistrez le fichier téléchargé dans le répertoire média
        with open(os.path.join(settings.MEDIA_ROOT,'photos' , fichier_telecharge.name), 'wb+') as destination:
            for chunk in fichier_telecharge.chunks():
                destination.write(chunk)
        # Enregistrer le chemin de l'image dans la base de données
        user_id = request.user.id
        image_obj = Pneumonia.objects.create(image=fichier_telecharge,target=prediction,user_id=user_id)
        user_username = request.user.username
        return render(request,'App/pneumonia.html',{'username':user_username,'prediction':prediction,'affiche':affiche})
    return render(request,'App/pneumonia.html')

def Confirm_email(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        my_user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        my_user = None

    if my_user is not None and generateToken.check_token(my_user, token):
        my_user.is_active  = True        
        my_user.save()
        messages.success(request,'Votre compte a été activé. Vous pouvez vous connecter en remplissant le formulaire ci-dessous.')
        return redirect('login')
    else:
        messages.error(request,"Échec de l'activation. Veuillez réessayer.")
        return redirect('register')

def forget_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        my_user = User.objects.get(email=email)
        
        current_site = get_current_site(request) 
        email_suject = "Confirmation de changement de mot de passe"
        messageConfirm = render_to_string("App/change_password.html", {
            'name': my_user.username,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(my_user.pk)),
            'token': generateToken.make_token(my_user)
        })
        
        email = EmailMessage(
            email_suject,
            messageConfirm,
            settings.EMAIL_HOST_USER,
            [my_user.email]
        )

        email.fail_silently = False
        email.send()
    return render(request,'autentification/forget_password.html')

def change_password(request, uidb64, token):
    if request.method == 'POST':
        new_password = request.POST.get('r_password')
        c_password = request.POST.get('c_password')
        if new_password != c_password:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
            return redirect('change_password', uidb64=uidb64, token=token)
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            my_user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            my_user = None

        if my_user is not None and generateToken.check_token(my_user, token):
            my_user.set_password(new_password)
            my_user.save()
            messages.success(request, 'Votre mot de passe a été réinitialisé. Veuillez vous connecter avec votre nouveau mot de passe.')
            return redirect('login')
        else:
            messages.error(request, 'La réinitialisation du mot de passe a échoué. Veuillez réessayer.')
            return redirect('change_password', uidb64=uidb64, token=token)
    return render(request, 'autentification/change_password.html', {'uidb64': uidb64, 'token': token})

