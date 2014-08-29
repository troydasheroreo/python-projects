import random

answer = [
    'Signs point to yes.',
    'Yes.',
    'Reply hazy, try again.',
    'Without a doubt.',
    'My sources say no.',
    'As I see it, yes.',
    'You may rely on it.',
    'Concentrate and ask again.',
    'Outlook not so good.',
    'It is decidedly so.',
    'Better not tell you now.',
    'Very doubtful.',
    'Yes - definitely.',
    'It is certain.',
    'Cannot predict now.',
    'Most likely.',
    'Ask again later.',
    'My reply is no.',
    'Outlook good.',
    'Don\'t count on it.',
    ]

while True:
    
    question = input ("What is your question?").strip().lower()
    if question == "what is the meaning of life":
        print("The magic 8-Ball does not answer questions of that nature.")
        break
    elif question == "who are you":
        print("I'm the Doctor")
        break
    else:
        answers = random.choice(answer)
        print(answers)
        

