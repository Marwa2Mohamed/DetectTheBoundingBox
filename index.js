/*global document*/
const fileInput = document.getElementById("imageFile"),
      imgCanvas = document.getElementById("img"),
      imgContext = imgCanvas.getContext("2d");



fileInput.addEventListener('change', e => {
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
    
    const f = e.target.files[0];
    reader.readAsDataURL(f);
  
})