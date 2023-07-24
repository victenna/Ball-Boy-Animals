import pygame,random,time
pygame.init()
screen = pygame.display.set_mode((1200,900))
clock = pygame.time.Clock()
start = time.time()
donkeys=[pygame.image.load('donkey0.png'),pygame.image.load('donkey1.png')]
images1=[pygame.image.load('m_man0.png'),pygame.image.load('m_man1.png')]
bears=[pygame.image.load('b0.png'),pygame.image.load('b1.png')]
monkeys=[pygame.image.load('monkey0.png'),pygame.image.load('monkey1.png')]
wolfs=[pygame.image.load('wolf1.png'),pygame.image.load('wolf0.png')]
balls=[pygame.image.load('ball1.png'),pygame.image.load('ball1.png')]
bg=pygame.image.load('bg.png')
class Player():
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y

    def up_down(self,image,down):
        self.image = image
        self.down=down
        self.rect = self.image.get_rect(center=(self.x,self.y))
        
    def draw(self):
        screen.blit(self.image,self.rect)
donkey=Player(415,700)
boy1=Player(600,695)
bear=Player(800,720)
monkey=Player(155,750)
wolf=Player(1000,750)

class Ball():
    def __init__(self,image,x):
        super().__init__()
        self.image = image
        self.image=pygame.transform.scale(self.image,(30,30))
        self.x=x
        self.dy=-20
        
    def no_motion(self,y):
        self.y=y
        self.rect = self.image.get_rect(center=(self.x,self.y))
    def motion(self):
        self.dy=self.dy+0.5
        self.y=self.y+self.dy
        self.rect = self.image.get_rect(center=(self.x,self.y))
    
    def draw(self):
        screen.blit(self.image,self.rect)
ball=Ball(balls[0],425)# x coordinate
ball1=Ball(balls[1],595)# x coordinate
ball2=Ball(balls[1],800)# x coordinate
ball3=Ball(balls[0],150)# x coordinate
ball4=Ball(balls[0],1000)# x coordinate
while True:
    screen.blit(bg,(0,0))
    tt = (time.time())
    sec=round((tt - start),2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if sec<0.1:
        donkey.up_down(donkeys[0],0)
        ball.no_motion(625)# y coordinate

        boy1.up_down(images1[0],0)
        ball1.no_motion(605)# y coordinate
        
        bear.up_down(bears[0],0)
        ball2.no_motion(630)# y coordinate
        
        monkey.up_down(monkeys[0],0)
        ball3.no_motion(670)# y coordinate
        
        wolf.up_down(wolfs[0],0)
        ball4.no_motion(740)# y coordinate


    if sec>=0.1:
        donkey.up_down(donkeys[1],1)
        ball.motion()
        #print(ball.y,sec)
        
        boy1.up_down(images1[1],1)
        ball1.motion()
        
        bear.up_down(bears[1],1)
        ball2.motion()
        
        monkey.up_down(monkeys[1],1)
        ball3.motion()
        
        wolf.up_down(wolfs[1],1)
        ball4.motion()

        if sec>0.5 and collision:
        
            donkey.up_down(donkeys[0],0)
            boy1.up_down(images1[0],0)
            bear.up_down(bears[0],0)
            monkey.up_down(monkeys[0],0)
            wolf.up_down(wolfs[0],0)

            if collision==None:
                ball.motion()
                ball1.motion()
                ball2.motion()
                ball3.motion()
                ball4.motion()

            if collision:#!=None:
                ball.no_motion(625)
                ball1.no_motion(605)
                ball2.no_motion(630)
                ball3.no_motion(670)
                ball4.no_motion(740)
                if sec>1.4:
                    start = time.time()
                    tt = (time.time())
                    #sec=round((tt - start),1)
                    ball.dy=-20
                    ball1.dy=-20
                    ball2.dy=-20
                    ball3.dy=-20
                    ball4.dy=-20

    collision=ball.rect.colliderect(donkey.rect)
    donkey.draw()
    ball.draw()
    boy1.draw()
    ball1.draw()
    bear.draw()
    ball2.draw()
    monkey.draw()
    ball3.draw()
    wolf.draw()
    ball4.draw()
    pygame.display.update()
    clock.tick(60)

