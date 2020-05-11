
is_male = True
is_tall = False

if is_male or is_tall:
    print("You are male, tall or both")
else:
    print("you are neither tall nor male")
    
if is_male and is_tall:
    print("You are a tall male")
else:
    print("you are either not male, not tall or both")
    
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male, but you are tall")