money = input("How much do I owe you?:")
money_str = float(money)
money_int = round(money_str*100)
counter = 0

while (money_int > 0):
    counter = int (money_int / 25);
    money_int = money_int % 25;
    counter = counter + int(money_int / 10);
    money_int = money_int % 10;
    counter = counter + int(money_int / 5);
    money_int = money_int % 5;    
    counter = counter + int(money_int / 1);
    money_int = money_int % 1
    print (counter)
