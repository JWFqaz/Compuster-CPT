enemy_x = 0
enemy_y = 0
enemy_sx = 0
enemy_sy = 10
enemy_sz = 100
player_sz=100
bullet_sy=10
score=1
text_color = color(96, 150, 186)
page = 0

def setup():
    size(800, 800)


def draw():
    if page == 0:
        background(155, 3, 255)
        fill(255)
        ellipse(100, 100, 40, 40)
    elif page == 1:
        background(255, 255, 0)
    elif page == 2:
        background(255, 100, 3)


def mousePressed():
    global page
    page += 1
    if page == 3:
         page = 0
         
def draw():
    global score
    global enemy_x 
    global enemy_y 
    global enemy_sx 
    global enemy_sy 
    global enemy_sz
    global player_sz

   
    background(0, 0, 0)
    x_player = mouseX
    y_player = mouseY
    plane = loadImage("plane.png")
    image(plane, x_player, y_player, player_sz, player_sz)
    
    enemy=loadImage('oe.jpg')
    noStroke()
    image(enemy, enemy_x, enemy_y, enemy_sz, enemy_sz)
    enemy_y += enemy_sy
    
    if enemy_y > height:
        enemy_y = 0
        enemy_x = random(5, width)
        score += 1
        
    r_enemy = enemy_sz/2
    r_player = player_sz/2
    a = enemy_x - x_player
    b = enemy_y - y_player
    d = sqrt(a**2 + b**2)
    if d<= r_enemy + r_player:
        score-= 1
        enemy_y = 0
        enemy_x = random(0, width)
        
    fill(text_color)
    textSize(40)
    textAlign(LEFT)
    text(score, 20, 50)
