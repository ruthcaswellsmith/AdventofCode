# DAY 21
# Part 1

# -----------
# Read Input
# -----------
foods = {}

f = open("Day21.txt", "r")

food = 0
line = f.readline()
while line:

    foods[food]={}
    # Process input
    line = line.strip('\n')
    left, right = line.split('(')
    foods[food]['ingredients'] = set(left.split())

    right = right.strip(')')
    right = right.replace('contains ', '')
    right = right.replace(',','')
    foods[food]['allergens'] = set(right.split())

    food += 1
    line = f.readline()

# Close file
f.close()

print(foods)

# -------------
# Process input
# -------------

ingredients = {}
allergens = {}

# Get unique list of ingredients and allergens
for food, dict in foods.items():

    for ingredient in dict['ingredients']:
        if ingredient not in ingredients:
            ingredients[ingredient] = {}

    for allergen in dict['allergens']:
        if allergen not in allergens:
            allergens[allergen] = {}

# Now fill in the dictionary for each ingredient with
# allergens as keys and counts as values
for ingredient, ingredient_dict in ingredients.items():
    for food, food_dict in foods.items():
        if ingredient in food_dict['ingredients']:
            for allergen in food_dict['allergens']:
                if allergen not in ingredient_dict.keys():
                    ingredient_dict[allergen] = 1
                else:  # update the count
                    ingredient_dict[allergen] += 1

print(ingredients)

# Now fill in the dictionary for each allergen with
# ingredients as keys and counts as values
for allergen, allergen_dict in allergens.items():
    for food, food_dict in foods.items():
        if allergen in food_dict['allergens']:
            for ingredient in food_dict['ingredients']:
                if ingredient not in allergen_dict.keys():
                    allergen_dict[ingredient] = 1
                else:  # update the count
                    allergen_dict[ingredient] += 1

print(allergens)

# Now we can loop through the allergens, removing any ingredient
# which did not appear as many times as the maximum for that allergen
# we can then remove that allergen from the associated ingredients

for allergen in list(allergens.keys()):
    max_appearance = max(allergens[allergen].values())
    for ingredient in list(allergens[allergen].keys()):
        if allergens[allergen][ingredient] < max_appearance:
            allergens[allergen].pop(ingredient)
            ingredients[ingredient].pop(allergen)

# We may be done.  Get a list of ingredients which cannot contain allergens
allergen_free = []

for ingredient in ingredients.keys():
    if len(ingredients[ingredient].keys()) == 0:
        allergen_free.append(ingredient)

# Now count how many times these appear in foods
count = 0
for ingredient in allergen_free:
    for food in foods.keys():
        if ingredient in foods[food]['ingredients']:
            count += 1

print('The answer is:', count)

# Part 2
#--------

# ---------
# Functions
# ---------

def not_done_yet():
    """returns True if at least one allergen has more than one ingredient associated with it"""

    for allergen in allergens.keys():
        if len(allergens[allergen].keys()) > 1:
            return True

    return False

def get_known_allergen():
    """returns the first allergen it finds which only has one ingredient associated with it"""

    for allergen in allergens.keys():
        if len(allergens[allergen].keys()) == 1:
            return allergen, list(allergens[allergen].keys())[0]

    return ''

# ----
# Main
# ----

# First let's get rid of all inert ingredients
for ingredient in allergen_free:
    # remove from foods
    for food in list(foods.keys()):
        if ingredient in foods[food]['ingredients']:
            foods[food]['ingredients'].remove(ingredient)

    # remove from ingredients
    ingredients.pop(ingredient)

# Now we loop through as long as each allergen has more than one ingredient listed
final_allergens = []
final_ingredients = []

not_done = True
while not_done:

    # Find an allergen that only has one ingredient
    known_allergen, known_ingredient = get_known_allergen()

    if known_allergen == '':
        print('we are stuck')
        not_done = False

    else:
        # add it to our final set
        final_allergens.append(known_allergen)
        final_ingredients.append(known_ingredient)

        # remove the known ingredient from all other allergens
        for allergen in allergens.keys():
            if allergen != known_allergen:
                allergens[allergen].pop(known_ingredient, 100)

        # remove the allergen itself from allergens because we're done with hit
        allergens.pop(known_allergen)

    not_done = not_done_yet()

# Add remaining allergens and ingredients to the list
for allergen in allergens.keys():

    final_allergens.append(allergen)
    final_ingredients.append(list(allergens[allergen].keys())[0])

# Build our answer
answer = [ingredient for _,ingredient in sorted(zip(final_allergens,final_ingredients))]
answer = ",".join(answer)
