import sys
from collections import defaultdict


def get_products(to_buy, recipes, product, mult):
    for ingredient in recipes[product]:
        if ingredient in recipes:
            to_buy = get_products(to_buy, recipes, ingredient, mult * recipes[product][ingredient])
        else:
            to_buy[ingredient] += mult * recipes[product][ingredient]
    return to_buy


def eval_products_to_buy(dishes, recipes, reefer):
    to_buy = defaultdict(int)
    for dish_name, dish_count in dishes.items():
        to_buy = get_products(to_buy, recipes, dish_name, dish_count)
    for ingredient in reefer:
        if ingredient in to_buy:
            to_buy[ingredient] -= reefer[ingredient]
            if to_buy[ingredient] <= 0:
                del to_buy[ingredient]
    to_buy = sorted(to_buy.items(), key=lambda x: x[0])
    for prod_name, prod_count in to_buy:
        print(prod_name, prod_count)


def main():
    num_iter = int(sys.stdin.readline())

    for n_iter in range(num_iter):
        dishes = dict()
        recipes = dict()
        reefer = dict()
        n_dishes, n_recipes, n_reefer = map(int, sys.stdin.readline().split())
        for _ in range(n_dishes):
            dish_name, dish_count = sys.stdin.readline().split()
            dishes[dish_name] = int(dish_count)
        for _ in range(n_recipes):
            recipe_name, recipe_count = sys.stdin.readline().split()
            recipes[recipe_name] = dict()
            for __ in range(int(recipe_count)):
                ingredient_name, ingredient_count = sys.stdin.readline().split()
                recipes[recipe_name][ingredient_name] = int(ingredient_count)
        for _ in range(n_reefer):
            ingredient_name, ingredient_count = sys.stdin.readline().split()
            reefer[ingredient_name] = int(ingredient_count)

        eval_products_to_buy(dishes, recipes, reefer)


if __name__ == '__main__':
    main()
