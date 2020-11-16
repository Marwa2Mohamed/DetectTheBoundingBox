/*global document*/

//Intizialize global element objects
const fileInput = document.getElementById("imageFile"),
      inputText = document.getElementsByClassName("coordinates"),
      imgCanvas = document.getElementById("img"),
      imgContext = imgCanvas.getContext("2d"),
      image = new Image();


//Initilize global variables
var height, width
    canvasX = imgCanvas.offsetLeft,
    canvasY = imgCanvas.offsetTop,
    last_mousex = last_mousey = 0,
    mousex = mousey = 0,
    X1 = Y1 = X2 = Y2 = X3 = Y3 = X4 = Y4 = 0,
    topRightX = topRightY = bottomLeftX = bottomLeftY = 0,
    mousedown = false;



/* rendering the chosen image in canvas*/

fileInput.addEventListener('change', event => {
    // FILE NAME AND EXTENSION.
    const fileName = fileInput.files.item(0).name.toLowerCase();
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

        /* start drawing rectangle or square on image in canvas*/

            //Mousedown

            imgCanvas.addEventListener('mousedown', function(e) {

                imgContext.clearRect(0, 0, imgCanvas.width, imgCanvas.height);
                imgContext.drawImage(image, 0, 0);
                last_mousex = parseInt(e.clientX-canvasX);
                last_mousey = parseInt(e.clientY-canvasY);
                mousedown = true;
            });

            //Mouseup
            imgCanvas.addEventListener('mouseup', function(e) {
                mousedown = false;
                /* begining of calculate and get the topright and bottomleft*/
                    calculateTheRectangleFourPoints();
                    getTopRight();
                    getBottomLeft();
                    setInputsValues(); // set the hidden inputs in form values to the calculated xs and ys
                /* end of calculate and get the topright and bottomleft*/
            });

            //Mousemove
            imgCanvas.addEventListener('mousemove', function(e) {
                    mousex = parseInt(e.clientX - canvasX);
                    mousey = parseInt(e.clientY- canvasY);

                if(mousedown) {
                    // imgContext.clearRect(0,0,imgCanvas.width,imgCanvas.height); //clear canvas
                    imgContext.beginPath();
                    width = mousex-last_mousex;
                    height = mousey-last_mousey;
                    imgContext.rect(last_mousex,last_mousey,width,height);
                    imgContext.strokeStyle = 'black';
                    imgContext.lineWidth = 10;
                    imgContext.stroke();
                }
          /* end drawing rectangle or square on image in canvas*/

        });
    } else {
        alert("Only images are accepted");
        location.reload();
    }

})
/* ending the chosen image in canvas*/

function calculateTheRectangleFourPoints() {
         /* Here I take the start point when the user started drawing (last_mousex & last_mousey) as the first point.
          * To calculate the other 3 point I add width , height or 0.
          * reminder: the x and y are inverted in web browsers
          * -ve width means the rectangle started from the right and moved to the left side
          * +ve width means the rectangle started from the left and moved to the right side
          * -ve height means the rectangle started from the bottom and moved upwards
          * +ve width means the rectangle started from the top and moved to downwards
          *  from those information I will calculate the four points
          *  */
        //First Point
            X1 = last_mousex;
            Y1 = last_mousey;
        //Second Point
            X2 = X1 + width;
            Y2 = Y1;
        //Third Point
            X3 = X1;
            Y3 = Y1 + height;
        //Fourth Point
            X4 = X2;
            Y4 = Y2 + height;

}
function getTopRight() {
    /* topRight ==> the largest x & smallest y*/
    topRightX = Math.max(X1,X2,X3,X4);
    switch (topRightX) {
        case X1:
        case X3:
            topRightY = Math.min(Y1,Y3);
            break;
        case X2:
        case X4:
            topRightY = Math.min(Y2,Y4);
            break;



    }
}
function getBottomLeft() {
    /* bottomLeft ==> the smallest x & largest y*/
    bottomLeftX = Math.min(X1,X2,X3,X4);
    switch (bottomLeftX) {
        case X1:
        case X3:
            bottomLeftY = Math.max(Y1,Y3);
            break;
        case X2:
        case X4:
            bottomLeftY = Math.max(Y2,Y4);
            break;
    }
}
function setInputsValues() {
        inputText[0].value = bottomLeftX;
        inputText[1].value = bottomLeftY;
        inputText[2].value = topRightX;
        inputText[3].value = topRightY;

}