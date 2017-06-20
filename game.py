import random
#import simplegui
try:
    import simplegui

except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


computer_score=0
human_score=0
human_choice=''
computer_choice=''

def choice_to_number(choice):
    return {'rock':0,'paper':1,'scissor':2}[choice]

def number_to_choice(number):
    return {0:'rock',1:'paper',2:'scissor'}[number]

def random_computer_choice():
    return random.choice(['rock','paper','scissor'])
def choice_result(human_choice,computer_choice):
    global computer_score
    global human_score
    human_number=choice_to_number(human_choice)
    computer_number=choice_to_number(computer_choice)

    if (human_choice-computer_choice)%3 ==1:
        print('computer wins')
        computer_score+=1

    elif human_number==computer_number:
        print('tie')

    else:
        print('human wins')
        human_score+=1

def test_choice_to_number():
    assert choice_to_number('rock')==0
    assert choice_to_number('paper')==1
    assert choice_to_number('scissor')==2

def test_number_to_choice():
    assert number_to_choice(0)=='rock'
    assert number_to_choice(1)=='paper'
    assert number_to_choice(2)=='scissor'

def test_all():
    test_choice_to_number()
    test_number_to_choice()

def rock():
    global human_choice,computer_choice
    global human_score,computer_score
    human_choice='rock'
    computer_choice=random_computer_choice()
    choice_result(human_choice,computer_choice)
    

def paper():
    global human_choice,computer_choice
    global human_score,computer_score
    human_choice='paper'
    computer_choice=random_computer_choice()
    choice_result(human_choice,computer_choice)

def scissor():
    global human_choice,computer_choice
    global human_score,computer_score
    human_choice='scissor'
    computer_choice=random_computer_choice()
    choice_result(human_choice,computer_choice)

def draw(canvas):
    try:
        canvas.draw_text('you:'+human_choice,[10,40],48,'green')
        canvas.draw_text('comp :'+computer_choice,[10,80],48,'red')
        canvas.draw_text('human_score:'+str(human_score),[10,150],30,'green')
        canvas.draw_text('comuter_score:'+str(computer_score),[10,190],30,'red')

    except TypeError:
        pass

def play_rps():
    frame=simplegui.create_frame('home',300,200)
    frame.add_button('rock',rock)
    frame.add_button('paper',paper)
    frame.add_buttom('scisssor',scissor)
    frame.set_draw_handler(draw)

    frame.start()

play_rps()
#print(dir(simplegui))



