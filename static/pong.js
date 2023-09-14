var pongcanvas = document.getElementById("ponggame")
var ctx = pongcanvas.getContext("2d")

var player1 = {x:0,y:0,width:20,height:100,color:"#FF0000"}
var player2 = {x:580,y:0,width:20,height:100,color:"#00FF00"}
var ball = {x:290,y:290,width:20,height:20,color:"#FFFFFF"}
var speedplayer = 5
var speedball = 5
var start = false

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
        || rect1.right < rect2.right
        || rect1.left > rect2.right
        )
}

function checkCollisionWall(ball)
{
    var ballBounds = getRectBounds(ball)
    return (
        ballBounds.bottom > pongcanvas.height
        || ballBounds.top < 0
        || ballBounds.left < 0
        || ballBounds.right > pongcanvas.width
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

function moveBall(ball,angle){

    ball.x += Math.cos(angle) * speedball
    ball.y -= Math.sin(angle) * speedball

    if(checkCollision(ball,player1) || checkCollision(ball,player2w) || checkCollisionWall(ball)){
        speedball*=(-1)
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
    drawRect(player1)
    drawRect(player2)    
}

function draw(){
    clearCanvas()
    moveplayer(player1,player2)
    moveBall(ball,Math.PI/4)
    drawRect(ball)
}

let keys = {};
setInterval(draw,20)


window.addEventListener("keydown", function(e) {
    keys[e.key] = true;
});

window.addEventListener("keyup", function(e) {
    keys[e.key] = false;
});

