from cmath import log
from itertools import count
from usecase import logo_
import os
welcome_message = "Hello, welcome to Cafe London!"
product_list = [" Americano Expresso", "Ginger chai Tea", "Regular Latte", "Caramel Latte", "Orange, papaya and manago smoothie", "Elder tree and apple juice"]
main_menu_message='press [0] to exit app, press [1] for product menu '
product_menu_message="[0] to return to main menu,\n[1] to show product menu,\n[2] to create a new product,\n[3] update existing product,\n[4] delete a product\n"


print(logo_)
print(welcome_message)
print(main_menu_message)


def main_menu():
    user_input_main_menu = int(input())
    if user_input_main_menu==0:
        print("Exit the app \n")
        with open('source/mini-project.txt', 'w') as file:
            for product in product_list:
                file.write(product)
        # file.writelines(product_list)
        exit()
    else: 
        product_menu()


def product_menu():
    while True:
        user_options = int(input(product_menu_message))
        if user_options == 0:
            print("Return to main menu.\n")
            print(main_menu_message)
            main_menu()
            
        elif user_options == 1:
            os.system('cls')
           
            print(product_list)
        elif user_options==2:
            print('create new product\n')
            1
            product_list.append(input('enter your new product here\n'))
            print(product_list)
            os.system('cls')
        
        elif user_options==3:
            for count,value in enumerate(product_list):
                print (count,value)
            choice1=int(input('what product do you want to change '))
            choice2=input('what do you want to add ')
            product_list[choice1]=choice2
            os.system('cls')
        elif user_options ==4:
            for count,value in enumerate(product_list):
                print(count, value)
                remove_item = int(input("what item number would you like to remove? "))
                return product_list[remove_item]
            os.system('cls')

main_menu()


