# 制御処理




# 問題 1

num = int(input("what number do you want to look at?"))
# inputされるデータはstringであることに注意する。
def judge_odd_even():
    if num % 2 == 1:
        print("odd")
    else:
        print("even")
judge_odd_even()




# 問題 2

def count_even(list):
    count = 0
    for i in list:
        if i % 2 == 0:
            count += 1
    print(count)

# count_even([1, 3, 4, 2, 7, 10])
# count_even([])




# 問題 3

def list_contain(name, list):
    if name in list:
        print("True")
    else:
        print("False")

# list_contain("Tom", ["Tom", "Michael", "Tony", "Mike", "John"])
