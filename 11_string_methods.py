python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)

index = python.index("n", index + 1)
print(index)
# print(python.index("Java"))  # 오류

print(python.find("n"))
print(python.find("Java"))  # -1 반환

print(python.count("n"))
