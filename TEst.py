def welcome():
    print("Welcome!")

#--------------------------
def hello(name='John'):
        print("Hello {}".format(name))

#-----------------------------
def ask_name():
    name = input("What is your name? ").strip().title()
    return name
#------------------------------
def area_of_circle(radius):
    import math
    area = math.pi * (radius ** 2)
    return area
##################################

welcome()
hello('Troy')
hello()
name = ask_name()
area = area_of_circle(4)
print(area)
