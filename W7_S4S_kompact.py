# Решение Алексея Киреева с лямбда функцией и двумя ключами в функции sorted
fin = open('input.txt')
# f = fin.read().split()
words = dict()
for i in fin.read().split():  # for i in f:
    words[i] = words[i] + 1 if i in words else 1
print(sorted(words, key=lambda x: (-words[x], x))[0])
