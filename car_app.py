command = ""
mode = 0
speed = 0.0

while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if mode == 0:
            mode = 1 # moving
            speed = 15
            print(f"Car is moving at {speed}mph")
        elif mode == 1:
            print(f"Car is already moving")
    elif command == "faster":
        if mode == 1:
            speed += 10
            print(f"Car is moving at {speed}mph")
        elif mode == 0:
            print("You need to start the car first")
    elif command == "slower":
        if mode == 1:
            speed -= 10
            if speed <= 0:
                speed = 0
                mode = 0  # stopped
                print(f"Car is stopped")
            else:
                print(f"Car is moving at {speed}mph")
        elif mode == 0:
            print("You need to start the car first")

    elif command == "stop":
        if mode == 1:
            mode = 0 # stopped
            speed = 0
            print("Car is stopped")
        elif mode == 0:
            print("Car is already stopped")
    elif command == "help":
        print("""start - to start the car
faster - to increase speed
slower - to increase speed
stop - to stop the car
quit - to quit the car""")

    elif command == "quit":
        break
    else:
        print("sorry, I don't understand that command. Try 'help'")


    # give the user warnings
    if 75 <= speed < 85:
        print(f"you should probably slow down.")
    elif 85 <= speed < 95:
        print(f"I think I see a police officer ahead. Better slow down.")
    elif 95 <= speed < 115:
        print(f"The police officer is signally for you to stop")
    elif 115 <= speed < 135:
        print(f"This is dangerous. Someone is going to get hurt")
    elif speed >= 135:
        print(f"You crashed! Drive slower next time.")
        break