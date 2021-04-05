class CoffeeMachine:
    n_machine = 0
    states = ['main_menu', 'buy', 'fill', 'take', 'remaining', 'exit']
    state = None

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.money = 550
        self.cups = 9
        self.state = 'main_menu'

    def buy_coffee(self):
        ingredients = [self.water, self.milk, self.beans, self.cups, self.money]
        count_espresso = (-250, 0, -16, -1, 4)  # Amount of ingredients for espresso
        count_latte = (-350, -75, -20, -1, 7)  # Amount of ingredients for latte
        count_capuc = (-200, -100, -12, -1, 6)  # Amount of ingredients for cappucino
        coffee = (count_espresso, count_latte, count_capuc)  # List of coffee's sorts
        name_ingr = ['water', 'milk', 'beans', 'cups']  # Name of ingredients
        empty_ingr = []  # List for ingredients missing
        choice = ''
        while choice not in ('1', '2', '3', 'back'):
            choice = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n").strip()
        if choice in ('1', '2', '3'):
            choice = int(choice) - 1
            for i in range(5):
                ingredients[i] += coffee[choice][i]
            if all([x > 0 for x in ingredients]):  # If all ingredients are present
                self.water += coffee[choice][0]  # Then the machine prepares coffee
                self.milk += coffee[choice][1]
                self.beans += coffee[choice][2]
                self.cups += coffee[choice][3]
                self.money += coffee[choice][4]
                print("I have enough resources, making you a coffee!")
            else:  # Otherwise, the missing ingredients are added to the list
                for i in [negative_num for negative_num in ingredients if negative_num < 0]:
                    empty_ingr.append(name_ingr[ingredients.index(i)])  # Message is displayed that
                print(f"Sorry, not enough {' and '.join(empty_ingr)}!")  # some ingredients are missing.
        self.state = 'main_menu'
        print()

    def fill_ingredients(self):
        self.water += int(input("\nWrite how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
        self.state = 'main_menu'
        print()

    def take_money(self):
        print(f"\nI gave you ${self.money}\n")
        self.money = 0
        self.state = 'main_menu'

    def remaining(self):
        print(f'''
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
{self.money} of money\n''')
        self.state = 'main_menu'

    def main_menu(self):
        while self.state not in self.states[1:]:
            self.state = input("Write action (buy, fill, take, remaining, exit):\n").strip()

    def work(self):
        while self.state != 'exit':
            if self.state == 'main_menu':
                self.main_menu()
            if self.state == 'buy':
                self.buy_coffee()
            if self.state == 'fill':
                self.fill_ingredients()
            if self.state == 'take':
                self.take_money()
            if self.state == 'remaining':
                self.remaining()


coffee_machine = CoffeeMachine()
coffee_machine.work()
