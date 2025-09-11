day=5
month=5
match day:
    case 1|2|3|4|5 if month==5 :
        print("Wednesday")
        
    case _:
        print("invalid day")    
day=int(input("Enter the number of day : "))
match day:
    case 1 :
        print("Monday")
    case 2 :
        print('Tuesday')
    case 3 :
        print("Wednesday")
    case 4 :
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
day=int(input("Enter the number : "))
match day:
    case 1|2|3|4|5 :
        print("Weekdays")
    case _:
        print("Weekend")