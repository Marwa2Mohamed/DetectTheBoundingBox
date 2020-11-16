/*global document*/

//Intizialize global element objects
const fileInput = document.getElementById("imageFile"),
      output = document.getElementById("output"),
      rect ={},
      imgCanvas = document.getElementById("img"),
      imgContext = imgCanvas.getContext("2d"),
      image = new Image();


//Initilize global variables
var canvasX = imgCanvas.offsetLeft,
    canvasY = imgCanvas.offsetTop,
    last_mousex = last_mousey = 0,
    curr_mousex = curr_mousey = 0,
    mousedown = false, finished =false;



/* rendering the chosen image in canvas*/

fileInput.addEventListener('change', event => {
    // FILE NAME AND EXTENSION.
    const fileName = fileInput.files.item(0).name;
    fileExtension = fileName.replace(/^.*\./, '');

    if (fileExtension == 'png' || fileExtension == 'jpg' || fileExtension == 'jpeg' || fileExtension == 'apng' || fileExtension == 'avif'|| fileExtension == 'gif'|| fileExtension == 'jfif'
        || fileExtension == 'pjpeg' || fileExtension == 'pjp' || fileExtension == 'svg' || fileExtension == 'webp' || fileExtension == 'bmp' || fileExtension == 'ico' || fileExtension == 'cur'
        || fileExtension == 'tif' || fileExtension == 'tiff') {
        const reader = new FileReader();
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
        imgCanvas.style.cursor = "crosshair";
        init();
    } else {
        alert("Only images are accepted");
        location.reload();
    }

})
/* ending the chosen image in canvas*/

/* start drawing rectangle or square on image in canvas*/
//Mousedown
function init() {
        imgCanvas.addEventListener("mousemove", function (event) {
            findxy('move', event)
        }, false);
        imgCanvas.addEventListener("mousedown", function (event) {
            findxy('down', event)
        }, false);
        imgCanvas.addEventListener("mouseup", function (event) {
            findxy('up', event)
        }, false);
        imgCanvas.addEventListener("mouseout", function (event) {
            findxy('out', event)
        }, false);
}
function findxy(res, event) {
        if (res == 'down') {
            if(finished == true) {
                imgContext.clearRect(0, 0, imgCanvas.width, imgCanvas.height);
                imgContext.drawImage(image, 0, 0);
                curr_mousex=curr_mousey=last_mousex= last_mousey= 0;

            }
            if( last_mousex == 0) {
                curr_mousex = event.clientX - imgCanvas.getBoundingClientRect().x;
                curr_mousey = event.clientY - imgCanvas.getBoundingClientRect().y;
            } else {
                last_mousex = event.clientX - imgCanvas.getBoundingClientRect().x;
                last_mousey = event.clientY - imgCanvas.getBoundingClientRect().y;
            }
            mousedown = true;
            console.log("last_mousex: " + last_mousex);
            console.log("last_mousey: " + last_mousey );
        }
        if (res == 'up' || res == "out") {
            mousedown = false;
        }
        if (res == 'move') {
            if (mousedown) {
                if(last_mousex == 0){
                    last_mousex = event.clientX - imgCanvas.getBoundingClientRect().x;
                    last_mousey = event.clientY - imgCanvas.getBoundingClientRect().y;
                } else {
                    curr_mousex = event.clientX - imgCanvas.getBoundingClientRect().x;
                    curr_mousey = event.clientY - imgCanvas.getBoundingClientRect().y;
                }
                draw();
                finished = true;
            }
        }
    }
    function draw() {
    imgContext.beginPath();
        var width = curr_mousex-last_mousex;
        var height = curr_mousey-last_mousey;


        imgContext.rect(last_mousex,last_mousey,width,height);
        imgContext.strokeStyle = 'red';
        imgContext.lineWidth = 10;
        imgContext.stroke();
    }

/* end drawing rectangle or square on image in canvas*/