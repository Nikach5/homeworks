# print("nika chubinidze")

#RAM 

name = "nika" 
        # name: variable-ცვლადი (ვერიებლ), 

        #nika არის ცვლადის მნიშვნელობა(ინგლისურად ეს არის value(ველიუ))

        #   = ტოლობის ნიშნით ხდება ცვლადისთვის მნიშვნელობის მინიჭება (ინგ:  assign (ესაინ))

print(name)

#"ბრჭყალებში თუ არის მოქცეული", ესეიგი მისი ტიპია: str 
#სტრინგი

#განვიხილოთ სხვადასხვა ტიპის ცვლადები

surname = "chubinidze"   #მისი type არის str 
age = 14    #მისი type არის int (integer)
height = 183.5  #მისი type არის float ( ათწილადი )
knows_programming = True #მისი type არის bool (ლოგიკურ)
qriste_agsdga = True 

# age += 3 

# print(age)

# age -= 1 

print(name, "aris", age, "wlis")

print(type(name))
print(type(age))
print(type(height))

#input VS output 
#output (print)
#input (input)

location = input("where do you live? ")

print(name, "lives in", location)

#მომხმარებელს ტერმინალიდან შეაყვანინეთ სახელი, გვარი, ასაკი, სიმაღლე, საცხოვრებელი ლოკაცია და დაპრინტეთ გრძელი წინადადება, რომელიც შეიცავს ყველა ამ მონაცემს

name = input("what is your name?")
print("my name is", name )

surname = input("what is your surname?")
print("my surname is", surname)

age = input("how old are you?")
print("i am", age)

height = input("how tall are you?")
print("i am", height)

location = input("where do you live?")
print("i live in", location)