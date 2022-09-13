d = {
    "key": "value",
    123: 54321,
    10: {"another": "first"},
}

print(d[123])

print(list(d.keys()))
print(list(d.items()))
print(list(d.values()))

print(d.get("browser", "Если нет такого ключа, то будет эта строка"))
