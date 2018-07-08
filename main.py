import socket
import pygame
##hc=input("host(h) or client(c)")
##pygame.init()
##gameDisplay=pygame.display.set_mode((600,600))
##s=socket.socket()
##host="localhost"
##port=12345
##if hc=='h'or'H':
##    s.bind((host,port))
##    s.listen(5)
##elif hc=='c' or 'C':
##        s.connect((host,port))
def game():
    s=socket.socket()
    host="localhost"
    port=12345
    s.bind((host,port))
    s.listen(5)
    pygame.init()
    gameDisplay=pygame.display.set_mode((800,800))

    white=[255,255,255]
    pygame.draw.rect(gameDisplay,white,[250,300,100,100],)
    pygame.draw.rect(gameDisplay,white,[355,300,100,100],)
    pygame.draw.rect(gameDisplay,white,[460,300,100,100],)
    pygame.draw.rect(gameDisplay,white,[250,405,100,100],)
    pygame.draw.rect(gameDisplay,white,[355,405,100,100],)
    pygame.draw.rect(gameDisplay,white,[460,405,100,100],)
    pygame.draw.rect(gameDisplay,white,[250,510,100,100],)
    pygame.draw.rect(gameDisplay,white,[355,510,100,100],)
    pygame.draw.rect(gameDisplay,white,[460,510,100,100],)
    cross=pygame.image.load("cross.png")
    circ=pygame.image.load("circ.png")
    LOSE=pygame.image.load("LOSE.png")
    WIN=pygame.image.load("WIN.png")
    turn1=True
    turn2=False
    p1=True
    p2=True
    p3=True
    p4=True
    p5=True
    p6=True
    p7=True
    p8=True
    p9=True
    x1=0
    x2=0
    x3=0
    x4=0
    x5=0
    x6=0
    x7=0
    x8=0
    x9=0
    while 1:
        c,addr=s.accept()
        while 1:
            
                
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
    ##                c.send(bytes("hi","utf-8"))
                    (x,y)=event.pos
    ##                if c.recv(1024) :
    ##                    pass
                
                    if(x>250 and x<350 and y>300 and y<400) and p1==True:
                        gameDisplay.blit(cross,(250,300))
                        pygame.display.update()
                        turn1=False
                        turn2=True
                        p1=False
                        x1=1
                        c.send(bytes("x1","utf-8"))
                    if(x>355 and x<455 and y>300 and y<400) and p2==True:
                        gameDisplay.blit(cross,(355,300))
                        turn1=False
                        turn2=True
                        p2=False
                        x2=1
                        c.send(bytes("x2","utf-8"))
                    if(x>455 and x<555 and y>300 and y<400)and p3==True:
                        gameDisplay.blit(cross,(455,300))
                        turn1=False
                        turn2=True
                        p3=False
                        x3=1
                        c.send(bytes("x3","utf-8"))
                    if(x>250 and x<350 and y>405 and y<505)and p4==True:
                        gameDisplay.blit(cross,(250,405))
                        turn1=False
                        turn2=True
                        p4=False
                        x4=1
                        c.send(bytes("x4","utf-8"))
                    if(x>355 and x<455 and y>405 and y<505)and p5==True:
                        gameDisplay.blit(cross,(355,405))
                        turn1=False
                        turn2=True
                        p5=False
                        x5=1
                        c.send(bytes("x5","utf-8"))
                    if(x>455 and x<555 and y>405 and y<505) and p6==True:
                        gameDisplay.blit(cross,(455,405))
                        turn1=False
                        turn2=True
                        p6=False
                        x6=1
                        c.send(bytes("x6","utf-8"))
                    if(x>250 and x<350 and y>510 and y<610)and p7==True:
                        gameDisplay.blit(cross,(250,510))
                        turn1=False
                        turn2=True
                        p7=False
                        x7=1
                        c.send(bytes("x7","utf-8"))
                    if(x>355 and x<455 and y>510 and y<610)and p8==True:
                        gameDisplay.blit(cross,(355,510))
                        turn1=False
                        turn2=True
                        p8=False
                        x8=1
                        c.send(bytes("x8","utf-8"))
                    if(x>455 and x<555 and y>510 and y<610)and p9==True:
                        gameDisplay.blit(cross,(455,510))
                        turn1=False
                        turn2=True
                        p9=False
                        x9=1
                        c.send(bytes("x9","utf-8"))
                    if ((x1+x5 +x9==3) or(x1+x2+x3==3) or(x1+x4+x7==3) or (x2+x5+x8==3) or(x3+x5+x7==3) or (x3+x6+x9==3) or(x4+x5+x6==3) or(x7+x8+x9==3)):
                       print("you win")
                       gameDisplay.blit(WIN,(0,0))
                       
                        
                    pygame.display.update()
                if turn2==True:
                    
                    f = c.recv(1024)
                    d=str(f)
                    print(d)
                    if p1==True and d=="b'x1'":
                        gameDisplay.blit(circ,(250,300))
                        turn2=False
                        turn1=True
                        p1=False
                        x1=10
                    if p2==True and d=="b'x2'":
                        gameDisplay.blit(circ,(355,300))
                        turn2=False
                        turn1=True
                        p2=False
                        x2=10
                    if(d=="b'x3'"and p3==True):
                        gameDisplay.blit(circ,(455,300))
                        turn2=False
                        turn1=True
                        p3=False
                        x3=10
                    if d=="b'x4'"and p4==True:
                        gameDisplay.blit(circ,(250,405))
                        turn2=False
                        turn1=True
                        p4=False
                        x4=10
                    if d=="b'x5'"and p5==True:
                        gameDisplay.blit(circ,(355,405))
                        turn2=False
                        turn1=True
                        p5=False
                        x5=10
                    if d=="b'x6'" and p6==True:
                        gameDisplay.blit(circ,(455,405))
                        turn2=False
                        turn1=True
                        p6=False
                        x6=10
                    if d=="b'x7'"and p7==True:
                        gameDisplay.blit(circ,(250,510))
                        turn2=False
                        turn1=True
                        p7=False
                        x7=10
                    if d=="b'x8'"and p8==True:
                        gameDisplay.blit(circ,(355,510))
                        turn2=False
                        turn1=True
                        p8=False
                        x8=10
                    if d=="b'x9'"and p9==True:
                        gameDisplay.blit(circ,(455,510))
                        turn2=False
                        turn1=True
                        p9=False
                        x9=10
                pygame.display.update()
