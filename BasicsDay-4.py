# # while loops
# i = 3
# while i>0:
#     print("*" * i)
#     i = i-1 
# print("DONE")    

# # GUESSING GAME
# count = 0
# n = 6

# while count < 3 :
#     guess_number = int(input("Guess the right number : "))
#     if n != guess_number :
#         print("wrong guess")
#         count += 1        
#     else : 
#         print("you guessed it right!! Congratulation")
#         break

# else : 
#     print(f"cant try more than {count} times")


start = "start"
stop = "stop"
quit = "quit"
com = ""
old_cmd =""
while com != quit : 
    com = input("Enter command for car")
    if com == start :
            print("car started")
    elif com == stop :
            print("car stopper")
    elif com == quit:
            break

