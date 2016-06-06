# implementation of card game - Memory
#implemented by Prajakta Gujarathi, June 4th 2016
import simplegui
import random

# helper function to initialize globals
def new_game():
    global state,exposed,cards,pos1,pos2,moves
    state = 0
    pos1 = 16
    pos2 = 16
    moves = 0
    cards = range(8)+range(8)
    random.shuffle(cards)
    exposed = [0]*16
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, pos1, pos2,moves
    
    if state == 0:
        pos1 = pos[0]//50
        exposed[pos1] = 1
        state = 1
    elif state == 1:
        pos2 = pos[0]//50
        if(pos2 != pos1):
            exposed[pos2] = 1
            moves += 1
            state = 2 
    else:
        if(pos2 != pos1):
            if(cards[pos1] == cards[pos2]):
                exposed[pos1] , exposed[pos2] = 1 ,1
            else:
                exposed[pos1] , exposed[pos2] = 0 ,0
                pos1 , pos2 = -1, -1 
            pos1 = pos[0]//50
            exposed[pos1] = 1
            state = 1    
  
    
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global start_pos_card
    for i in range(16):
        if(exposed[i] == 1):
            canvas.draw_polygon([[i*50,0],[i*50,100],[(i+1)*50,100],[(i+1)*50,0]],1,"white","black")
            canvas.draw_text(str(cards[i]),((i)*50+15, 60), 40, "red")
        elif(exposed[i] == 0):
            canvas.draw_polygon([[i*50,0],[i*50,100],[(i+1)*50,100],[(i+1)*50,0]],1,"white","green")
    label.set_text("Turns = " + str(moves))
    
        

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
