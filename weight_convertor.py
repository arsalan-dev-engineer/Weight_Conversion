
def user_choice():
    """This function is used for navigating user"""
    userWeight = int(input("\nSelect weight conversion\n" +
                           "1. kg\n" +
                           "2. stone\n" +
                           "3. pound\n"))

    if userWeight == 1:
        kilograms()

    elif userWeight == 2:
        stone()

    elif userWeight == 3:
        pound()


def kilograms():
    """This function converts user weight from kg to stones and pounds"""
    user_weight = float(input("Your weight in kilograms: "))
    print()

    stones = lambda s: s * 0.157473
    print("Your weight in stones: {0:.4f}".format(stones(user_weight)))

    pounds = lambda p: p * 2.20462
    print("Your weight in pounds: {0:.4f}".format(pounds(user_weight)))
    user_choice()


def stone():
    """This function converts user weight from stones to kg and pounds"""
    user_weight = float(input("Your weight in stones: "))
    print()

    kg = lambda k: k * 6.35029
    print("Your weight in kg: {0:.4f}".format(kg(user_weight)))

    pounds = lambda p: p * 14
    print("Your weight in pounds: {0:.4f}".format(pounds(user_weight)))
    user_choice()


def pound():
    """This function converts user weight from pounds to kg and stones"""
    user_weight = float(input("your weight in pounds: "))
    print()

    kg = lambda k: k * 0.453592
    print("Your weight in kg: {0:.4f}".format(kg(user_weight)))

    stones = lambda s: s * 0.0714286
    print("Your weight in stones: {0:.4f}".format(stones(user_weight)))
    user_choice()


user_choice()
