# type casting 


birth_YEAR = input("enter your birth year : ")
print(type(birth_YEAR))
new_year = int(birth_YEAR)
print(type(new_year))

weight = int(input("how much do u weight : "))
print("your weight in pounds = ")
print(weight)
print("your weight in kg = ")
print(weight/2.2)

# sting types 
str1 = "Hello's everyone!!"
str2 = 'hello "everyoe"'
str3 = '''
        hello 
        how 
        are 
        you 
        '''

print(str1)
print(str2)
print(str3)


# indexing in str
print(str1[0]) 
print(str1[-2]) 
print(str1[0:4])
print(str2[1:-1])


# formatted string
name = "james"
last = "smith"
msg = f"{name} {last}"
print(msg)

# length of string 
print(len(name))
print(name.lower)
print(name.upper)
print(name.find('a'))
