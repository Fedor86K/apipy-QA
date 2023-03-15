
print("\n" + " "*10 + "Welcome to QApiPy launcher!" + " "*10)

choice = input("\nPress key 1 (POST mode) or key 2 (GET mode)...")

if choice == "1":
    exec(open('post.py').read())
    
if choice == "2":
    exec(open('get.py').read())
    
else:
    print("\nUnknown command!")

input("\nPress ""ENTER"" to exit...")


