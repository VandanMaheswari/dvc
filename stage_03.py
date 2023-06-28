with open("artifacts.txt","r") as f:
    text=f.read()
    
with open("artifacts.txt","w") as f:
    text=f.write(text+"i have added one line")
    
    
print(text)
print("it is a end of stage 3")