
# Health Managment System

# Challange by CodeWithHarry

"""
About:
Date: 30/05/2021
Author: Salman Bilal
https://twitter.com/salmanb34055398
"""

import datetime

# ----------------------------------------Let's Try-----------------------------------------------------

print("""
Clients
1 - Salman
2 - Saad
3 - Hashir
""")

def hms(our_clients):

    try:

        if(our_clients==1):

            print("Salman\'s Diet or Exercise")
            
            print("1 - Diet and 2 - Exercise")
            
            diet_or_ex = int(input("Diet or Exercise: "))
        
            if(diet_or_ex==1):
            
                with open("salman-diet.txt", "a") as salman_diet:
            
                    writing_in_salman_diet = input("What have you eatan: ")
            
                    salman_diet.write(f"[{datetime.datetime.now()}] - {writing_in_salman_diet}\n")

            elif(diet_or_ex==2):
            
                with open("salman-exercise.txt", "a") as salman_exercise:
            
                    writing_in_salman_exercise = input("What Exercise have you done: ")              
            
                    salman_exercise.write(f"[{datetime.datetime.now()}] - {writing_in_salman_exercise}\n")

            else:
            
                print("What's this")

        elif(our_clients==2):

            print("Saad\'s Diet or Exercise")
            
            print("1 - Diet and 2 - Exercise")
            
            diet_or_ex = int(input("Diet or Exercise: "))

            if(diet_or_ex==1):
            
                with open("saad-diet.txt", "a") as saad_diet:
            
                    writing_in_saad_diet = input("What have you eatan: ")
            
                    saad_diet.write(f"[{datetime.datetime.now()}] - {writing_in_saad_diet}\n")

            elif(diet_or_ex==2):
            
                with open("saad-exercise.txt", "a") as saad_exercise:
            
                    writing_in_saad_exercise = input("What Exercise have you done: ")
            
                    saad_exercise.write(f"[{datetime.datetime.now()}] - {writing_in_saad_exercise}\n")

            else:
            
                print("What's this")

        elif(our_clients==3):

            print("Hashir\'s Diet or Exercise")

            print("1 - Diet and 2 - Exercise")

            diet_or_ex = int(input("Diet or Exercise: "))
        
            if(diet_or_ex==1):

                with open("hashir-diet.txt", "a") as hashir_diet:

                    writing_in_hashir_diet = input("What have you eatan: ")

                    hashir_diet.write(f"[{datetime.datetime.now()}] - {writing_in_hashir_diet}\n")

            elif(diet_or_ex==2):

                with open("hashir-exercise.txt", "a") as hashir_exercise:

                    writing_in_hashir_exercise = input("What Exercise have you done: ")

                    hashir_exercise.write(f"[{datetime.datetime.now()}] - {writing_in_hashir_exercise}\n")

            else:

                print("What's this")

        else:

            print("No Client found.")

    except Exception as err:

        print(err)

    if __name__ == '__main__':
        pass
    print("Successfully Written")


hms(int(input("Client No: ")))

# ----------------------------------------Succeeded------------------------------------------------------
