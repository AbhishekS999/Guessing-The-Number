import random
import time


f_open = open("high_score_easy.txt", "a+")
f_open.close()
f_open = open("high_score_medium.txt", "a+")
f_open.close()
f_open = open("high_score_hard.txt", "a+")
f_open.close()


def levels():
    global lvl
    print("Enter your difficulty level:\n1-Easy\n2-Medium\n3-Hard")
    lvl = int(input("Enter your choice:"))
    if lvl == 1:
        guess(10)
    elif lvl == 2:
        guess(100)
    elif lvl == 3:
        guess(1000)
    else:
        print("Invalid Option!!!\n\n")
    time.sleep(1)
    menu()


def guess(x):
    score = 100
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        print(f"Current Score: {score}")
        score -= 5

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

    if lvl == 1:
        f1 = open("high_score_easy.txt", "r")
        scr = f1.read()
        if scr == "":
            scr = 0
        f1.close()
        if int(scr) < (score + 5):
            f = open("high_score_easy.txt", "w")
            f.write(f"{score + 5}")
            f.close()
    elif lvl == 2:
        f1 = open("high_score_medium.txt", "r")
        scr = f1.read()
        if scr == "":
            scr = 0
        f1.close()
        if int(scr) < (score + 5):
            f = open("high_score_medium.txt", "w")
            f.write(f"{score + 5}")
            f.close()
    else:
        f1 = open("high_score_hard.txt", "r")
        scr = f1.read()
        if scr == "":
            scr = 0
        f1.close()
        if int(scr) < (score + 5):
            f = open("high_score_hard.txt", "w")
            f.write(f"{score + 5}")
            f.close()

    time.sleep(1)
    menu()


def menu():
    print("Welcome to Guessing the number game!!!\n1- Play\n2- High Scores\n3- Exit\n")
    choice = int(input("Enter your Choice:"))
    if choice == 1:
        play()
    elif choice == 2:
        high_scores()
    elif choice == 3:
        exit()


def high_scores():
    f1 = open("high_score_easy.txt", "r")
    f2 = open("high_score_medium.txt", "r")
    f3 = open("high_score_hard.txt", "r")
    scr1 = f1.read()
    scr2 = f2.read()
    scr3 = f3.read()
    if scr1 == "":
        scr1 = 0
    if scr2 == "":
        scr2 = 0
    if scr3 == "":
        scr3 = 0
    f1.close()
    f2.close()
    f3.close()
    print(f"Easy {scr1}\nMedium {scr2}\nHard {scr3}\n\n")
    time.sleep(0.1)
    menu()


def play():
    levels()


menu()
