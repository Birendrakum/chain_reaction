string = input()
arr = []
result = 0
length = 0
for i in string:
    if i == "(":
        arr.append("(")
        len += 1
    elif i == ")":
        if length >= 1:
            arr.pop(-1)
        else:
            result = 1
            break
print(result)
