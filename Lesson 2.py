print("Welcome to lesson 2")

print ("""1. Typhoon
2. Sunny
3. Snowing
4. METEOR STRIKE""")
weather= input("What is the weather like today?")

if weather == "1":
    location = "inside"
elif weather == "2":
    location = "at the beach"
elif weather == "3":
    location = "on a mountain"
if weather == "4":
    location = "trying to survive getting incinerated"
else:
    print("I do not understand")

food = input("What are you eating?")

activity = input("What are you doing?")

if activity[0] == "t":
    print("TTTHATTS TTTTOTALLY UNTTTTERRIBLE!!")
if activity[-1 == "s"]:
    print("SSSSUPPER GREAT!")


feeling = input("Are you bored?")

if feeling == "no":
    happiness = "very exciting"
elif feeling == "yes":
    happiness = "very sad"
else:
    print("I don't understand, please elaborate")

print(f"Today you are {location} eating {food} doing {activity} which is {happiness}.")