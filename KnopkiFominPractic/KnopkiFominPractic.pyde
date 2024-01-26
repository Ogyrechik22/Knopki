# a = 25
# b = 25
# defa = 2.9
# defb = 3.2
# def setup():
#     size(1000,1000)
#     background(1)
#     frameRate(6000)
#     fill(255)
# def draw():
#     global a,b,defa,defb
#     background(1)
#     ellipse(a,b,50,50)
#     a = a + defa
#     b += defb
#     if a < 25:
#         defa = 2.9
#     if a > 975:
#         defa = -2.9
#     if b < 25:
#         defb = 3.2
#     if b > 950:
#         defb = -3.2
# a = 0
# def setup():
#     size(1000,1000)
#     background(1)
#     frameRate(600)
#     textSize(30)
# def draw():
#     background(1)
#     global a
#     rect(450,470,100,70)
#     text("ochki", 100,50)
#     text(a, 200,50)
# def mouseClicked():
#     global a
#     if mouseX > 449 and mouseX < 531 and mouseY > 469 and mouseY < 531:
#         a = a + 1
# x = 1
# def setup():
#     size(1000,1000)
#     frameRate(1000)
#     background(1)
#     stroke(255)
#     fill(255)
#     textSize(10)
# def draw():
#     global x
#     line(mouseX, mouseY,pmouseX,pmouseY)
#     text('G - green',20,20)
#     text('R - red',20,30)
#     text('O - orange',20,40)
#     text('Y - yellow',20,50)
#     text('H - black',20,60)
#     text('W - white',20,70)
#     text('C - cyan',20,80)
#     text('B - blue',20,90)
#     text('L - clean',20,100)
#     text('S - strk more',20,110)
#     text('M - strk low',20,120)
#     text('G - lastik',20,130)
#     if keyPressed:
#         if key == 'r' or key == 'R':
#             stroke(255,3,3)
#         elif key == 'o' or key == 'O':
#             stroke(255,145,3)
#         elif key == 'y' or key == 'Y':
#             stroke(255,245,3)
#         elif key == 'g' or key == 'G':
#             stroke(3,255,21)
#         elif key == 'h' or key == 'H':
#             stroke(1)
#         elif key == 'w' or key == 'W':
#             stroke(255)
#         elif key == 'c' or key == 'C':
#             stroke(3,255,240)
#         elif key == 'b' or key == 'B':
#             stroke(3,29,255)
#         elif key == 'l' or key == 'L':
#             clear()
#         elif key == 's' or key == 'S':
#             x = x + 1
#             strokeWeight(x)
#         elif key == 'n' or key == 'N':
#             x = x - 1
#             strokeWeight(x)
#         elif key == 'x' or key == 'X':
#             noStroke()
#             fill(1)
#             rect(mouseX, mouseY,20,20)
#             strokeWeight(1)
#             fill(255)
# def setup():
#     size(1000,1000)
#     background(1)
#     frameRate(60)
#     rectMode(CENTER)
#     fill(0)
#     noStroke()
# def draw():
#     background(1)
#     rect(mouseX,mouseY,50,50)
#     if mousePressed:
#         fill(255)
# def mouseReleased():
#     fill(1)
# a = 0
# b = 0
# def setup():
#     size(1000,1000)
#     background(1)
#     frameRate(60)
#     textSize(40)
# def draw():
#     global a,b
#     background(1)
#     rect(450,500,100,70)
#     text(b, 200,50)
#     a = a + 1
#     if a >= 1800:
#         noLoop()
#         background(1)
#         text("YOU LOSE!!!", 400,500)
#     if b == 30:
#         noLoop()
#         background(1)
#         text("YOU WIN!!!", 410,500)
# def mouseClicked():
#     global b
#     if mouseX > 449 and mouseX < 531 and mouseY > 469 and mouseY < 531:
#         b = b + 1
# w = 1
# def setup():
#     size(1000,1000)
#     background(1)
#     frameRate(10)
#     strokeWeight(1)
# def draw():
#     global w
#     stroke(random(0,255),random(0,255),random(0,255))
#     line(0,0,random(1,999),random(1,999))
#     if keyPressed == True:
#         if key == 'p' or key == 'P':
#             w = w + 1           
#             strokeWeight(w)
#         if key == 'm' or key == 'M':
#             w = w - 1
#             strokeWeight(w)
#         if key == 'c' or key == 'C':
#             background(1)
#         if key == 'r' or key == 'R':
#             noStroke()
#             fill(1)
#             ellipse(mouseX,mouseY,30,30)
#             fill(255)
#             strokeWeight(w)
#     if mousePressed == True:
#         noLoop()
# def mouseReleased():
#     loop()
            
    
    
    
    
    
        
    
