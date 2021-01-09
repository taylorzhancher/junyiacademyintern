old = input()
new1 = old.split(" ")
new2 = [i[::-1] for i in new1]
new3 = " ".join(new2)
print(new3)