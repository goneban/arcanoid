import pygame
import random
import time
pygame.init()
mv = pygame.display.set_mode((500, 500))
class TextArea:
    def __init__(self, x, y, weight, height, color):
        self.rect = pygame.Rect(x, y, weight, height)
        self.fill_color = color
    def set_color(self, color):
        self.fill_color = color
    
    def fill(self):
        pygame.draw.rect(mv, self.fill_color, self.rect)

class Label(TextArea):
    def set_text(self, text, fsize=26, text_color=(0, 0, 0)):
        self.text = text
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self, shiftx, shifty):
        self.fill()
        mv.blit(self.image, (self.rect.x + shiftx, self.rect.y + shifty))
    def win(self, x, y):
        return self.rect.collidepoint(x, y)
score = Label(360, 16, 40, 20, (200, 255, 255))
tim = Label(80, 16, 60, 20, (200, 255, 255))

spisok = [Label(90+90*i, 200, 80, 200, (255, 255, 0)) for i in range(4)]
spisok1 = [Label(85+90*i, 190, 90, 220, (0, 0, 100)) for i in range(4)]

mv.fill((200, 255, 255))
clock = pygame.time.Clock()
q = 0
for elem in spisok:
    elem.set_text('CLICK')
    elem.draw(13, 80)
    elem.fill()
for elem in spisok1:
    elem.set_color((0, 0, 100))
    elem.fill()
wait = 0
score.set_text('Счёт:')
score.draw(0, 0)
stat = Label(360, 40, 80, 30, (200, 255, 255))
l = 0
k = time.time()
t = 0
tim.set_text('Время:')
tim.draw(0, 0)
tm = Label(150, 16, 80, 20, (200, 255, 255))
pobeda = Label(0, 0, 500, 500, (200, 255, 200))
lose = Label(0, 0, 500, 500, (250, 128, 114))
lose.set_color((250, 128, 114))
lose.set_text('Время вышло!!!')
pobeda.set_color((200, 255, 200))
pobeda.set_text('Победа!!!')


while True:
    pygame.display.update()
    p = time.time()
    t = p - k
    if q >= 5:
        pobeda.fill()
        pobeda.draw(200, 240)
    elif t >= 10:
        lose.fill()
        lose.draw(200, 240)
    else:
        
        if wait == 0:
            tm.set_text(str(round(t)))
            tm.draw(0, 0)
            l = random.randint(0, 3)
            for elem in spisok:
                elem.fill()
            spisok[l].set_text('CLICK')
            spisok[l].draw(13, 80)
            wait = 40
        else:
            
            wait -= 1
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                n, m = event.pos
                if spisok[l].win(n, m):
                    spisok[l].set_color((0, 255, 51))
                    spisok[l].fill()
                    spisok[l].set_color((255, 255, 0))
                    q += 1
                    stat.set_text(str(q))
                    stat.draw(0, 0)

                else:
                    q -= 1
                    stat.set_text(str(q))
                    stat.draw(0, 0)
                    for elem in spisok:
                        if elem.win(n, m):
                            elem.set_color((255, 0, 0))
                            elem.fill()
                            elem.set_color((255, 255, 0))
                            break
    
    clock.tick(100)
