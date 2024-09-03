

start_time = 20
cooking_duration = 14

end_time = (start_time + cooking_duration) % 24

print(f"Take the turkey out of the oven at: {end_time}")