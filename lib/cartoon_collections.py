def roll_call_dwarves(dwarves):
    index = 1
    for name in dwarves:
        print(f'{index}. {name}')
        index += 1

def summon_captain_planet(planeteer_calls):
    return[call.title() + '!' for call in planeteer_calls]

def long_planeteer_calls(call_len):
    for call in call_len:
        if len(call) > 4:
            return True
    
    return False

def find_the_cheese(str_foods):
    cheese = ["cheddar", "gouda", "camembert"]
    for food in str_foods:
        if food in cheese:
            return food 
    
    return None
