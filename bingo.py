import random
import ast

def pop(a,accumulated=None):
    print("type q to move on to verification")
    if accumulated is None:
        accumulated = set()
    v = 'I can put any string here, as long as it is not "q" :-)'
    while v.lower() != 'q':
        b = a.pop(0)
        if b <= 15:
            print ('b', b, end=' ')
        elif 15 < b <=30:
            print ('i', b, end=' ')
        elif 30 < b <=45:
            print ('n', b, end=' ')
        elif 45 < b <=60:
            print ('g', b, end=' ')
        else:
            print ('o', b, end=' ')
        accumulated.add(b)
        v = input()
    return accumulated

def verify(numbers, length):
    new_nums = input("enter " + str(length) + " numbers separated by ',': ")
    nums = ast.literal_eval(new_nums)
    assert( len(nums) == length ) #Need 5 numbers to win
    result = set(nums).issubset(numbers)
    print ("Verified? ",result, "\n")
    return result
    #alternatively, and probably slightly more efficient
    # print numbers.issuperset(nums)
    #I prefer the other though as `subset` is easier for me to remember


def robust_verify(numbers, length):
   """
   keep trying to verify the numbers until we succeed
   """
   try:
       result = verify(numbers, length)
       return result
   except (AssertionError,SyntaxError,TypeError):  #other error conditions might go here too, but these are the ones I can think of right now ...
       robust_verify(numbers, length)
  


def play_bingo(length=5, game_vals=None,accumulated=None):   
    if game_vals is None:
        game_vals = list(range(1,76))  #list strictly not necessary here, but why not?
        random.shuffle(game_vals)

    nums = pop(game_vals,accumulated=accumulated)
    if not robust_verify(nums, length):
        play_bingo(game_vals=game_vals,accumulated=nums)
    else:
        replay()

def replay():
    again = input("\n Would you like to play again? ")
    if again.casefold() == "y" or again.casefold() == "yes":
        play_bingo(length=game_mode())
    else:
        print("Thank you for playing! Press enter to exit.")
        quit()


def game_mode():
    mode = None
    
    game_type = input("What type of game would you like to play? \nA) Classic Bingo\nB) Four Corners\nC) Blackout\nD) Custom: ")

    if game_type.upper() == "A":
        mode = 5
    elif game_type.upper() == "B":
        mode = 4
    elif game_type.upper() == "C":
        mode = 24
    elif game_type.upper() == "D":
        mode = input("Please input custom validation length")
    else:
        print("That is not a valid response, please try again. \n")
        mode = game_mode()
    return mode

play_bingo(length = game_mode())