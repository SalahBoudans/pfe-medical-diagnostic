document.getElementById('resultCard').scrollIntoView({ behavior: 'smooth' });

        /*_________ diabetes________*/
function togglePregnanciesInput() {
    var sexInput = document.getElementById('sex');
    var pregnanciesInput = document.getElementById('Pregnancies');

    // If sex is women, enable the Pregnancies input, otherwise, disable it
    pregnanciesInput.disabled = (sexInput.value === 'men');
}
// Initial call to set the initial state based on the default value
togglePregnanciesInput();

function chooseFile() {
    document.getElementById("fileInput").click();
}
document.getElementById("fileInput").addEventListener("change", handleFile);

function handleFile(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = function(e) {
        const img = new Image();
        img.src = e.target.result;
        img.onload = function() {
            // Display the image
            document.body.appendChild(img);
            // You can now send the file to the server for further processing
        };
    };
    reader.readAsDataURL(file);
}