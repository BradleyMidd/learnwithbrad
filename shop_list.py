# Basic Shopping list
products = ["Apple", "Pear", "Cornflakes", "Cookie", "Chips", "Ice Cream"]

my_list = []

while len(my_list) < 3:
    pro_list = print("\n".join(products) + "\n")
    choose = input("Pick the products available above: ").upper()

    # Short way of adding products to your list
    for i in range(len(products)):
        if choose == products[i].upper():
            print(products[i] + " is added to your list \n")
            my_list.append(products[i])
            break

    else:
        print("\nThis product is not in our list! Please try again \n")

# Long way of adding product to your list
"""
    if choose == products[0].upper():
        print(products[0] + " is added to your list \n")
        my_list.append(products[0])

    elif choose == products[1].upper():
        print(products[1] + " is added to your list \n")
        my_list.append(products[1])

    elif choose == products[2].upper():
        print(products[2] + " is added to your list \n")
        my_list.append(products[2])

    elif choose == products[3].upper():
        print(products[3] + " is added to your list \n")
        my_list.append(products[3])

    elif choose == products[4].upper():
        print(products[4] + " is added to your list \n")
        my_list.append(products[4])

    elif choose == products[5].upper():
        print(products[5] + " is added to your list \n")
        my_list.append(products[5])

    else:
        print("\nThis product is not in our list! Please try again \n")
"""

if len(my_list) == 3:
    print("The products you have chosen: \n")
    print("\n".join(my_list))