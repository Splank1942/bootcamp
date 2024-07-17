def ing():
    print(f"The Ingredients for {selection} are:")
    for items in potions[selection]: 
        print(items)

potions = { 
    "Invisibility Potion": ["Moonstone", "Dragon Scale", "Fairy Dust"], 
    "Flying Potion": ["Phoenix Feather", "Troll Tooth", "Mermaid Scale"],
    "Healing Potion": ["Unicorn Horn", "Elf Hair", "Golden Apple"] 
      }

print("Welcome to Splank's Potion Emporium!")
print("Here are the potions we currently have for sale: ")
for items in potions: 
    print(items)

selection = input("Which of our magical potions would you like to buy ingredients for? ")

if selection == "Invisibility Potion":
    ing()
elif selection == "Flying Potion":
    ing()
elif selection == "Healing Potion":
    ing()
else: 
    print("We do not carry that potion please start over.")

print("Let's buy some Ingredients!")

for item in potions[selection][0:3]:
        buy = input(f"Would you like to buy {item}? Yes/No? ")
        if buy == "Yes":
            print(f"You have bought {item}!")
        elif buy == "No":
            print(f"You Have chosen to stop shopping for {selection}!")
            break
if buy == "Yes":   
    print(f"Congratulations you bought all ingredients for {selection}!")