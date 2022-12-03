

s = input("Введите строку")
count = 0
vowels = set("aeiou")
for letters in s:
    if letters in vowels:
        count += 1
    print("Количество гласных равно:")
    print(count)