with open("files/day21.txt") as file:
    foods_list = [i.strip() for i in file]
# print(foods_list)

from collections import defaultdict

maybe_allergens = defaultdict(set)
all_allergens = set()
all_ingredients = set()
willkillyou_ingredients = set()
foods = []
# print(maybe_allergens)
# print(all_allergens)
# print(all_ingredients)
# print(willkillyou_ingredients)
# print(foods)

for i in foods_list:
    i = i.split(" (contains ")

    all_ingredients.update(i[0].split())
    all_allergens.update(i[1].replace(")", "").replace(",", "").split())
    foods.append(i[0].split())

    for x in i[1].replace(")", "").replace(",", "").split():
        if x not in maybe_allergens:
            maybe_allergens[x] = set(i[0].split())

        else:
            maybe_allergens[x].intersection_update(i[0].split())


# print(maybe_allergens)
# print(all_allergens)
# print(willkillyou_ingredients)
# print(foods)


allergen_ingredient = {}
while len(allergen_ingredient) != len(all_allergens):
    for i, ingredients in maybe_allergens.items():

        ingredients -= willkillyou_ingredients

        if len(ingredients) == 1:
            ingredient = ingredients.pop()
            allergen_ingredient[i] = ingredient
            willkillyou_ingredients.add(ingredient)

# print(allergen_ingredient, willkillyou_ingredients)
safe_ingredients = all_ingredients - willkillyou_ingredients
# print(safe_ingredients)

p1 = 0
for line in foods:
    p1 += len(safe_ingredients.intersection(line))


print(f"part1: {p1}")


canonical_dangerous_ingredient_list = ",".join(
    [allergen_ingredient[i] for i in sorted(allergen_ingredient.keys())])
print("part2:", canonical_dangerous_ingredient_list)
