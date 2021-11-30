import pygame
import random
import time

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LAVENDER = (230, 230, 250)
L_BLUE = (61, 165, 255)
# ---------------------------------------------
# User Defined Functions

def prettyText(word):
    wrd = ''
    for c in word:
        wrd += c+' '
        
    return wrd

def cow_bull(guess,word):
    c,b = 0,0
    for i in range(0,4):
        for j in range(0,4):
            if(word[i] == guess[j] and i==j):
                b = b + 1
            elif(word[i] == guess[j] and i!=j):
                c = c + 1
    return c,b

def startScreen(screen):
    screen.blit(play_image, [263, 95])

# ---------------------------------------------

class Game():
    def __init__(self):
        self.guessed_words = []
        self.words = []
        self.word = ''
        self.parseWords()
        self.setWord()
    
    def parseWords(self):
        with open("words_cb.txt") as words_lst:
            self.words = [w.upper() for w in words_lst.read().split(',')]
            
    def setWord(self):
        self.word = str(self.words[random.randint(0,len(self.words))].upper())
        
    def update_guess_list(self, word):
        self.guessed_words.append(word)
        
    def get_guessed_words(self):
        return self.guessed_words
    
    def checkGuessWord(self, guess):
        return self.word.upper() == guess.upper()

    
#----------------------------------------------
VALID_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class TextBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.text = ""
        self.word = ""
        self.font = pygame.font.SysFont('Calibri', 45, True, False)
        self.image = self.font.render("_ _ _ _".upper(), False, RED)
        self.rect = self.image.get_rect()
        
    def add_chr(self, char):
        if len(self.word) >= 4:
            pass
        elif char in VALID_CHARS:
            #self.text += char.upper() + ' '
            self.word += char.upper()
            self.update_text()
        else:
            pass
        self.update()
        
    def update(self):
        old_rect_pos = self.rect.center
        self.image = self.font.render(self.text, False, RED)
        self.rect = self.image.get_rect()
        self.rect.center = old_rect_pos
        
    def update_text(self):
        self.text = ''
        for c in self.word:
            self.text += c + ' '

        while len(self.text) < 8:
            self.text += '_ '
            

player = Game()            

clock = pygame.time.Clock()
screen = pygame.display.set_mode([626, 626])
textBox = TextBox()
textBox.rect.center = [125, 30]
background_image = pygame.image.load("bull-cow.jpg").convert()
play_image = pygame.image.load("play_e_r.png").convert()
done = False

count = 1
text_y = 30
font1 = pygame.font.SysFont('Calibri', 45, True, False)
font2 = pygame.font.SysFont('Calibri', 20, True, False)
font3 = pygame.font.SysFont('Calibri', 55, True, False)

error = False
win = False
start_screen = True
lost = False

c, b = 0, 0
#print(player.word)
while not done:
        # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYUP:
            if not start_screen:
                textBox.add_chr(pygame.key.name(event.key))
                if event.key == pygame.K_BACKSPACE:
                    textBox.word = textBox.word[:-1]
                    textBox.update_text()
                    textBox.update()

                elif event.key == pygame.K_RETURN:
                    if len(textBox.word) == 4:
                        if textBox.word not in player.words:
                            textBox.word = ''
                            textBox.update_text()
                            textBox.update()
                            error = True
                            #time.sleep(3)

                        elif not player.checkGuessWord(textBox.word):
                            error = False
                            c,b = cow_bull(textBox.word.upper(),player.word.upper())
                            player.update_guess_list((count, textBox.word, c, b, text_y - 22))
                            textBox.word = ''
                            textBox.update_text()
                            textBox.update()
                            count += 1
                            if count > 10:
                                lost = True
                            text_y += 40

                        else:
                            win = True
                    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button: ({},{})".format(x,y))
            if x >= 263 and x <= 363:
                if y >= 95 and y <= 135:
                    start_screen = False
            
 
    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    #print(x,y)
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    #screen.fill(L_BLUE)
    screen.blit(background_image, [0, 0])
 
    # --- Drawing code should go here
    lst = player.get_guessed_words()
    if len(lst) > 0:
        for item in lst:
            string1 = "{0:02}. {1}".format(item[0],prettyText(item[1]))
            string2 = "{}C {}B".format(item[2],item[3])
            image_text1 = font1.render(string1, True, RED)
            image_text2 = font1.render(string2, True, RED)
            screen.blit(image_text1, [5, item[4]])
            screen.blit(image_text2, [250, item[4]])
            
    if start_screen:
        startScreen(screen)
        
    else:    
        if win:
            win1 = font3.render("You Won!",True,RED)
            screen.blit(win1, [5, text_y + 25])
            
        elif lost:
            loose1 = font3.render("You Lost!",True,RED)
            screen.blit(loose1, [5, text_y + 25])

        elif error:
            error1 = font2.render("Please Enter a Word from the Dictionary without repeating letters!",True,RED)
            screen.blit(error1, [5, text_y + 25])
            
        if not lost:     
            str_count = "{0:02}".format(count)
            try_count = font1.render(str_count+".",True,RED)
            screen.blit(try_count, [5, text_y - 22])

            textBox.rect.center = [140, text_y]
            screen.blit(textBox.image, textBox.rect)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
 # Close the window and quit.
pygame.quit()
#print(player.get_guessed_words())
print(player.word)