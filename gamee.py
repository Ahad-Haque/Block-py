import pygame
import random
pygame.init()
win = pygame.display.set_mode((1280, 720))
n=0
ng=10
gg=20
ng2=10
pygame.display.set_caption("Squarey")
x = random.randint(0,1000)
y = random.randint(0,500)
baddyX = random.randint(0,1000)
baddyY = random.randint(0,1000)
vel = 20
baddyVel = 20
scr=255
run = True
def draw_game():
          win.fill((scr, 255, 255))
          pygame.draw.rect(win, (0, 0, 255), (x, y, 20, 20))
          pygame.draw.rect(win, (n, ng, ng2),(baddyX, baddyY, gg, gg))
          pygame.display.update()

while run:
      pygame.time.delay(10)
      if baddyX < x - 10:
          baddyX = baddyX + baddyVel
      elif baddyX > x + 10:
          baddyX = baddyX - baddyVel
      elif baddyY < y - 10:
          baddyY = baddyY +baddyVel
      elif baddyY > y + 10:
          baddyY = baddyY - baddyVel
      else:
          pygame.mixer.music.load("jump.mp3")
          pygame.mixer.music.play()
          
          pygame.draw.rect(win, (n, ng, ng2),(baddyX, baddyY, gg, gg))
          if n<255:
              n+=5
          elif n>=255:
              ng+=5
              if ng>255:
                  ng2+=10
                  ng=ng-5
          gg=gg+5
          if scr >10:
              scr-=10
              
          x = random.randint(0,1000)
          y = random.randint(0,500)
          pygame.draw.rect(win, (0, 0, 255), (x, y, 20, 20))
          pygame.mixer.music.stop()
      
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False
      draw_game()          
pygame.quit()