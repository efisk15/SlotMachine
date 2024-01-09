MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: print("Must be a number between 0 and " + MAX_LINES + " .")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        bet = input(f"How much would you like to bet on each Line?(Min Amount:${MIN_BET} Max Amount:${MAX_BET}) $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please print a number between ${MIN_BET} and ${MAX_BET}!")
        else:
            print("Please print a real number!")

    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    print(balance, lines, bet)

main()