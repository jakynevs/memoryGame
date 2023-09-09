# implementation of card game - Memory

import simplegui
import random

#GLOBALS
CARDS = 16
list1 = list(range(1, (CARDS // 2 + 1)))
list2 = list(range(1, (CARDS // 2 + 1)))
cards = list1 + list2
mos_pos = 0


# helper function to initialize globals
def new_game():
    global state, turns, cards, exposed
    state = 0
    turns = 0
    random.shuffle(cards)
    label.set_text("Turns = " + str(turns))
    exposed = [False for i in range(1 , CARDS+1)]

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, turns, card_index, card_one_index, card_two_index
    
    card_index = pos[0] // 50 
    if exposed[card_index] == False:
        exposed[card_index] = True
        
        if state == 0:
            card_one_index = card_index
            state = 1

        elif state == 1:
            turns += 1
            state = 2
            card_two_index = card_index

        elif state == 2:
            state = 1
            if cards[card_one_index] != cards[card_two_index]:

                exposed[card_one_index] = False
                exposed[card_two_index] = False 

            exposed[card_index] == True

            card_one_index = card_index
    label.set_text("Turns = " + str(turns))
                        
def draw(canvas): 
    global card_index, exposed, pos, mos_pos, CARDS, cards
    
    for i in range(len(exposed)): 
        
        card_pos = i * 50 
        
        if exposed[i] == True:
            
            num_pos = i * 50 + 16        

            canvas.draw_polygon([(card_pos, 0), (card_pos, 100), (card_pos + 50, 100), (card_pos + 50, 0)], 1, 'White', 'Black')
            
            canvas.draw_text(str(cards[i]), (num_pos, 60), 24, 'White')
            
        elif exposed[i] == False:
            canvas.draw_polygon([(card_pos, 0), (card_pos, 100), (card_pos + 50, 100), (card_pos + 50, 0)], 1, 'Black', 'Green')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", (len(cards) * 50), 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
