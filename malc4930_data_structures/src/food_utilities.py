"""
-------------------------------------------------------
food_utilities.py
Utilities for working with a Food object.
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2017-08-19"
-------------------------------------------------------
"""
from food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Postconditions:
        returns
        food - a completed food object (Food).
    -------------------------------------------------------
    """
    name = input("Name: ")
    print(Food.origins())
    origin = int(input(": "))
    vegetarian = input("Vegetarian(Y/N): ")
    
    if vegetarian == "Y":
        vegetarian = True
    else:
        vegetarian = False
        
    calories = int(input("Calories: "))
    
    food = Food(name,origin,vegetarian,calories)
    
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Preconditions:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Postconditions:
        returns
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    l = line.split("|")
    name = l[0]
    origin = int(l[1])
    vegetarian = l[2]
    if vegetarian == "True":
        vegetarian = True
    else:
        vegetarian = False
    calories = int(l[3])
    
    food = Food(name, origin, vegetarian, calories)
    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_food(file_variable)
    -------------------------------------------------------
    Preconditions:
        file_variable - an already open input file of food data (file)
    Postconditions:
        returns
        foods - a list of food objects (list of food)
    -------------------------------------------------------
    """
    foods = []
    for line in file_variable:
        foods.append(read_food(line))
    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Preconditions:
        file_variable - an already open output file of food data (file)
        foods - a list of Food objects (list of Food)
    Postconditions:
        file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    -------------------------------------------------------
    """
    for i in foods:
        i.write(file_variable)
    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
    Postconditions:
        returns
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    veggies = []
    for i in foods:
        if i.is_vegetarian == True:
            veggies.append(i)
    return veggies

def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Postconditions:
        returns
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    origins = []
    for i in foods:
        if i.origin == origin:
            origins.append(i)
            
    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
    Postconditions:
        returns
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    num = 0
    total = 0
    for i in foods:
        total += i.calories
        num += 1
    avg = total/num
    return avg
        
def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    Use: calories_by_origin(foods)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Postconditions:
        prints
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    origins= by_origin(foods, origin)
    avg = average_calories(origins)
    return avg
    
def food_table(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    Use: calories_by_origin(foods)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
    Postconditions:
        prints
        a table of the foods sorted by name
    -------------------------------------------------------
    """
    sort = []
    while len(foods) != 0:
        num = 0
        small = foods[0]
        for i in foods:
            if i < small:
                small = i
                num = foods.index(i)
        sort.append(foods.pop(num))
    
    print("Food                                Origin       Vegetarian Calories")
    print("----------------------------------- ------------ ---------- --------")
    for i in sort:
        if i.is_vegetarian == 0 :
            i.is_vegetarian = "False"
        else:
            i.is_vegetarian = "True"
                
        print("{:36}{:18}{:10}{}".format(i.name,Food.ORIGIN[i.origin],i.is_vegetarian, i.calories))

    return

def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    Use: result = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Postconditions:
        returns
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))
    result = []
    if origin == -1:
        new = foods
    else:
        new = by_origin(foods, origin)
    if is_veg == True:
        veg = get_vegetarian(new)
    elif is_veg == False:
        veg = new
    if max_cals == 0:
        result = veg
    else:
        for i in veg:
            if i.calories <= max_cals:
                result.append(i)
                
    return result
