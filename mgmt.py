menuCard = {"burger": 100,"pizza": 200,"fries": 50,"sandwich": 150,"coke": 25,"pepsi": 25,"chicken": 150,"mutton": 200,"chocolate": 50,"iceCream": 50}

print('Menu List is :')
print()

for i in menuCard:
    print(i, ':', menuCard[i])
print()

item_buied = []
total_amount = 0
def askItem(item_buied,total_amount):
    ask_to_buy = input('Do you want to buy something? (y/n): ')
    print()

    if ask_to_buy == 'y' or ask_to_buy == 'Y' or ask_to_buy == 'Yes' or ask_to_buy == 'yes':
        item = input('Enter the item you want to buy: ')
        print()
        if item not in menuCard:
            print('Item not found in the menu. Please choose something else.')
            print()
            return askItem(item_buied,total_amount)
        else:
            ask_quantity = int(input('Enter the quantity: '))
            if ask_quantity < 1:
                print('Please enter a valid quantity.')
                print()
                return askItem(item_buied,total_amount)
            elif ask_quantity > 10:
                print('Please enter a quantity less than 10.')
                print()
                return askItem(item_buied, total_amount)
            else:
                item_buied.append(menuCard[item]*ask_quantity)
                return askItem(item_buied,total_amount)
    elif ask_to_buy == 'n' or ask_to_buy == 'N' or ask_to_buy == 'No' or ask_to_buy == 'no':
        for i in range(len(item_buied)):
            total_amount += item_buied[i]

        print('Total Amount is :', total_amount, 'Rs')
        return "Thankyou For Visiting. Hope to See You Soon.. :)"
    else:
        print('Please enter a valid option.')
        print()
        return askItem(item_buied, total_amount)
    
    
        
print(askItem(item_buied,total_amount))
