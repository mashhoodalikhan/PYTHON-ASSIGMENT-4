text=input("enter a string:")
alpha=input("enter an alphabet:")
words=text.split(" ")
for word in words:
    if word[0]==alpha:
        print(word)
