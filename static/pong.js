const ball = document.getElementById('ball');
const player1 = document.getElementById('box1');
const player2 = document.getElementById('box2');
const container = document.getElementById('ponggame');
const gameover = document.getElementById('gameoverdiv');

function checkCollision(div1, div2) {
    var rect1 = div1.getBoundingClientRect();
    var rect2 = div2.getBoundingClientRect();

    return !(rect1.bottom < rect2.top 
            || rect1.top > rect2.bottom
            || rect1.right < rect2.right
            || rect1.left > rect2.right)
}

// Set initial position
var posBallX = ball.offsetLeft;
var posBallY = ball.offsetTop;

const minX = player1.clientWidth
const minY = 0;
const maxX = container.clientWidth - player2.clientWidth - ball.clientWidth;
const maxY = container.clientHeight - ball.clientHeight;
const maxYplayer = container.clientHeight - player2.clientHeight; 
console.log({"maxYplayer":maxYplayer,"maxY":maxY,"maxX":maxX,"minX":minX,"minY":minY })
// Set the speed of movement
var speedX = 5;
var speedY = 5;

document.body.style.overflow = 'hidden';

setInterval(
    function(){
        // bug: Javascript takes posBallX/Y as string

        posBallX = posBallX + speedX;
        posBallY = posBallY + speedY;
        console.log({"posBallX":posBallX,"posBallY":posBallY})
        console.log({"maxYplayer":maxYplayer,"maxY":maxY,"maxX":maxX,"minX":minX,"minY":minY })
        console.log({"containerwidth":container.clientWidth,"containerheight":container.clientHeight})

        if (posBallX < minX && checkCollision(ball,player1)) {
            posBallX = minX;
            speedX *= -1; // Change direction
        } else if (posBallX > maxX && checkCollision(ball,player2)) {
            posBallX = maxX;
            speedX *= -1; // Change direction
        } 
        // else {
        //     var parentDiv = container.parentNode;
        //     console.log({"parentDiv":parentDiv})
        //     parentDiv.replaceChild(container, gameover)
        // }
    
        if (posBallY < minY) {
            posBallY = minY;
            speedY *= -1; // Change direction
        } else if (posBallY > maxY) {
            posBallY = maxY;
            speedY *= -1; // Change direction
        }
        
        ball.style.top = posBallY + 'px';
        ball.style.left = posBallX + 'px';
    },
    20
) // update pos every 20ms

// Listen for keydown event
window.addEventListener('keydown', function(e) {
    var p1top = player1.offsetTop
    var p2top = player2.offsetTop

    switch (e.key) {     
        case "w":
            {
                p1top = (p1top - 15);
            }
            break;
        case "s":
            {
                p1top = p1top + 15;
            }
            break;    
        case "ArrowUp":
            {    
                p2top = p2top - 15;
            }
            break;
        case "ArrowDown":
            {
                p2top = (p2top + 15);
            }
            break;
    }

    if (p1top < minY) {
        p1top = minY;
    } else if (p1top > maxYplayer) {
        p1top = maxYplayer;
    }

    if (p2top < minY) {
        p2top = minY;
    } else if (p2top > maxYplayer) {
        p2top = maxYplayer;
    }

    player1.style.top = p1top + "px";
    player2.style.top = p2top + "px";
});
  

// In this code, we’re listening for the keydown event on the window object. When a key is pressed, we check if it’s one of the arrow keys and adjust our posX and posY variables accordingly. We then update the top and left CSS properties of our div to move it.

// Please replace 'yourDivId' with the actual id of your HTML element. Also, ensure that this script is either placed at the end of your HTML body or is run after the DOM has fully loaded, to make sure that the element can be correctly selected with document.getElementById.

// Also, make sure your div has a CSS position value of absolute, relative, or fixed, otherwise the top and left properties will have no effect.

// Remember to add boundary checks if you don’t want your div to be able to move outside of the viewport or another container.