"""
A virtual vending machine.
"""
# A list of coins allowed
ACCEPTABLE_COINS = [5]

def insert_coin(coin, inserted_coins):
    """
    Accepts a coin and appends it to inserted_coins list.
    """
    if coin not in ACCEPTABLE_COINS:
        raise ValueError
    inserted_coins.append(coin)


class InsufficientFunds(Exception):
    """
    Exception used to indicate that there isn't
    enough money to make a purchase.
    """
