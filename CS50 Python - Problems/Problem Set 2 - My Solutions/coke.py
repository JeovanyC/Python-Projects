def main():
    amountDue = 50
    coins = [50, 25, 10, 5]
    change = 0

    while amountDue > 0:
        print(f"AmountDue: {amountDue}")
        insertCoin = int(input("Insert Coin: "))

        if insertCoin in coins:
            amountDue -= insertCoin
    
    else:
        change = abs(amountDue)
        print(f"Change Owed: {change}")


if __name__ == "__main__":
    main()