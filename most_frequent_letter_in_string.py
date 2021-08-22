name = input("Enter the word : ")
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
result = (most_frequent(name))
result = sorted(result.items(), key=lambda item: item[1], reverse=True)
print(result)
