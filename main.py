from pygame import *
import pygame
import sys
import creds
init()
SIZE = (800, 500)
screen = display.set_mode(SIZE)
screenrect = (0,0,800,500)
#-----COLORS-----
GREEN = (0,255,0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
YELLOW = (255,193,37)
moodyBlue = (28,134,238)
lightMoodyBlue = (0,178,238)
cornBlue = (0,154,205)
darkPink = (205,16,118)
BEIGE = (245, 245, 220)
#-----FONTS-----
myFont = font.SysFont('Times New Roman', 30)
font = font.SysFont("Times New Roman",20)
#-----FUNCTIONS-----
def xCenteredText(string, size, rect, color, y):
  font = pygame.font.SysFont("Times New Roman",size)
  textWidth, textHeight = font.size(string)
  centerx = (rect[2] - textWidth)//2
  centery = (rect[3] - textHeight)//2
  text = font.render(string, 1, color)
  screen.blit(text, [centerx,y])

def centertext(string, size, rect):
  font = pygame.font.SysFont("Times New Roman",size)
  textWidth, textHeight = font.size(string)
  offX = rect[0] + (rect[2] - textWidth)//2
  offY = rect[1] + (rect[3] - textHeight)//2
  textRect = pygame.Rect(offX, offY, textWidth, textHeight)
  text = font.render(string , 1, (0, 0, 0))
  screen.blit(text, textRect)
 
def drawtext(string, size, rect, color, x, y):
  font = pygame.font.SysFont("Times New Roman", size)
  textWidth, textHeight = font.size(string)
  textRect = Rect(x, y, textWidth, textHeight)
  text = font.render(string , 1, color)
  screen.blit(text, textRect)
#def key():  
  # while True:
  #     for event in event.get():
  #         if event.type == QUIT:
  #           quit()
  #           sys.exit()
  #         elif event.type == KEYDOWN:
  #             if event.unicode.isalpha() or event.unicode.isdigit():
  #                 input_text = event.unicode
  #                 return input_text
  #             elif event.key == K_BACKSPACE:
  #                 input_text = input_text[:-1]
  #                 return "delete"
  #             elif event.key == K_RETURN:
  #                 input_text = input_text[:-1]
  #                 return "enter"
               
def searchBar(mx, my, button, currentState):
  search_rect = pygame.Rect(50, 25, 400, 50)
  search_font = pygame.font.Font(None, 36)
  pygame.draw.rect(window, (0, 0, 0), search_rect, 2)  
def homescreen(mx, my, button, currentState):
  screen.fill(WHITE)
  #title
  xCenteredText('Google translate', 50, screenrect, (0,0,0), 50)
  draw.line(screen, BLACK, (180, 80), (370, 80), 5)
  drawtext('Hackathon', 40, screenrect, BLUE, 180, 20)
  #the box for the inputs
  nounBox = Rect(225, 225, 100, 50)
  draw.rect(screen, BLACK, nounBox, 3)
  verbBox = Rect(375, 225, 100, 50)
  draw.rect(screen, BLACK, verbBox, 3)
  centertext('Noun', 30, nounBox)
  centertext('Verb', 30, verbBox)
  if nounBox.collidepoint(mx, my) == True:
    draw.rect(screen, YELLOW, nounBox)
    draw.rect(screen, BLACK, nounBox, 3)
    centertext('Noun', 30, nounBox)
    if button == 1:
      currentState = STATE_NOUN
  if verbBox.collidepoint(mx, my) == True:
    draw.rect(screen, YELLOW, verbBox)
    draw.rect(screen, BLACK, verbBox, 3)
    centertext('Verb', 30, verbBox)
    if button == 1:
      currentState = STATE_VERB
  return currentState

# search screen function
def backButton(mx, my, button):
    draw.rect(screen, BLACK, (10, 10, 106, 46))
    draw.rect(screen, WHITE, (13, 13, 100, 40))
    draw.rect(screen, BLACK, (43, 25, 58, 14))
    draw.polygon(screen, BLACK, ((23, 32), (43, 16), (43, 49)))
    area = Rect(10, 10, 106, 46)
    if area.collidepoint(mx, my) == True:
        draw.rect(screen, BLACK, (10, 10, 106, 46))
        draw.rect(screen, YELLOW, (13, 13, 100, 40))
        draw.rect(screen, BLACK, (43, 25, 58, 14))
        draw.polygon(screen, BLACK, ((23, 32), (43, 16), (43, 49)))
        if button == 1:
          return True
    return False
 
def nounscreen(mx, my, button, currentState, word, enterstate, key):
  screen.fill(WHITE)
  searchBox = Rect(200, 200, 300, 50)
  draw.rect(screen, BLACK, searchBox, 3)
  # if searchBox.colliderect(mx, my) == True:
  #   enterstate = True
  if searchBox.collidepoint(mx, my) == True:
    enterstate = True
  if enterstate == True:
    word =+ key
    print(word)
  if backButton(mx, my, button) == True:
    currentState = STATE_MAIN
  return currentState
def verbscreen(mx, my, button, currentState):
  screen.fill(WHITE)
  if backButton(mx, my, button) == True:
    currentState = STATE_MAIN
  return currentState

#-----STATES-----
STATE_MAIN = 0
STATE_EXIT = 1
STATE_NOUN = 2
STATE_VERB = 3

#-----SETUP-----
running = True
myClock = time.Clock()
currentState = STATE_MAIN
mx = my = button = 0
enterstate = False
word = ''
#-----RUN LOOP-----
while running:
  for evnt in event.get():
    if evnt.type == QUIT:
      running = False
    if evnt.type == MOUSEBUTTONDOWN:
      mx, my = evnt.pos
      button = evnt.button
    if evnt.type == MOUSEMOTION:
      mx, my = evnt.pos
    if evnt.type == KEYDOWN:
      key = evnt.unicode

    if currentState == STATE_MAIN:
      currentState = homescreen(mx, my, button, currentState)
    elif currentState == STATE_NOUN:
      currentState = nounscreen(mx, my, button, currentState, word, enterstate, key)
    elif currentState == STATE_VERB:
      currentState = verbscreen(mx, my, button, currentState, word, enterstate, key)
    button = 0
    # waits long enough to have 60 fps
  display.flip()
  myClock.tick(60)