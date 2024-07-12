turkey_cooking_time = 14

ham_cooking_time = 8

start_time = int(input("Provide start time "))

def cooking_end_time(start_time, duration):
    end_time = (start_time + duration) % 24
    return end_time

print(f"Take the Turkey out of the oven at: {cooking_end_time(start_time, turkey_cooking_time)}")

print(f"Take the Ham out of the oven at: {cooking_end_time(start_time, ham_cooking_time)}")