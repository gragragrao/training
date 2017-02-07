# 制御処理




# 問題 1

num = int(input("what number do you want to look at?"))
# inputされるデータはstringであることに注意する。
def judge_odd_even():
    if num % 2 == 1:
        return "odd"
    else:
        return "even"

print(judge_odd_even())





# 問題 2

def count_even(list):
    count = 0
    for i in list:
        if i % 2 == 0:
            count += 1
    return count


print(count_even([1, 3, 4, 2, 7, 10]))
print(count_even([]))





# 問題 3

def list_contain(name, list):
    if name in list:
        return "True"
    else:
        return "False"

print(list_contain("Tom", ["Tom", "Michael", "Tony", "Mike", "John"]))
