# 🏥 Application Web de Diagnostic Médical assisté par le Machine Learning

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-5.0-darkgreen)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📋 Table des matières

- [Vue d'ensemble](#vue-densemble)
- [Contexte et Problématique](#contexte-et-problématique)
- [Objectifs](#objectifs)
- [Fonctionnalités principales](#fonctionnalités-principales)
- [Architecture du système](#architecture-du-système)
- [Technologies utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Configuration](#configuration)
- [Exécution du projet](#exécution-du-projet)
- [Utilisation](#utilisation)
- [API Endpoints](#api-endpoints)
- [Base de données](#base-de-données)
- [Modèles de Machine Learning](#modèles-de-machine-learning)
- [Améliorations futures](#améliorations-futures)
- [Auteurs](#auteurs)

---

## 🎯 Vue d'ensemble

Cette application web innovante intègre des techniques avancées de **Machine Learning** et de **traitement du langage naturel (NLP)** pour fournir un système de diagnostic médical assisté. Elle permet aux utilisateurs de :

- **Prédire le risque de diabète** en saisissant leurs indicateurs de santé
- **Évaluer le risque de maladies cardiovasculaires** à partir de données médicales
- **Détecter la pneumonie** via l'analyse d'images radiographiques thoraciques
- **Consulter un Chatbot médical interactif** pour obtenir des réponses à leurs questions

L'application combine une **interface web conviviale** avec des **modèles de prédiction performants**, offrant une solution accessible et efficace pour la surveillance de la santé.

---

## 📌 Contexte et Problématique

### Contexte
Face à l'évolution constante de la médecine et l'importance croissante des données dans le secteur de la santé, les sciences de données jouent un rôle central en permettant d'analyser et de tirer des prédictions à partir de vastes ensembles de données médicales.

### Problématique
Le domaine de la santé est confronté à plusieurs défis majeurs :

- **Coût élevé** des méthodes traditionnelles de diagnostic et de suivi
- **Inaccessibilité** de services de santé pour certaines populations
- **Manque de personnalisation** dans les conseils de santé
- **Nécessité d'une surveillance régulière** et de prévention précoce des maladies

### Solution proposée
Une plateforme web innovante combinant :
- ✅ Système d'authentification sécurisé pour protéger les données médicales
- ✅ Modèles de Machine Learning pour prédictions précises
- ✅ Interface conviviale pour saisie facile des données
- ✅ Chatbot médical pour support en temps réel

---

## 🎓 Objectifs

Le projet vise à développer un système complet de diagnostic médical assisté par Machine Learning répondant aux objectifs suivants :

1. **Prédiction des maladies** : Développer des modèles précis et fiables pour :
   - Prédiction du diabète
   - Prédiction des maladies cardiovasculaires
   - Détection de la pneumonie

2. **Accessibilité** : Offrir une solution web accessible et facile à utiliser pour la surveillance de la santé

3. **Sécurité des données** : Implémenter un système d'authentification robuste pour protéger les données médicales sensibles

4. **Support utilisateur** : Intégrer un chatbot médical pour répondre aux questions des utilisateurs en temps réel

---

## ✨ Fonctionnalités principales

### 1. Authentification et Gestion des utilisateurs
- **Inscription** : Création de compte avec validation d'email
- **Connexion** : Authentification sécurisée
- **Oubli de mot de passe** : Récupération par email avec token sécurisé
- **Modification de mot de passe** : Changement sécurisé du mot de passe
- **Déconnexion** : Fermeture sécurisée de session

### 2. Prédiction du Diabète
- Formulaire intuitif avec 8 indicateurs :
  - Âge
  - Nombre de grossesses
  - Taux de glucose
  - Pression artérielle
  - Épaisseur de la peau
  - Taux d'insuline
  - Indice de Masse Corporelle (IMC)
  - Historique familial de diabète
- Prédiction en temps réel basée sur le modèle séquentiel
- Affichage du pourcentage de risque et recommandations

### 3. Prédiction des Maladies Cardiovasculaires
- Formulaire complet avec 13 paramètres médicaux :
  - Âge et sexe
  - Type de douleur thoracique
  - Pression artérielle
  - Taux de cholestérol
  - Taux de glucose sanguin
  - Résultats électrocardiographiques
  - Fréquence cardiaque maximale
  - ET 6 autres indicateurs clés
- Analyse prédictive sophistiquée
- Recommandations personnalisées basées sur les résultats

### 4. Détection de la Pneumonie
- **Upload d'images radiographiques** thoraciques
- **Analyse par vision par ordinateur** (modèle VGG16)
- Résultats binaires : Pneumonie détectée / Non détectée
- Affichage du pourcentage de confiance
- Conseils médicaux adaptés

### 5. Chatbot Médical Interactif
- Interface de chat en temps réel
- Compréhension du langage naturel (NLP)
- Réponses basées sur la base de connaissances médicales
- Support multilingue (adaptable)
- Questions/réponses sur les prédictions et la santé générale

### 6. Dashboard utilisateur
- Vue d'ensemble de la santé
- Historique des prédictions
- Accès rapide aux services de diagnostic
- Interface responsive et intuitive

---

## 🏗️ Architecture du système

```
┌─────────────────────────────────────────────────────────────┐
│                     COUCHE PRÉSENTATION                      │
│  (HTML/CSS/JavaScript - Bootstrap - Interface utilisateur)   │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                  COUCHE MÉTIER (Django)                      │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Views: Gestion des requêtes HTTP                      │ │
│  │  - Authentification                                    │ │
│  │  - Prédictions                                         │ │
│  │  - Chatbot                                             │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Logique métier: Intégration ML/NLP                   │ │
│  │  - Chargement des modèles pré-entraînés              │ │
│  │  - Traitement des données utilisateur                │ │
│  │  - Génération des prédictions                        │ │
│  └────────────────────────────────────────────────────────┘ │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│              COUCHE DONNÉES & MODÈLES                         │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Base de données (SQLite3)                             │ │
│  │  - Utilisateurs                                        │ │
│  │  - Prédictions (Diabète, Cardio, Pneumonie)          │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Modèles de Machine Learning (Keras/TensorFlow)       │ │
│  │  - diabetes_prediction.h5 (Modèle Séquentiel)        │ │
│  │  - heart_prediction.h5 (Modèle Séquentiel)           │ │
│  │  - Pneumonia_prediction.h5 (VGG16)                   │ │
│  │  - chatbot_model.h5 (RNN pour NLP)                   │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Base de connaissances NLP (intents.json)             │ │
│  │  - Patterns et réponses du chatbot                    │ │
│  └────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

### Flux de données - Prédiction du Diabète

```
Utilisateur
    │
    ▼
[Formulaire avec 8 indicateurs]
    │
    ▼
[Validation des données]
    │
    ▼
[Normalisation des données]
    │
    ▼
[Modèle Séquentiel]
    │
    ▼
[Prédiction (0 ou 1)]
    │
    ▼
[Stockage en base de données]
    │
    ▼
[Affichage des résultats]
```

---

## 🛠️ Technologies utilisées

### Backend
- **Django 5.0** : Framework web Python pour la gestion des URLs et des vues
- **Python 3.8+** : Langage de programmation principal

### Machine Learning & Deep Learning
- **TensorFlow 2.x** : Bibliothèque open-source pour le Machine Learning
- **Keras** : API haute niveau pour créer et entraîner les modèles
- **NumPy** : Calculs numériques et manipulation de tableaux
- **Scikit-learn** : Prétraitement et évaluation des modèles

### Traitement du Langage Naturel
- **NLTK (Natural Language Toolkit)** : Bibliothèque pour NLP
  - Tokenization (division du texte en tokens)
  - Stemming (extraction de la racine des mots)
  - Classification de texte

### Frontend
- **HTML5** : Structure et contenu des pages web
- **CSS3** : Styles et mise en forme
- **JavaScript** : Interactivité et dynamisme côté client
- **Bootstrap 5** : Framework CSS pour interfaces réactives et responsives

### Base de données
- **SQLite3** : Base de données légère intégrée
- **Django ORM** : Mapping objet-relationnel

### Outils de développement
- **Visual Studio Code** : Éditeur de code
- **Git** : Contrôle de version
- **XAMPP** (optionnel) : Serveur local de développement

### Autres bibliothèques
- **Pillow** : Traitement d'images
- **Python Imaging Library (PIL)** : Manipulation d'images pour les radiographies

---

## 💻 Installation

### Prérequis

- **Python 3.8 ou supérieur**
- **pip** (gestionnaire de paquets Python)
- **Git** (optionnel, pour cloner le projet)

### Étapes d'installation

#### 1. Cloner ou télécharger le projet

```bash
# Via Git
git clone https://github.com/votre-username/medical-diagnosis-app.git
cd medical-diagnosis-app

# Ou télécharger et décompresser le dossier
```

#### 2. Créer un environnement virtuel

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

#### 3. Installer les dépendances

```bash
# Installer les dépendances du projet
pip install -r requirements.txt

# Dépendances principales :
# - Django==5.0.2
# - TensorFlow 2.x
# - Keras
# - NLTK
# - NumPy
# - Pillow
# - djangorestframework (optionnel, pour API)
```

#### 4. Appliquer les migrations de la base de données

```bash
# Se placer dans le répertoire du projet
cd PFE

# Appliquer les migrations
python manage.py migrate
```

#### 5. Créer un superutilisateur (Admin)

```bash
python manage.py createsuperuser
# Suivez les instructions pour créer un compte administrateur
```

---

## ⚙️ Configuration

### Variables d'environnement importantes

Le fichier `PFE/settings.py` contient les configurations suivantes :

```python
DEBUG = True  # À passer à False en production

ALLOWED_HOSTS = []  # À remplir avec votre domaine en production

# Configuration Email (Gmail)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'votre-email@gmail.com'
EMAIL_HOST_PASSWORD = 'votre-mot-passe-app'
```

### Configuration des données sensibles

⚠️ **Pour la production**, créez un fichier `.env` pour stocker les informations sensibles :

```bash
# .env
SECRET_KEY=votre-clé-secrète
DEBUG=False
ALLOWED_HOSTS=votre-domaine.com

EMAIL_HOST_USER=votre-email@gmail.com
EMAIL_HOST_PASSWORD=votre-mot-passe-app
```

Notez que vous pouvez aussi utiliser le fichier d'exemple `PFE/settings_example.py` fourni : copiez-le en `PFE/settings.py` et remplacez les valeurs `<YOUR_...>` par vos informations (clé secrète, email, mot de passe/app-password, etc.).
Ne committez pas `PFE/settings.py` dans le dépôt public — il est déjà listé dans `.gitignore`.

---

## 🚀 Exécution du projet

### 1. Lancer le serveur Django

```bash
# Dans le répertoire du projet (PFE/)
python manage.py runserver
```

**Résultat attendu :**
```
Starting development server at http://127.0.0.1:8000/
```

### 2. Accéder à l'application

Ouvrez votre navigateur et allez à :
- **Application web** : `http://localhost:8000/`
- **Panneau admin** : `http://localhost:8000/admin/`

### 3. Se connecter

- Utilisez les identifiants du superutilisateur créé lors de la configuration
- Ou créez un nouveau compte via la page d'inscription

---

## 📖 Utilisation

### Flux utilisateur typique

#### 1. **Inscription et Authentification**

```
1. Cliquer sur "S'inscrire" depuis la page d'accueil
2. Remplir le formulaire (username, email, mot de passe)
3. Confirmer l'email via le lien envoyé
4. Se connecter avec les identifiants
```

#### 2. **Prédiction du Diabète**

```
1. Depuis le dashboard, cliquer sur "Prédiction Diabète"
2. Remplir les 8 indicateurs de santé :
   - Âge (en années)
   - Nombre de grossesses
   - Taux de glucose (mg/dL)
   - Pression artérielle (mmHg)
   - Épaisseur de la peau (mm)
   - Taux d'insuline (mU/L)
   - Indice de Masse Corporelle (IMC)
   - Historique familial de diabète (0 ou 1)
3. Cliquer sur "Prédire"
4. Visualiser le résultat et le pourcentage de risque
```

#### 3. **Prédiction des Maladies Cardiovasculaires**

```
1. Depuis le dashboard, cliquer sur "Prédiction Cardiovasculaire"
2. Remplir les 13 paramètres médicaux
3. Cliquer sur "Prédire"
4. Consulter les résultats et recommandations
```

#### 4. **Détection de la Pneumonie**

```
1. Depuis le dashboard, cliquer sur "Prédiction Pneumonie"
2. Uploader une image radiographique thoracique (format : JPG, PNG)
3. Cliquer sur "Analyser"
4. Visualiser le résultat (Pneumonie détectée ou Non)
5. Consulter le pourcentage de confiance
```

#### 5. **Utilisation du Chatbot Médical**

```
1. Cliquer sur "Chatbot" depuis le menu
2. Poser une question en langage naturel
   Exemple : "Quels sont les symptômes du diabète ?"
            "Comment réduire mon risque cardiovasculaire ?"
3. Lire la réponse du chatbot
4. Continuer la conversation
```

### Capture d'écran - Pages clés

> [Page d'accueil](./screenshots/home.png)
> 
> [Page de connexion](./screenshots/login.png)
> 
> [Dashboard utilisateur](./screenshots/dashboard.png)
> 
> [Prédiction du diabète](./screenshots/diabetes.png)
> 
> [Résultat de prédiction](./screenshots/result.png)
> 
> [Chatbot médical](./screenshots/chatbot.png)

---

## 🔌 API Endpoints

### Authentification

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET/POST | `/register/` | Inscription d'un nouvel utilisateur |
| GET/POST | `/login/` | Connexion utilisateur |
| GET | `/logout/` | Déconnexion utilisateur |
| GET/POST | `/forget_password/` | Récupération du mot de passe |
| GET/POST | `/change_password/<uidb64>/<token>/` | Changement du mot de passe |
| GET | `/confirm/<uidb64>/<token>/` | Confirmation de l'email |

### Prédictions (Medical Endpoints)

| Méthode | Endpoint | Description | Authentification |
|---------|----------|-------------|------------------|
| GET/POST | `/diabetes/` | Prédiction du diabète | ✅ Requise |
| GET/POST | `/cardio/` | Prédiction cardiovasculaire | ✅ Requise |
| GET/POST | `/pneumonia/` | Détection de pneumonie | ✅ Requise |

### Chatbot

| Méthode | Endpoint | Description | Authentification |
|---------|----------|-------------|------------------|
| GET/POST | `/chatbot` | Interaction avec le chatbot | ✅ Requise |

### Format des requêtes POST

#### Prédiction Diabète
```python
POST /diabetes/
Content-Type: application/x-www-form-urlencoded

pregnancies=2&glucose=140&blood_pressure=90&
skin_thickness=25&insulin=100&bmi=32.5&
diabetes_pedigree_function=0.612&age=45
```

#### Prédiction Cardiovasculaire
```python
POST /cardio/
Content-Type: application/x-www-form-urlencoded

age=59&Sexe=1&chest_pain=2&blood_pressure=120&
cholestoral=220&blood_sugar=0&electrocardiographic=2&
heart_rate=112&exercise=0&slope=1&Oldpeak=1.8&
major_vessels=1&Thalassemia=2
```

#### Détection Pneumonie
```python
POST /pneumonia/
Content-Type: multipart/form-data

image=<fichier_radiographie>
```

#### Chatbot
```javascript
POST /chatbot
Content-Type: application/x-www-form-urlencoded

msg="Quels sont les symptômes du diabète ?"

Response:
{
  "response": "Le diabète est caractérisé par..."
}
```

---

## 💾 Base de données

### Schéma de la base de données

```sql
-- Table Utilisateurs (Django User Model)
┌─────────────────────────────┐
│ User (Django Auth)          │
├─────────────────────────────┤
│ id (PK)                     │
│ username (unique)           │
│ email (unique)              │
│ password (hashed)           │
│ first_name                  │
│ last_name                   │
│ is_active                   │
│ date_joined                 │
└─────────────────────────────┘

-- Table Prédictions Diabète
┌─────────────────────────────────────────┐
│ App1_diabetes                           │
├─────────────────────────────────────────┤
│ id (PK)                                 │
│ user_id (FK) → User.id                 │
│ pregnancies (INT)                       │
│ glucose (INT)                           │
│ blood_pressure (INT)                    │
│ skin_thickness (INT)                    │
│ insulin (INT)                           │
│ bmi (FLOAT)                             │
│ diabetes_pedigree_function (FLOAT)      │
│ age (INT)                               │
│ outcome (FLOAT) [0.0 ou 1.0]           │
│ created_at (TIMESTAMP)                  │
└─────────────────────────────────────────┘

-- Table Prédictions Maladies Cardiovasculaires
┌──────────────────────────────────────────┐
│ App1_predictcardio                       │
├──────────────────────────────────────────┤
│ id (PK)                                  │
│ user_id (FK) → User.id                  │
│ age (INT)                                │
│ Sexe (INT) [0: Femme, 1: Homme]        │
│ chest_pain (INT) [0-3]                  │
│ blood_pressure (FLOAT)                   │
│ cholestoral (INT)                        │
│ blood_sugar (INT)                        │
│ electrocardiographic (INT)               │
│ heart_rate (INT)                         │
│ exercise (INT)                           │
│ slope (INT)                              │
│ Oldpeak (FLOAT)                          │
│ major_vessels (INT)                      │
│ Thalassemia (INT)                        │
│ target (FLOAT) [0.0 ou 1.0]             │
│ created_at (TIMESTAMP)                   │
└──────────────────────────────────────────┘

-- Table Prédictions Pneumonie
┌─────────────────────────────────────────┐
│ App1_pneumonia                          │
├─────────────────────────────────────────┤
│ id (PK)                                 │
│ user_id (FK) → User.id                 │
│ image (IMAGEFIELD) [path/to/image]     │
│ target (FLOAT) [0.0 ou 1.0]            │
│ created_at (TIMESTAMP)                  │
└─────────────────────────────────────────┘
```

### Modèles Django (ORM)

```python
# Voir App1/models.py pour la définition complète
from django.db import models
from django.contrib.auth.models import User

class Diabetes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ... 8 champs de prédiction
    outcome = models.FloatField(default=False)

class PredictCardio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ... 13 champs de prédiction
    target = models.FloatField(default=0)

class Pneumonia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos')
    target = models.FloatField(default=0)
```

### Requêtes SQL courantes

```sql
-- Récupérer l'historique des prédictions d'un utilisateur
SELECT * FROM App1_diabetes WHERE user_id = 1;

-- Calculer le pourcentage de prédictions positives
SELECT COUNT(*) * 100.0 / 
       (SELECT COUNT(*) FROM App1_diabetes) 
FROM App1_diabetes WHERE outcome = 1.0;

-- Récupérer les prédictions les plus récentes
SELECT * FROM App1_diabetes 
ORDER BY id DESC LIMIT 10;
```

---

## 🤖 Modèles de Machine Learning

### 1. Prédiction du Diabète - Modèle Séquentiel

**Architecture :**
```
Input Layer (8 features)
    ↓
Dense Layer (16 neurons, ReLU)
    ↓
Dense Layer (8 neurons, ReLU)
    ↓
Output Layer (1 neuron, Sigmoid)
    ↓
Binary Classification (0 ou 1)
```

**Paramètres :**
- Loss Function : BinaryCrossentropy
- Optimizer : Adam
- Epochs : 1000
- Accuracy : 90%

**Features d'entrée :**
1. Pregnancies (nombre de grossesses)
2. Glucose (taux de glucose)
3. BloodPressure (pression artérielle)
4. SkinThickness (épaisseur de la peau)
5. Insulin (taux d'insuline)
6. BMI (indice de masse corporelle)
7. DiabetesPedigreeFunction (historique familial)
8. Age (âge)

### 2. Prédiction des Maladies Cardiovasculaires - Modèle Séquentiel

**Architecture :**
```
Input Layer (13 features)
    ↓
Dense Layer (26 neurons, ReLU)
    ↓
Dense Layer (13 neurons, ReLU)
    ↓
Dense Layer (26 neurons, Softmax)
    ↓
Dense Layer (13 neurons, Softmax)
    ↓
Output Layer (1 neuron, Sigmoid)
    ↓
Binary Classification
```

**Paramètres :**
- Loss Function : BinaryCrossentropy
- Optimizer : Adam
- Epochs : 1100
- Accuracy : 94%

**Features d'entrée :**
13 paramètres incluant : age, sexe, type de douleur thoracique, pression artérielle, cholestérol, etc.

### 3. Détection de Pneumonie - VGG16 (Convolutional Neural Network)

**Architecture :**
```
Input Layer (224x224x3 - images RGB)
    ↓
13 Couches Convolutionnelles (ReLU)
    ↓
Max Pooling Layers (réduction dimensionnelle)
    ↓
3 Couches Fully Connected (Dense)
    ↓
Output Layer (1 neuron, Softmax)
    ↓
Binary Classification (Pneumonie / Normal)
```

**Paramètres :**
- Architecture : VGG16 pré-entraîné
- Image Size : 224x224 pixels
- Données d'entraînement : 5216 images
- Accuracy : 93%
- Precision : 93%
- Recall : 96%

**Dataset :**
- Train : 1341 normal + 3875 pneumonie
- Test : 243 normal + 390 pneumonie
- Validation : 8 normal + 8 pneumonie

### 4. Chatbot Médical - Réseau de Neurones (NLP)

**Architecture :**
```
Input (Bag of Words)
    ↓
Embedding Layer
    ↓
Hidden Layers (128 neurons, ReLU)
    ↓
Output Layer (softmax - classification par intents)
```

**Traitement NLP :**
1. **Tokenization** : Division du texte en mots
2. **Lowercase** : Conversion en minuscules
3. **Stemming** : Extraction de la racine des mots
4. **Bag of Words** : Vectorisation des tokens
5. **Prédiction d'intent** : Classification du message
6. **Réponse** : Sélection aléatoire dans les réponses possibles

**Performance :**
- Couverture d'intents : ~50 catégories médicales
- Temps de réponse : < 100ms

---

## 🚀 Améliorations futures

### Court terme
- [ ] **Interface responsive améliorée** : Optimisation mobile complète
- [ ] **Historique détaillé** : Graphiques de suivi des tendances sanitaires
- [ ] **Export de rapports** : PDF/Excel des prédictions
- [ ] **Notifications** : Alertes pour résultats anormaux
- [ ] **Localisation** : Support de plusieurs langues

### Moyen terme
- [ ] **API REST complète** : Utilisation de Django REST Framework
- [ ] **Authentification OAuth** : Connexion via Google/Facebook
- [ ] **Intégration EHR** : Connexion aux dossiers médicaux électroniques
- [ ] **Améliorations ML** : Modèles plus sophistiqués et précis
- [ ] **Tests automatisés** : Suite de tests complète

### Long terme
- [ ] **Application mobile** : React Native / Flutter
- [ ] **Cloud deployment** : AWS, Azure, ou Google Cloud
- [ ] **Intégration IA avancée** : GPT-4, modèles transformers
- [ ] **Téléconsultation** : Vidéoconférence avec professionnels
- [ ] **Bases de données distribuées** : Pour scalabilité
- [ ] **Conformité RGPD/HIPAA** : Normes internationales
- [ ] **Intelligence artificielle explicable (XAI)** : Justification des prédictions

---

## 👥 Auteurs

| Rôle | Personne |
|------|----------|
| **Développeurs** | Salah Eddine Boudans, Imane Idhaddou |
| **Encadrant académique** | Mr. Youssef Taouil |
| **Établissement** | École Supérieure de Technologie - Essaouira |
| **Filière** | Informatique Décisionnelle et Sciences de Données |
| **Année** | 2023-2024 |

### Contact
- 📧 **Email** : contact@healthdiagnosis.fr (exemple)
- 🔗 **GitHub** : [Lien vers le repository](https://github.com)
- 📱 **LinkedIn** : [Profil LinkedIn](https://linkedin.com)

---

## 📝 Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](./LICENSE) pour plus de détails.

---

## 🤝 Contribution

Les contributions sont bienvenues ! Pour contribuer :

1. Fork le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/NouvelleFeature`)
3. Commitez vos changements (`git commit -m 'Ajout de NouvelleFeature'`)
4. Poussez vers la branche (`git push origin feature/NouvelleFeature`)
5. Ouvrez une Pull Request

---

## ⚠️ Avertissement médical

**Disclaimer important :**

Cette application est **destinée à des fins éducatives et de recherche uniquement**. Elle ne remplace pas un avis médical professionnel. 

- ❌ Ne pas utiliser pour l'auto-diagnostic médical
- ❌ Les résultats ne constituent pas un diagnostic médical officiel
- ✅ Consulter toujours un professionnel de santé qualifié
- ✅ Les prédictions doivent être validées par un médecin

---

## 📚 Ressources supplémentaires

### Documentation officielle
- [Django Documentation](https://docs.djangoproject.com/)
- [TensorFlow & Keras](https://www.tensorflow.org/)
- [NLTK](https://www.nltk.org/)
- [Bootstrap](https://getbootstrap.com/)

### Datasets utilisés
- [Diabetes Dataset](https://www.kaggle.com/datasets/nanditapore/healthcare-diabetes)
- [Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)
- [Chest X-ray Pneumonia](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

### Tutoriels et articles
- [Machine Learning Basics](https://machine-learning.fr/)
- [Django Tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
- [CNN for Medical Imaging](https://arxiv.org/)

---

## 🐛 Signalement de bugs

Si vous trouvez un bug, veuillez créer une **issue** avec :
- Description du problème
- Étapes pour reproduire
- Résultat attendu vs résultat obtenu
- Informations système (OS, version Python, etc.)

---

**Merci d'avoir utilisé notre application ! 🎉**

Pour toute question ou suggestion, n'hésitez pas à nous contacter.

*Dernière mise à jour : Juin 2026*