##                if ((x1+x5 +x9==3) or(x1+x2+x3==3) or(x1+x4+x7==3) or (x2+x5+x8==3) or(x3+x5+x7==3) or (x3+x6+x9==3) or(x4+x5+x6==3) or(x7+x8+x9==3)):
##                   print("you win")
                if ((x1+x5 +x9==30) or(x1+x2+x3==30) or(x1+x4+x7==30) or (x2+x5+x8==30) or(x3+x5+x7==30) or (x3+x6+x9==30) or(x4+x5+x6==30) or(x7+x8+x9==30)):
                   print("you lose")
                   gameDisplay.blit(LOSE,(0,0))
def gameclient():
    s=socket.socket()
    host="localhost"
    port=12345
    s.connect((host,port))
    pygame.init()
    white=[255,255,255]

    gameDisplay=pygame.display.set_mode((800,800))

    pygame.draw.rect(gameDisplay,white,[250,300,100,100],)
    pygame.draw.rect(gameDisplay,white,[355,300,100,100],)
    pygame.draw.rect(gameDisplay,white,[460,300,100,100],)
    pygame.draw.rect(gameDisplay,white,[250,405,100,100],)
    pygame.draw.rect(gameDisplay,white,[355,405,100,100],)
    pygame.draw.rect(gameDisplay,white,[460,405,100,100],)
    pygame.draw.rect(gameDisplay,white,[250,510,100,100],)
    pygame.draw.rect(gameDisplay,white,[355,510,100,100],)
    pygame.draw.rect(gameDisplay,white,[460,510,100,100],)
    cross=pygame.image.load("cross.png")
    circ=pygame.image.load("circ.png")
    LOSE=pygame.image.load("LOSE.png")
    WIN=pygame.image.load("WIN.png")
    pygame.display.update()
    turn1=True
    turn2=False
    p1=True
    p2=True
    p3=True
    p4=True
    p5=True
    p6=True
    p7=True
    p8=True
    p9=True
    x1=0
    x2=0
    x3=0
    x4=0
    x5=0
    x6=0
    x7=0
    x8=0
    x9=0
    while 1:
        for event in pygame.event.get():
            if turn1==True:
                r=(s.recv(1024))
                e=str(r)
                if e=="b'x1'" and p1==True:
                    gameDisplay.blit(cross,(250,300))
                    pygame.display.update()
                    p1==False
                    turn1=False
                    turn2=True
                    x1=1
                if e=="b'x2'" and p2==True:
                    gameDisplay.blit(cross,(355,300))
                    pygame.display.update()
                    p2==False
                    turn1=False
                    turn2=True
                    x2=1
                if e=="b'x3'" and p3==True:
                    gameDisplay.blit(cross,(460,300))
                    pygame.display.update()
                    p3==False
                    turn1=False
                    turn2=True
                    x3=1
                if e=="b'x4'" and p4==True:
                    gameDisplay.blit(cross,(250,400))
                    pygame.display.update()
                    p4==False
                    turn1=False
                    turn2=True
                    x4=1
                if e=="b'x5'" and p5==True :
                    gameDisplay.blit(cross,(355,400))
                    pygame.display.update()
                    p5==False
                    turn1=False
                    turn2=True
                    x5=1
                if e=="b'x6'" and p6==True:
                    gameDisplay.blit(cross,(460,400))
                    pygame.display.update()
                    p6==False
                    turn1=False
                    turn2=True
                    x6=1
                if e=="b'x7'" and p7==True:
                    gameDisplay.blit(cross,(250,500))
                    pygame.display.update()
                    p7==False
                    turn1=False
                    turn2=True
                    x7=1
                if e=="b'x8'" and p8==True:
                    gameDisplay.blit(cross,(355,500))
                    pygame.display.update()
                    p8==False
                    turn1=False
                    turn2=True
                    x8=1
                if e=="b'x9'" and p9==True:
                    gameDisplay.blit(cross,(460,500))
                    pygame.display.update()
                    p9==False
                    turn1=False
                    turn2=True
                    x9=1
                if ((x1+x5 +x9==3) or(x1+x2+x3==3) or(x1+x4+x7==3) or (x2+x5+x8==3) or(x3+x5+x7==3) or (x3+x6+x9==3) or(x4+x5+x6==3) or(x7+x8+x9==3)):
                       print("you LOSE")
                       gameDisplay.blit(LOSE,(0,0))
            if turn2==True:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    (x,y)=event.pos
                    if(x>250 and x<350 and y>300 and y<400) and p1==True:
                        gameDisplay.blit(circ,(250,300))
                        turn2=False
                        turn1=True
                        p1=False
                        x1=10
                        s.sendto(bytes("x1","utf-8"),(host,port))
                    if(x>355 and x<455 and y>300 and y<400) and p2==True:
                        gameDisplay.blit(circ,(355,300))
                        turn2=False
                        turn1=True
                        p2=False
                        x2=10
                        s.sendto(bytes("x2","utf-8"),(host,port))
                    if(x>455 and x<555 and y>300 and y<400)and p3==True:
                        gameDisplay.blit(circ,(455,300))
                        turn2=False
                        turn1=True
                        p3=False
                        x3=10
                        s.sendto(bytes("x3","utf-8"),(host,port))
                    if(x>250 and x<350 and y>405 and y<505)and p4==True:
                        gameDisplay.blit(circ,(250,405))
                        turn2=False
                        turn1=True
                        p4=False
                        x4=10
                        s.sendto(bytes("x4","utf-8"),(host,port))
                    if(x>355 and x<455 and y>405 and y<505)and p5==True:
                        gameDisplay.blit(circ,(355,405))
                        turn2=False
                        turn1=True
                        p5=False
                        x5=10
                        s.sendto(bytes("x5","utf-8"),(host,port))
                    if(x>455 and x<555 and y>405 and y<505) and p6==True:
                        gameDisplay.blit(circ,(455,405))
                        turn2=False
                        turn1=True
                        p6=False
                        x6=10
                        s.sendto(bytes("x6","utf-8"),(host,port))
                    if(x>250 and x<350 and y>510 and y<610)and p7==True:
                        gameDisplay.blit(circ,(250,510))
                        turn2=False
                        turn1=True
                        p7=False
                        x7=10
                        s.sendto(bytes("x7","utf-8"),(host,port))
                    if(x>355 and x<455 and y>510 and y<610)and p8==True:
                        gameDisplay.blit(circ,(355,510))
                        turn2=False
                        turn1=True
                        p8=False
                        x8=10
                        s.sendto(bytes("x8","utf-8"),(host,port))
                    if(x>455 and x<555 and y>510 and y<610)and p9==True:
                        gameDisplay.blit(circ,(455,510))
                        turn2=False
                        turn1=True
                        p9=False
                        x9=10
                        s.sendto(bytes("x9","utf-8"),(host,port))
                    if ((x1+x5 +x9==30) or(x1+x2+x3==30) or(x1+x4+x7==30) or (x2+x5+x8==30) or(x3+x5+x7==30) or (x3+x6+x9==30) or(x4+x5+x6==30) or(x7+x8+x9==30)):
                       print("you lose")
                       gameDisplay.blit(WIN,(0,0))

        pygame.display.update()

if __name__=='__main__':
    hc=int(input("host(1) or client(2)"))
    if hc== 1 :
        game()
    if hc== 2:
        gameclient()
    
