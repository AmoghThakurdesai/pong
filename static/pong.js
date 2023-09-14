var pongcanvas = document.getElementById("ponggame")
var ctx = pongcanvas.getContext("2d")


var player1 = {x:10,y:250,width:10,height:30,color:"#FF0000"}
var player2 = {x:580,y:250,width:10,height:30,color:"#00FF00"}
var ball = {x:290,y:290,width:8,height:8,color:"#FFFFFF"}
var speedplayer = 5
var speedball = 5
var speedballx = speedball
var speedbally = speedball
var start = false
var ballAngle = getRandomAngle()
var gameover = false
var player1score = 0
var player2score = 0
const GAMEOVERMSG = "GAME OVER!!"

function getRectBounds(rect){
    return {
        top: rect.y,
        left: rect.x,
        bottom: rect.y + rect.height,
        right: rect.x + rect.width
    }
}



function checkCollision(r1, r2) {
    var rect1 = getRectBounds(r1)
    var rect2 = getRectBounds(r2)

    return !(
        rect1.bottom < rect2.top 
        || rect1.top > rect2.bottom
        || rect1.right < rect2.left
        || rect1.left > rect2.right
        )
}

function checkCollisionWallY(ball)
{
    var ballBounds = getRectBounds(ball)
    return (
        ballBounds.bottom > pongcanvas.height
        || ballBounds.top < 0
    )
}

function checkCollisionWallleft(ball){
    var ballBounds = getRectBounds(ball)
    return (
        ballBounds.left < 0
    )
}

function checkCollisionWallright(ball){
    var ballBounds = getRectBounds(ball)
    return (
        ballBounds.right > pongcanvas.width
    )
} 
function drawRect(rect){
    ctx.fillStyle = rect.color
    ctx.fillRect(rect.x,rect.y,rect.width,rect.height)
}

function clearCanvas(){
    ctx.clearRect(0,0,pongcanvas.width,pongcanvas.height)
}

function getRandomAngle(){
    var randomangle = (-Math.PI + Math.random() * (2*Math.PI))
    if(randomangle==(Math.PI / 2) || randomangle==(-Math.PI / 2)){
        randomangle = (-Math.PI + Math.random() * (2*Math.PI))
    }
    return randomangle
}


function moveBall(ball){
    if(checkCollision(ball,player1) || checkCollision(player2,ball)){
        speedballx*=(-1)
    }
    else if(checkCollisionWallY(ball)){
        speedbally*=(-1)
    }
    else if(checkCollisionWallleft(ball)){
        gameover=true
        player2score+=1;
        console.log({"p2scorechange":player2score})
    }
    else if(checkCollisionWallright(ball)){
        gameover=true
        player1score+=1;
        console.log({"p1scorechange":player1score})
    }

    if(!gameover)
    {
        ball.x += Math.cos(ballAngle) * speedballx
        ball.y -= Math.sin(ballAngle) * speedbally
    }
}



function moveplayer(player1,player2){
    if(keys['w'] && player1.y > 0){
        player1.y -= speedplayer;
    }
    if(keys['s'] && player1.y < (pongcanvas.height - player1.height)){
        player1.y += speedplayer;
    }
    if(keys['ArrowUp'] && player2.y > 0){
        player2.y -= speedplayer;
    }
    if(keys['ArrowDown'] && player2.y < (pongcanvas.height - player2.height)){
        player2.y += speedplayer;
    }
    // if(keys['w'] && checkCollisionWall(player1)){
    //     player1.y -= speedplayer;
    // }
    // if(keys['s'] && checkCollisionWall(player1)){
    //     player1.y += speedplayer;
    // }
    // if(keys['ArrowUp'] && checkCollisionWall(player2)){
    //     player2.y -= speedplayer;
    // }
    // if(keys['ArrowDown'] && checkCollisionWall(player2)){
    //     player2.y += speedplayer;
    // }
    drawRect(player1)
    drawRect(player2)    
}

function draw(){
    clearCanvas()
    moveplayer(player1,player2)
    moveBall(ball)
    drawRect(ball)
    if(gameover){
        clearInterval(gameloop)
        clearCanvas()
        ctx.font = "30px Arial";
        ctx.textAlign = "center";
        ctx.fillText(`${GAMEOVERMSG} Score: ${player1score} - ${player2score}`, pongcanvas.width/2, pongcanvas.height/2);
    }
}

let keys = {};
let gameloop = setInterval(draw,20)


window.addEventListener("keydown", function(e) {
    keys[e.key] = true;
});

window.addEventListener("keyup", function(e) {
    keys[e.key] = false;
});

