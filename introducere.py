def check_numbers(a, b):
    if a > b:
        print('First number is greater!')
    elif a < b:
        print('Second number is greater!')
    else:
        print('They are equal')
 
def data_types():
    x=int(2)
    y="MAP"
    print(type(x))
    print(type(y))
 
def tuple_type():
    cars=["Audi","BMW","Dacia"]
    x,y,z = cars
    print(x + " " + y + " " + z)
 
def string_interpolation():
    age = 27
    print(f'My name is Daniel and I\'m {age} years old!')
 
def while_instruction():
    i = 1
    while i<=5 :
        print("while loop #", i)
        i+=1
 
def array_list():
    test_array=[]
    n = int(input("Please input the number of elements: "))
    for i in range (0,n):
        test_array.append(int(input(f'Please input element at position {i}: ')))
    print("Array list: ", test_array)
 
check_numbers(1, 2)
data_types()
tuple_type()
string_interpolation()
while_instruction()
array_list()