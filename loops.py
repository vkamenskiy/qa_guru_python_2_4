i = 0

while i < 10:
    #print("Hello " + str(i))
    # i = i + 1
    i +=1

for i in range(10):
    print(f"Hello {i}")

for i, element in enumerate([1, "two", "three"]):
    print(i, element)

for key, value in {"first": 1, "second": 2}.items():
    print(f"В ключе {key} содержится значение {value}")

