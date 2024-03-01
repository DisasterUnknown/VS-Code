car_started = False
controles = ("""
Enter 'help' for controls!
Enter 'start' to start the car!
Enter 'stop' to stop the car!
Enter 'quit' to quit!
                            """)


print(controles)
while True:
    opption = input("Enter opption > ").lower()
    if opption == 'start':
        if car_started:
            print("Car Has Already Started!")
        else:
            print("Car Started!")
            car_started = True
    elif opption == 'stop':
        if car_started:
            print("Car Stoped!")
            car_started = False
        else:
            print('Car Has Already Stoped!')
    elif opption == 'quit':
        break
    elif opption == 'help':
        print(controles)
    else:
        print("Sorry I can't understand it!")