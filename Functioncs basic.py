def greet_user():
    print('Welcome')
greet_user()
#Welcome

def greet_user(username):
    print(f'Welcome {username.title()}')
greet_user('tom')
#Welcome Tom

def favorite_book(book):
    print(f'{book.title()}, is my favorite')
favorite_book('mindfuck')
#Mindfuck, is my favorite

def describe_pet(animal_type, pet_name):
    print(f'My animal is a {animal_type}')
    print(f'His name is {pet_name.title()}')
describe_pet('cat', 'rollo')
#My animal is a cat
#His name is Rollo

def catering_menu(name, type, kcal_value, adress):
    print(f'{name.title()}, ordered {type}, with the kcal value of {kcal_value}. Delivery adress is {adress.title()}')
catering_menu('tom', 'vegetarian', 1500, 'kastetvej 82, 4th')
#Tom, ordered vegetarian, with the kcal value of 1500. Delivery adress is Kastetvej 82, 4Th

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count 

    sorted_numbers = sorted (numbers)
    middle = count // 2
    if count %2 == 0:
        lower = sorted_numbers[middle -1]
        upper = sorted_numbers[middle]
        median = (lower+ upper) / 2
    else:
        median = sorted_numbers[middle]

    return minimum, maximum, average, median, count 
lenghts = [63, 56, 43, 78, 98, 35, 38, 76, 29]

minimum, maxiumum, average, median, count = get_stats(lenghts)
print(f' Minimum: {minimum}, Maximum: {maxiumum}, Avg: {average}, Median: {median}, Count: {count}')
#Minimum: 29, Maximum: 98, Avg: 57.333333333333336, Median: 56, Count: 9

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print('\n Please write your name and surname')
    print('(Press "q" to quit)')

    f_name = input("Name")
    if f_name == 'q':
        break
    f_last = input("Surname")
    if f_last == 'q':
        break
    formatted_name = get_formatted_name(f_name, f_last)
    print(f'\nWelcom, {formatted_name}')


