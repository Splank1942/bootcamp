def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

def follow_roundabout(exit_number):
    print(f"taking exit number {exit_number} from the roundabout")

print("Start Engine")

destination = input("Where do you want to go? ")

if destination == "library":
    move_forward()
    turn("left")
    print("You have arrived at the library!")
elif destination == "tech park":
       move_forward()
       turn("left")
       print("You have arrived at the tech park")
elif destination in ["hospital", "mall", "airport", "university", "stadium"]:
      move_forward()
      if destination == "hospital":
            follow_roundabout(1) 
            print("You have arrived at the hospital!")
      elif destination == "mall":
            follow_roundabout(2)
            move_forward()
            turn("right")
            print("You have arrived at the mall!")
      elif destination == "airport":
            follow_roundabout(3)
            print("You have arrived at the airport!")
      elif destination == "university" or "stadium":
            follow_roundabout(4)
            move_forward()
            if destination == "university":
                  turn("left")
                  print("You have arrived at the university!")
            else:
                  turn("right")
                  print("You have arrived at the stadium!")
else:
      print("That is not a valid destination!")

stop_engine()
