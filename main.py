import pygame
from pygame import mixer

pygame.init()

WIDTH = 1400
HEIGHT = 800
black = (0,0,0)
white =(255,255,255)
grey = (128,128,128)
green =(0,255,0)
gold = (212,175,55)
blue = (0,255,255)

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.Font('Roboto-Bold.ttf',32)

fps =60
timer = pygame.time.Clock()
beats = 8
instruments =6
boxes =[]
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
bpm = 120
playing = True
active_length =0
active_beat = 1
beat_changed =True

#load in sounds
hi_hat = mixer.Sound('sounds/hihat-nice.wav')
snare = mixer.Sound('sounds/snare.wav')
kick = mixer.Sound('sounds/kick-nice.wav')
clap = mixer.Sound('sounds/clap03.wav')
note1 = mixer.Sound('sounds/1note.wav')
note2 = mixer.Sound('sounds/2note.wav')

def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat]==1:
            if i ==0:
                hi_hat.play()
            if i ==1:
                kick.play()
            if i == 2:
                snare.play()
            if i == 3:
                note1.play()
            if i == 4:
                note2.play()
            if i == 5:
                clap.play()


def draw_grid(clicks,beat):
    left_box =pygame.draw.rect(screen,grey,[0,0,200,HEIGHT-200],5)
    bottom_box = pygame.draw.rect(screen,grey,[0,HEIGHT-200,WIDTH,200],5)
    boxes =[]
    colors = [grey,white,grey]
    hi_hat_text = label_font.render('hi-hat', True, white)
    screen.blit(hi_hat_text,(30,30))
    kick_text = label_font.render('kick', True, white)
    screen.blit(kick_text, (30, 130))
    snare_text = label_font.render('snare', True, white)
    screen.blit(snare_text, (30, 230))
    note1_text = label_font.render('note1', True, white)
    screen.blit(note1_text, (30, 330))
    note2_text = label_font.render('note2', True, white)
    screen.blit(note2_text, (30, 430))
    clap_text = label_font.render('clap', True, white)
    screen.blit(clap_text, (30, 530))
    for i in range(instruments):
        pygame.draw.line(screen,grey,(0,(i * 100) +100), (200,(i * 100) +100),3)

    for i in range(beats):
        for j in range(instruments):
            if clicks[j][i] ==-1:
                color =grey
            else:
                color = green
            rect = pygame.draw.rect(screen, color,
                                    [i * ((WIDTH - 200) // beats) + 205, (j * 100)+5, ((WIDTH - 200) // beats)-10,
                                     ((HEIGHT - 200) // instruments)-10], 0, 3)
            pygame.draw.rect(screen, gold,
                             [i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200) // beats),
                              ((HEIGHT - 200) // instruments)], 5, 5)
            pygame.draw.rect(screen, black,
                             [i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200) // beats),
                              ((HEIGHT - 200) // instruments)], 2, 5)

            boxes.append((rect,(i,j)))




        active = pygame.draw.rect(screen,blue,[beat*((WIDTH-200) // beats) + 200, 0 , ((WIDTH-200) // beats), instruments*100],5,3)
    return boxes

#sounds



run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked, active_beat)

    if beat_changed:
        play_notes()
        beat_changed =False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
        if event.type ==pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords =boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1

    beat_length= fps * 60 // bpm

    if playing:
        if active_length < beat_length:
            active_length+=1

        else:
            active_length = 0
            if active_beat < beats-1:
                active_beat +=1
                beat_changed =True

            else:
                active_beat = 0
                beat_changed =True




    pygame.display.flip()
pygame.quit()