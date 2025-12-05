# Dictioneries  (look like json in js) 


customer = {
    "name": "John Doe",
    "age": 30,
    "is_verified": True  
}
print(customer["name"])
# print(customer["date_of_birth"])  # This will raise a KeyError since the key doesn't exist
print(customer.get("date_of_birth"))  # This will return None since the key doesn't exist
print(customer.get("date_of_birth","29"))  # This will return "29" since the key doesn't exist

customer["name"] = "Jane Smith"  # Update existing key
print(customer["name"]) 
customer["date_of_birth"] = "1993-01-15"  # Add new key-value pair
print(customer)  








# Exercise
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
  output  += digits_mapping.get(ch,"!") + " "
print(output)

message = input(">")
words = message.split(" ")
imojis = {
    ":)": "😊",
    ":(": "😞",
    "happy": "😄",
    "sad": "😢",
    "love": "❤️"
}
output = ""
for word in words:
    output += imojis.get(word,word) + " "
    
print(output)
