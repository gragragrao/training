# 内包表記（comprehension）
# リストや辞書におけるループ処理を簡単・シンプルに書くための記法。

# [種類]
# 1.リスト内包

print([x ** 2 for x in [1,2,3,4,5]])
# >>> [1, 4, 9, 16, 25]

print([x + 2 for x in range(5)])
# >>> [2, 3, 4, 5, 6]

# 2.ジェネレータ式：（）で定義する。要素を一つずつ生成するジェネレータを作る

a = 0
for y in (x ** 2 for x in range(5)):
    a += y

print(a)


# このように、ジェネレエータ式はfor文に組み込まれることがほとんどだが、以下が基本。


s = (x + 4 for x in range(10))

print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))



# 3.セット内包表記

print({x ** 4 for x in range(15)})

print(2 ** 4)




# 4.辞書内包
