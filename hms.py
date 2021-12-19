
# Project - Health Management System

import datetime


def current_time(current__time):
    return current__time


print("Tell us do you want to Retrieve data or Write data in file.")
retrieve_or_write = int(input("Retrieve(1) or Write(2): "))

if retrieve_or_write == 1:
    print("""Clients
        1 - Salman
        2 - Saad
        3 - Hashir
        """)
    client = int(input("Client no: "))

    if client == 1:
        exe_or_eat = int(input("Exercise(1) or Eaten(2): "))

        if exe_or_eat == 1:
            with open("salman-exercise.txt", "r") as salman_exercise:
                print(salman_exercise.read())

        elif exe_or_eat == 2:
            with open("salman-diet.txt", "r") as salman_diet:
                print(salman_diet.read())

    if client == 2:
        exe_or_eat = int(input("Exercise(1) or Eaten(2): "))

        if exe_or_eat == 1:
            with open("saad-exercise.txt", "r") as saad_exercise:
                print(saad_exercise.read())

        elif exe_or_eat == 2:
            with open("saad-diet.txt", "r") as saad_diet:
                print(saad_diet.read())

    if client == 3:
        exe_or_eat = int(input("Exercise(1) or Eaten(2): "))

        if exe_or_eat == 1:
            with open("hashir-exercise.txt", "r") as hashir_exercise:
                print(hashir_exercise.read())

        elif exe_or_eat == 2:
            with open("hashir-diet.txt", "r") as hashir_diet:
                print(hashir_diet.read())


if retrieve_or_write == 2:
    print("""Clients
    1 - Salman
    2 - Saad
    3 - Hashir
    """)
    client = int(input("Client no: "))

    if client == 1:
        exe_or_eat = int(input("Exercise(1) or Eaten(2): "))

        if exe_or_eat == 1:
            exercise = input("What exercise have you done? ")

            with open("salman-exercise.txt", "w") as salman_exercise:
                salman_exercise.write(f"[{current_time(datetime.datetime.now())}] - {exercise}\n")

        elif exe_or_eat == 2:
            eaten = input("What have you eaten? ")

            with open("salman-diet.txt", "w") as salman_diet:
                salman_diet.write(f"[{current_time(datetime.datetime.now())}] - {eaten}\n")

    elif client == 2:
        exe_or_eat = int(input("Exercise(1) or Eaten(2): "))

        if exe_or_eat == 1:
            exercise = input("What exercise have you done? ")

            with open("saad-exercise.txt", "w") as saad_exercise:
                saad_exercise.write(f"[{current_time(datetime.datetime.now())}] - {exercise}\n")

        elif exe_or_eat == 2:
            eaten = input("What have you eaten? ")

            with open("saad-diet.txt", "w") as saad_diet:
                saad_diet.write(f"[{current_time(datetime.datetime.now())}] - {eaten}\n")

    elif client == 3:
        exe_or_eat = int(input("Exercise(1) or Eaten(2): "))

        if exe_or_eat == 1:
            exercise = input("What exercise have you done? ")

            with open("hashir-exercise.txt", "w") as hashir_exercise:
                hashir_exercise.write(f"[{current_time(datetime.datetime.now())}] - {exercise}\n")

        elif exe_or_eat == 2:
            eaten = input("What have you eaten? ")

            with open("hashir-diet.txt", "w") as hashir_diet:
                hashir_diet.write(f"[{current_time(datetime.datetime.now())}] - {eaten}\n")

    else:
        print("Sorry! Client not found")
