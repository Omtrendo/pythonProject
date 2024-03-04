def make_pizza(*toppings):
    """Скласти список замовлених інгредієнтів"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green pappers', 'extra cheese')

#
def make_pizza(size, *toppings):
    """Описати піццу, яку ми збираємось приготувати"""
    print(f"\nMaking a {size} - inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16,'pepperoni')
make_pizza(12, 'mushrooms', 'green pappers', 'extra cheese')
#
def build_profile(first, last, **user_info):
    """Створити словник, який міститиме всю інформацію про користувача"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein',
                             location= 'princeton', field= 'physics')
print(user_profile)

#do_it_yourself бутерброд
def sandwich(*ingredients):
    print(f"Your sandwich with {ingredients} is ready. Please take it.")

sandwich('butter')
sandwich('cheese', 'mushrooms')
sandwich('souse', 'onion', 'meat')

#my_profile
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('alla', 'shykhova',
                             location= 'lviv', language= 'python',
                             age = '26')
print(user_profile)

#car profile
def car_profile(firm_name, model_name, **additional_characteristics):
    return additional_characteristics

car_profile1 = car_profile('range rover', 'discovery', transmission='manual', color='white')
car_profile2 = car_profile('Jaguar', 'I-Pace', speed='200', type='electric')
car_profile3 = car_profile('Lexus', 'LX', type='outlander', platform='4x4')

print(car_profile1)
print(car_profile2)
print(car_profile3)