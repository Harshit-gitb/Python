# for loop 


# iterate a string
for i in "hello":
    print(i)


# using range funtion 

            # from , t0 , skip by 
for i in range(1 , 10 , 2) : 
    print(i)


# calculate price
cart = [10,20,40,20,30]
total  = 0
for price in cart : 
    total = total + price

print(total)

# nested loops 
x = 0
y= 0 
for x in range(3) :
    for y in range(4):
        print(f"({x},{y})")

lis = [3,4,5,2,3]
for x in lis:
    str = ''
    for y in range(x) :
        str += 'x'
    print(str)

# list 
names = ["a","b","c","d","e"]
print(names[2])
print(names[2:4])


# find largest
number = [1,2,3,4,5,7,4,3,2,5]
larger = number[0]
for i in number :
    if larger < i :
        larger = i

print(larger)



# list methods 
numbers = [1,4,3,5,6,7,3]
number.append(2)  # add an item
number.remove(1)  # remove the item
number.insert(2,5) # insert in between
number.pop() # remove last item
number.index(3) # find index for number
print(3 in number) # find values in list
print(number.count(4)) # count in list
number.sort() # to sort the list assending
number.reverse() # to sort in decending 
number2 = number.copy()

number.remove

# remove duplicates

lis1 = [2,36,3,5,4,23,4,3,2,4,]
lis2 = []
for i in lis1 :
    if i not in lis2 :
        lis2.append(i)


print(lis2)