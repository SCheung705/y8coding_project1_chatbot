# your chatbot code here!

name = input("Enter your name!")
print(name, "it's you!", name, "i've been waiting all my life to meet you.")
print(name.upper(), "!", name.upper(), "!!", name.upper(), "!!!!!!!!")

if name == "Ryan":
    print("IT'S RYAN!")
else:
    print("It wasn't Ryan")

siblings = int(input("How many brothers and sisters do you have?"))

if siblings == 0:
    print("You're an only child")
elif siblings > 5:
    print("That's alot of siblings")
elif siblings < 0:
    print()