

def move_forward():
    print("moving forward")

def stop_moving():
    print("stop at stop sign")

def stop():
    print("stop")    

def turn(direction):
    print(f"turning {direction}")    

def start_engine():
    print("starting engine")    

def stop_engine():
    print("turn off engine")    

def park():
    print("pull in to a parking spot")   

def reverse():
    print("back out of the drive-way")    

destination = input("Where do you want to go? ")



if destination == "school":
    start_engine()
    reverse()
    move_forward()
    stop_moving()
    turn("right")
    move_forward()
    stop_moving()
    turn("left")
    move_forward()
    park()
    stop()
    stop_engine()
    print("We arrived at the school, hooray science!")


elif destination == "grocery store" or destination == "dentist":
    start_engine()
    reverse()
    move_forward()
    stop_moving()
    turn("left")
    move_forward()
    stop_moving()
    if destination == "grocery store":
        turn("right")
        move_forward()
        park()
        stop()
        stop_engine()  
        print("We arrived at the grocery store, nom nom nom!")
    else:
        turn("left")
        move_forward()
        park()
        stop()
        stop_engine()  
        print("We arrived at the dentist! I hope he prescibes pain meds, ouch!")
elif destination == "restaurant":
    start_engine()
    reverse()
    move_forward()
    stop_moving()
    move_forward()
    stop_moving()
    turn("right")
    move_forward()
    park()
    stop()
    stop_engine()  
    print("We arrived at the Bucca di Beppo, noms all night!")


else:
    print("This is not a valid destination for this version of Tesla AutoPilot, pay Elon Musk 1 million dollars or the vehicle will catch fire in 30 seconds!!!")