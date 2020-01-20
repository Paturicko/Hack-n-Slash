'''
    -- Age Test --

    name = input("What is your name?")
    age = int(input("How old are you?"))
    days = age*365
    hours = days*24
    minutes = hours*60
    seconds = minutes*60

    print(name, age, days, "days old", hours, "hours old", minutes, "minutes old", seconds, "seconds old")

    -- How Many Fingers --
'''
fingers = int(input("How many fingers am I holding up?"))

print(fingers)

if fingers == 0:
    print("Correct, I don't have fingers")
else:
    print("Wrong, I have no fingers")





