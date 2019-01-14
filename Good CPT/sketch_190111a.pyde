enemy_x = 0
enemy_y = 0
enemy_sx = 0
enemy_sy = 100
enemy_sz = 100
player_sz=100
score=1
text_color = color(96, 150, 186)
page = 0

def setup():
    size(800, 800)
    
def draw():
  background(255, 255, 224)
  menu()
  game()
  
def menu():
    textSize(64)
    text("Welcome To The Odessy of air fight", 120,250)
    textAlign(CENTER)
    fill(255,255,224)
         
def game():
    global score
    global enemy_x 
    global enemy_y 
    global enemy_sx 
    global enemy_sy 
    global enemy_sz
    global player_sz


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
    
def win_or_lose():
    global score
    while True:
     if score<0:
        break
