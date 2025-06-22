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

profit = 0
avail_resources = {"water": 1000, "milk": 800, "coffee": 150}
is_on = True
money = {'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01}


def selection(user, profit):
    if user in MENU:
        print(MENU[user])
        return profit
    else:
        print("sahi se dekh kar likh")
        return profit


def reso_check(user):
    ingreeds = MENU[user]['ingredients']
    for item in ingreeds:
        if avail_resources.get(item, 0) < ingreeds[item]:
            print(f"{item} kam hai resource bro ❌")
            return False
    return True


def coins():
    total = 0
    for coin in money:
        value = money[coin]
        count = int(input(f"Kitne {coin}? (1 {coin} = {value}) "))
        total += count * value
    total = round(total, 2)
    print(f"Tune itna diya: ${total}")
    return total


def make_cofffee(user):
    ingreeds = MENU[user]['ingredients']
    for item in ingreeds:
        avail_resources[item] -= ingreeds[item]
    print(f"{user} ban gaya bro ☕")
    print(f"Bacha hua resource: {avail_resources}")


while is_on:
    user = input('kya lega bro : latte/cappuccino/espresso? (off/report bhi likh) \n').lower()

    if user == "off":
        is_on = False
        print("Thanks for coming bro 👋")
    elif user == "report":
        print(f"Total kamaya: ${profit}")
        print(f"Resources: {avail_resources}")
    elif user in MENU:
        if reso_check(user):
            selection(user, profit)
            payment = coins()
            cost = MENU[user]['cost']
            if payment >= cost:
                change = round(payment - cost, 2)
                if change > 0:
                    print(f"Le bhai tera change: ${change}")
                profit += cost
                make_cofffee(user)
            else:
                print("Paise kam hai bro, refund kar diya.")
        print(f"Total kamaya: ${profit}")
    else:
        print("Sahi se likh bhai, latte/espresso/cappuccino likh ☕")
