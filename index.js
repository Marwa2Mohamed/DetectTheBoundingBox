/*global document*/
const fileInput = document.getElementById("imageFile"),
      imgCanvas = document.getElementById("img"),
      imgContext = imgCanvas.getContext("2d");
/* rendering the chosen image in canvas*/

fileInput.addEventListener('change', event => {
    // FILE NAME AND EXTENSION.
    const fileName = fileInput.files.item(0).name;
    fileExtension = fileName.replace(/^.*\./, '');

    if (fileExtension == 'png' || fileExtension == 'jpg' || fileExtension == 'jpeg' || fileExtension == 'apng' || fileExtension == 'avif'|| fileExtension == 'gif'|| fileExtension == 'jfif'
        || fileExtension == 'pjpeg' || fileExtension == 'pjp' || fileExtension == 'svg' || fileExtension == 'webp' || fileExtension == 'bmp' || fileExtension == 'ico' || fileExtension == 'cur'
        || fileExtension == 'tif' || fileExtension == 'tiff') {
        const reader = new FileReader(),
            image = new Image();
        reader.onload = e => {
            image.src = e.target.result;
            image.onload = function() {
                imgCanvas.width = image.width;
                imgCanvas.height = image.height;
                imgContext.drawImage(image, 0, 0);
            };
        }
        const file = event.target.files[0];
        reader.readAsDataURL(file);
    } else {
        alert("Only images are accepted");
    }
})