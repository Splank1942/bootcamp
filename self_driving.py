

def move_forward():
    print("moving forward")

def stop_moving():
    print("stop")

def turn(direction):
    print(f"turning {direction}")    

def start_engine():
    print("starting engine")    

def stop_engine():
    print("stopping engine")    

def park():
    print("pull in to parking spot")   

destination = input("Where do you want to go? ")

start_engine()
move_forward()
stop_moving()

if destination == "school":
    turn("right")
    move_forward()
    stop_moving()
    turn("left")
    move_forward()
    park()
    stop_moving()
    stop_engine()
    print("We arrived at the school, hooray science!")


elif destination == "grocery store":
    turn("left")
    move_forward()
    stop_moving()
    turn("right")
    move_forward()
    park()
    stop_moving()
    stop_engine()  
    print("We arrived at the grocery store, nom nom nom!")