# # if else
# is_yes = True 

# if is_yes:
#     print("you are saying yes")
#     print("thank YOU !!")
# else:
#     print("you are saying no!!")
#     print("say yessssssssssss!!!!!!!!!!")

# num = 20
# if num > 20:
#     print("bigge then 20")
# elif num < 20 :
#     print("smaller then 20")
# else :
#     print("its 20!!")


# housePrice = 1000000
# is_creditGood = 1
# if is_creditGood :
#     print("your credit score is good so u can proceed by 10%")
#     print(f"amount would be {housePrice * 0.1}")
# else : 
#     print(f"u have to start with 20% your amount would be {housePrice * 0.2}")

# # operators 

# # logical operators
# has_card = True 
# has_cash = True

# if has_cash and has_cash :
#     print("you are very rich")
# elif has_cash or has_card : 
#     print("you are rich")
# else : 
#     print("you are poor ")

# if has_card and not has_cash :
#     print("you are still rich but without card")

# # comparison operator

# temp = 30
# if temp > 30 : 
#     print("hot day")
# elif temp < 30 :
#     print("its not so hot")


# # name situation 
# name = input("enter your name : ")
# if len(name) < 4 :
#     print("you name is too short try again !!")
# elif len(name) > 20 :
#     print("who have this long name try again !!")
# else :
#     print("your name will work perfectly fine !! :)")

# weight converter
weight = int(input("enter your weight"))
char = input("what unit to convert in L OR K ")
if char.lower() == "k" : 
    print(f"your wright in kg = {(weight * 0.45)}")
elif char.lower() == "l" :
    print(f"your weight in lbs = {(weight * 2.2)}")
else :
    print("Invalid Unit")   