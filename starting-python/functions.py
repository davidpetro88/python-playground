def call_numbers():
    for number in range(0,5):
        print(number)

def call_numbers_with_limit(limit):
    list = range(0,10)
    for number in range(limit):
        print(number)

def calculator(x=10, y=15):
    return x-y

print("call_numbers")
call_numbers();

print("call_numbers_with_limit")
call_numbers_with_limit(2)

print("Result is calculator", calculator(5))
print("Result is calculator", calculator(30))