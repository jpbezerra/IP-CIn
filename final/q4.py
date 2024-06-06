number = int(input())
count = 0

for numb in range(1, number):
    if number % numb == 0:
        count += numb

if count == number:
    print(f"O número {number} é perfeito!")

else:
    print(f"O número {number} não é perfeito!")