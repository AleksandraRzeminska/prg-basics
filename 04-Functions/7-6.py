def hide(card_number):
    return card_number[:2] + "*" * (len(card_number) - 6) + card_number[-4:]
    

if __name__ == "__main__":
    print(hide("5290312400019022"))