plane_x = 0
# plane x
plane_sz=125
bullet_x = plane_x+48
bullet_sz=20
# bullet x
plane_y = 600
plane_w = plane_y
page=0
game = False
mouse = False
score=0
#enmey
enemy_x = 0
enemy_y = 0
enemy_sx = 0
enemy_sy = 30
enemy_sz = 120
score=0
text_color = color(96, 150, 186)

def setup():
    size(800, 800)
    frameRate(60)


def draw():
    global plane_x, bullet_x, plane_y, plane_w,game,page,mouse, plane_sz, page, score, enemy_y, enemy_sx, enemy_sy, enemy_sz, bullet_sz, enemy_x
    if page == 0:
        background(40)
        textSize(100)
        text("Air Fight",200,300)
        
        textSize(30)
        text("Press [h] to Begin",280,500) 
        
        textSize(40)
        text("Hints: try your best to get 10 scores!",80,600)

    if page ==2:
        background(40)
        textSize(60)
        text("Try again! Never give up!",70,400)
           
    if page==3:
       background(40)
       textSize(100)
       text("WELL DONE!",150,400)   
          
    if page == 1:
        background(40)
        y = 550
        image(loadImage("plane.png"), plane_x, plane_y, plane_sz, plane_sz)
        noStroke()
        fill(255)
        if mouse == False:
            noCursor()
 
        smooth();
        if mouse == True:
            plane_x = mouseX - 64
            cursor(CROSS)
        
    
        plane_w -= 160
        image(loadImage("BulletCol1OGApre1.png"), bullet_x, plane_w, bullet_sz, bullet_sz)
    
        if plane_w <= 0:
            plane_w = plane_y+10
            bullet_x = plane_x+48
            # if w != 0, the variable w and z will be isolate.
    
        enemy=loadImage('oe.png')
        noStroke()
        image(enemy, enemy_x, enemy_y, enemy_sz, enemy_sz)
        enemy_y += enemy_sy
    
        if enemy_y > height:
          enemy_y = 0
          enemy_x = random(5, width)
          score -= 1
        
    r_enemy = enemy_sz/2
    r_bullet = bullet_sz/2
    a = enemy_x - bullet_x
    b = enemy_y - plane_w
    d = sqrt(a**2 + b**2)
    if d<= r_enemy + r_bullet:
        score+= 1
        enemy_y = 0
        enemy_x = random(0, width)
        
    r_enemy = enemy_sz/2
    r_plane = plane_sz/2
    a = enemy_x - plane_x
    b = enemy_y - plane_y
    d = sqrt(a**2 + b**2)
    if d<= r_enemy + r_plane:
        score-= 1
        enemy_y = 0
        enemy_x = random(0, width)
        
    fill(text_color)
    textSize(40)
    textAlign(LEFT)
    text(score, 20, 50) 
    
    if score<0:
        page=2
            
    if score==10:
        page=3
        
    if keyPressed:
            if key == 'h' or key == 'H':
                page = 1
            if key == 'm' or key == 'M':
                if mouse == False:
                    
                    mouse = True
      
                else:
                    mouse = False
            
    
            if key == 'a' or key == 'A' and mouse == False:
                plane_x -= 60
            if key == 'd' or key == 'D' and mouse == False:
                plane_x += 60
            if key == 'w' or key == 'W' and mouse == False:
                plane_y -= 20
            if key == 's' or key == 'S' and mouse == False:
                plane_y += 20
                
            if page == 1:
      
                if plane_x >= 700:
                    plane_x = 700
                if plane_x <= 15:
                    plane_x = 15
