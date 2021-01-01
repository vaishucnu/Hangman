import pygame
import math
import os
import random
#window setup
pygame.init()
pygame.display.set_caption("Hangman")
window = pygame.display.set_mode((750,500))

#buttom variables

radius  = 20
gap = 15
letter = []
startx = round((380-(radius*2+gap)*13/2))
starty = 400
A = 65

for i in range(26):
    x = startx + gap *2 + ((radius *2 +gap ) *(i%13))
    y = starty + ((i//13)*(gap+radius*2))
    letter.append([x,y,chr(A+i),True])


#fonts

font = pygame.font.SysFont('comiscans', 40)
word_font = pygame.font.SysFont('comiscans', 60)


#load image

image = []
for i in range(7):
    load_image = pygame.image.load(os.path.join("C:/Users/srinivasan/Desktop/project","hangman"+str(i)+".png"))
    #print(load_image)
    image.append(load_image)
print(image)
   
#
    

# hangman status

h_status = 0
words = ["HELLO","DEVELOPER","PYTHON"]
word = random.choice(words)
guessed = []





#setup loop

clock = pygame.time.Clock()
run = True 


def draw():
    window.fill((69,24,70))
    #draw title
    
    
    #draw word
    display_word = ""
    for l in word:
        if l in guessed:
            display_word +=l +" "
        else:
            display_word += "_"
    text = word_font.render(display_word, 1, (255,255,255))
    window.blit(text,(400,200))
    
    #draw button
    
    for l in letter:
        x,y,let,visible = l
        if visible :
            
            pygame.draw.circle(window,(255,255,255),(x,y),radius,3)
            text = font.render(let, 1, (255,255,255))
            window.blit(text, (x-text.get_width()/2,y-text.get_height()/2))
    window.blit(image[h_status],(150,100))
    pygame.display.update()
    


while run:
    clock.tick(60)
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x,m_y = pygame.mouse.get_pos()
            for l in letter:
                x,y,let,visible = l
                if visible:
                    dis = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                    if dis < radius:
                        #print(let)
                        l[3] = False
                        guessed.append(let)
                        if let not in word:
                            h_status +=1
    draw()
                            
    won = True 
    for l in word:
        if l not in guessed:
            won = False
            break  
    if won:
        pygame.time.delay(500) 
        window.fill((0,0,0))
        text = word_font.render("YOU WON!",1,(255,255,255))
        window.blit(text,(380-text.get_width()/2,300-text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break
    if h_status==6 :
        pygame.time.delay(500) 
        window.fill((0,0,0))
        text = word_font.render("YOU LOST!",1,(255,255,255))
        window.blit(text,(380-text.get_width()/2,300-text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000) 
        break
        
        
pygame.quit()
    

