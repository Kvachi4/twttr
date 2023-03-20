vowels = ['A', 'E', 'I', 'O', 'U']
my_text = input("INPUT: ").upper()

for i in my_text:
    if i in vowels:
         my_text = my_text.replace(i, "")
print("OUTPUT: ", my_text)