
print("\n" + " "*10 + "Welcome to QApipy launcher!" + " "*10)

choice = input("\nPress key 1 (POST mode) or key 2 (GET mode)...")

if choice == "1":
    exec(open('post.py').read())
    
if choice == "2":
    exec(open('get.py').read())
    
else:
    pass

input("\nPress ""ENTER"" to exit...")


