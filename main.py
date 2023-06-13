"""Contains a class to represent a coffee vending machine"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


class CoffeeMachine:
    """Coffee vending machine"""
    def __init__(self, starting_resources, menu):
        self.resources = starting_resources.copy()
        self.menu = menu
        self.order_prompt()

    def order_prompt(self):
        """Prompts the user to enter their order"""
        order = input("What would you like? \n")
        if order == "off":
            print("Shutting down.")
            return
        elif order == "print report":
            return self.print_report()
        else:
            return self.check_ingredients(order)

    def check_ingredients(self, order):
        """Checks to make sure there are sufficient ingredients for the user's order"""
        not_enough = []
        for ingredient, amount_needed in self.menu[order]["ingredients"].items():
            if amount_needed > self.resources[ingredient]:
                not_enough.append(ingredient)
        if not_enough:
            print(f"Sorry, not enough {not_enough}")
            return self.order_prompt()
        return self.process_coins(order)

    def process_coins(self, order):
        """Takes coins"""
        total = self.menu[order]['cost']
        print(f"Total: {total}")
        quarters = int(input("How many quarters? \n")) * 0.25
        dimes = int(input("How many dimes? \n")) * 0.10
        nickels = int(input("How many nickels? \n")) * 0.05
        pennies = int(input("How many pennies? \n")) * 0.01
        amount_paid = quarters + dimes + nickels + pennies
        return self.transaction_successful(order, total, amount_paid)

    def transaction_successful(self, order, total, amount_paid):
        """Check to see if the user input enough money and distributes change"""
        if amount_paid < total:
            print("Insufficient funds. Refunding coins.")
            return self.order_prompt()
        else:
            print(f"Change: {amount_paid - total}. Please wait while your drink is being made.")
            return self.make_drink(order)

    def make_drink(self, order):
        """Subtract ingredients from the machines resources to make the drink"""
        for ingredient, amount in self.menu[order]['ingredients'].items():
            self.resources[ingredient] = self.resources[ingredient] - amount
        print(f"Here is your {order}. Thank you!")
        return self.order_prompt()

    def print_report(self):
        """Print how much there is of each ingredient"""
        print(self.resources)
        return self.order_prompt()
