plane_x = 0
# plane x
plane_sz=125
bullet_x = plane_x+48
bullet_sz=20
# bullet x
plane_y = 600
plane_w = plane_y
page=0
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
    def keyprocess():
        global plane_x, plane_y,page
        if key == 'l' or key == 'L':
            page = 1
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
                
    if page == 0:
        title_list = ['Press [l] to Begin',' use l to start','appuyez sur [l] pour commencer']
        for i in range(0,3):
            background(40)
            textSize(100)
            text("Air Fight",200,300)
            
            textSize(30)
            text(title_list[i],280,500) 
        
            textSize(40)
            text("Tips: try your best to get 20 scores!",80,600)
            
        
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
        #player
        
        if plane_w <= 0:
            plane_w = plane_y+10
            bullet_x = plane_x+48
            # if w != 0, the variable w and z will be isolate.
    
        enemy=loadImage('oe.png')
        noStroke()
        image(enemy, enemy_x, enemy_y, enemy_sz, enemy_sz)
        enemy_y += enemy_sy
        #emeny
        if enemy_y > height:
          enemy_y = 0
          enemy_x = random(5, width)
          score -= 1
        

    if page ==2:
        GG_list = ['GG','Try again!']
        background(40)
        textSize(200)
        text(GG_list[0],250,400)
        
        textSize(70)
        text(GG_list[1],250,600)
           
    if page==3:
       Good_list = ['WELL DONE!']
       background(40)
       textSize(100)
       text(Good_list[0],150,400)   
          
    def add_or_dis(): 
        global plane_x, bullet_x, plane_y, plane_w,game,page,mouse, plane_sz, page, score, enemy_y, enemy_sx, enemy_sy, enemy_sz, bullet_sz, enemy_x
        r_enemy = enemy_sz/2
        r_bullet = bullet_sz/2
        a = enemy_x - bullet_x
        b = enemy_y - plane_w
        d = sqrt(a**2 + b**2)
        
        r_enemy = enemy_sz/2
        r_plane = plane_sz/2
        a1 = enemy_x - plane_x
        b1 = enemy_y - plane_y
        e=sqrt(a1**2+b1**2)
        
        if d<= r_enemy + r_bullet:
            score+= 1
            enemy_y = 0
            enemy_x = random(0, width)
            #print("kk")
        #determine bullet and emeny
            
        
        elif e<= r_enemy + r_plane:
            score-= 1
            enemy_y = 0
            enemy_x = random(0, width)
            #print("tk")
        #determine plane amd enemy
        
    fill(text_color)
    textSize(40)
    textAlign(LEFT)
    text(score, 20, 50) 
    
    if score<0:
        page=2
            
    if score>=20:
        page=3

    add_or_dis()
    
    if keyPressed:
        keyprocess()
def use_for_test(input):
    return input
def test():
    assert use_for_test(1) == 1,'function error'
    assert use_for_test(10) == 10,'function error'
    assert use_for_test(100) == 100,'function error'
    print("pass all test")

test()
