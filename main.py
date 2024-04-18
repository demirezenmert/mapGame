from turtle import Turtle, Screen
import pandas

turtle= Turtle()
screen= Screen()
image= 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data= pandas.read_csv('50_states.csv')
all_states= data.state.to_list()
guessed_states=[]
while len(guessed_states)<50:
    answer_state= screen.textinput(f'{len(guessed_states)}/50 states correct', "What's another state's name?").title()

    if answer_state == 'Exit':
        missing_states= [item for item in all_states if item not in guessed_states]

        # for state in all_states:    
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data= pandas.DataFrame(missing_states)
        new_data.to_csv('Missing_states.csv')
        print(missing_states)
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t= Turtle()
        t.penup()
        t.hideturtle()
        state_data= data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())




screen.exitonclick()