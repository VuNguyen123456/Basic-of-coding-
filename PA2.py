def gas_price(prev_price, new_price):
    #Price unchanged/decrease
    if new_price <= prev_price:
     result = 'Full Tank'
    #Price increase less than 20%
    elif prev_price * 1.2 > new_price:
     result = '3/4 Tank'
    #Price increase by 20% or more but less than 80%
    elif prev_price * 1.8 > new_price:
     result = 'Half Tank'
    #Price increase by 80% or more but less than 100%
    elif prev_price * 2 > new_price:
     result = '1/4 Tank'
    #Price increase by 100% or more
    elif prev_price * 2 <= new_price:
     result = 'Go Home'
    #Return the result of the function acording to the input
    return result


def level(num_coins, difficulty):
    #The level of the game at beginner difficulty
    if  difficulty == 'Beginner':
     result = num_coins // 4
    #The level of the game at amateur difficulty
    elif difficulty == 'Amateur':
     result = num_coins // 4
    #The level of the game at intermediate difficulty
    elif difficulty == 'Intermediate':
     result = num_coins // 6
    #The level of the game at pro difficulty
    elif difficulty == 'Pro':
     result = num_coins // 6
    #The level of the game at expert difficulty
    elif difficulty == 'Expert':
     result = num_coins // 8
    #The level of the game at legendary difficulty
    elif difficulty == 'Legendary':
     result = num_coins // 10
    #Return the result of the function acording to the input
    return result
    
def card_game(player1_card, player2_card, tiebreak_with_card):
    #Finding the suit of player 1
    suit1 = (((player1_card-1)//13)+1)
    #Finding the suit of player 2
    suit2 = (((player2_card-1)//13)+1)
    #Finding the card number of player 1
    num1 = ((player1_card-1)%13)+1
    #Finding the card number of player 2
    num2 = ((player2_card-1)%13)+1
    
    #Finding the winner
    if suit1 < suit2 and num1 > num2:
     result = 'Player 1 Wins'
    elif suit1 > suit2 and num1 < num2:
     result = 'Player 2 Wins'
    #Tiebreaker
    else:
     #Tiebreaker when decided by card number
     if tiebreak_with_card == True and num1 > num2:
       result = 'Player 1 Wins'
     elif tiebreak_with_card == True and num1 < num2:
       result = 'Player 2 Wins'
     #Tiebreaker when decided by suit
     elif tiebreak_with_card == False and suit1 < suit2:
       result = 'Player 1 Wins'
     elif tiebreak_with_card == False and suit1 > suit2:
       result = 'Player 2 Wins'
     else:
      result = 'Tie'
    #Return result
    return result
      
