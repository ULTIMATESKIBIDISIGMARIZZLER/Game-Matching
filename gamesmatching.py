import pygame

pygame.init()
WIDTH,HEIGHT=600,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Games Matching")

screen.fill(color=(0,0,0))

pygame.display.update()

subway_surfer=pygame.image.load("Lesson 7/images/Subwaysurfers.png")
ludo=pygame.image.load("Lesson 7/images/Ludo.png")
temple=pygame.image.load("Lesson 7/images/Temple.png")
candy=pygame.image.load("Lesson 7/images/Candycrush.png")

screen.blit(subway_surfer, (150,100))
screen.blit(ludo, (150,200))
screen.blit(temple, (150,300))
screen.blit(candy, (150,400))

font=pygame.font.SysFont("Georgia",36)
text1=font.render("Ludo",True,(255,255,255))
text2=font.render("Candy Crush",True,(255,255,255))
text3=font.render("Subway Surfers",True,(255,255,255))
text4=font.render("Temple Run",True,(255,255,255))

screen.blit(text1,(350,100))
screen.blit(text2,(350,200))
screen.blit(text3,(350,300))
screen.blit(text4,(350,400))

pygame.display.update()

while True:
    event=pygame.event.poll()
    if event.type==pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,(255,0,0),(pos),20,0)
        pygame.display.update()

    elif event.type==pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen,(0,0,250),(pos),(pos2),4)
        pygame.draw.circle(screen,(255,255,0),(pos2),20,0)
        pygame.display.update()

