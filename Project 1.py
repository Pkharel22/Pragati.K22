https://app.codingrooms.com/app/course/computer-programming-QezJJAW/b/project%253A-text-game-ixXkN6k

########
#import modules
#######

########
#define functions
#######
def start():
    print("Welcome!")
    frontdesk()

def frontdesk():
    print("You are in frontdesk") 
    move = input("\nWhere would you like to go? Say one of these choices vending machine, book shelves, stay here")
    if move.lower() == "vending machine":
        vendingmachine()
    elif move.lower() == "bookshelf":
        bookshelf()
    else:
        #TODO: what should happen if they type something else?
        pass
        
def vendingmachine():
    print("You are in vendingmachine")
    move = input("\nWhere would you like to go? Say one of these choices"
    "stay here, bookshelf, frontdesk")
    if move.lower() == "vending machine":
        room1()
    elif move.lower() == "book shelf":
        room3()
    else:
        #TODO: what should happen if they type something else?
        pass

def bookshelf():
    print("You are in bookshelf")
    move = input("\nWhere would you like to go? Say one of these choices:\n\stay here, vendingmachine, frontdesk")
    if move.lower() == "vending machine":
        room2()
    elif move.lower() == "front desk":
        room1()
    else:
        #TODO: what should happen if they type something else?
        pass