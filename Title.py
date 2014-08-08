def ask(question):
    answer = input(question).strip().lower()
    print("You answered: " + answer)
    return answer

def ask_color():
    return ask("What is your favorite color?")

def die():
    print("Thou art cast into the Gorge of Eternal Peril")
    print("You are dead")

def live():
    print("Fine. Off you go then")

def run():
    name = ask("What is your name?")
    if name == 'lancelot':
            color = ask_color
            if color == 'blue':
                live()
            else:
                die()
            
    elif name == 'robin':
        capital = ask("What is the capital of Assyria?")

    elif name == 'galahad':
        color = ask_color

    elif name == 'arthur':
        answer = ask("What is the air speed velocity of an unlaiden swallow?")

    else:
        color = ask_color

#######################################
run()
