# リスト



# 練習も兼ねて例外処理を使っています。

# 問題 1

class MyException(Exception):
    pass

def get_average(a):
    try:
        if len(a) == 0:
            raise MyException("list is empty.")
        average = sum(a) / len(a)
        return average

    except MyException as msg:
        return msg

print(get_average([1.3, 2.2, 10.3, 4.3]))
# >>> 4.525

print(get_average([]))
# >>> list is empty.





# 問題 2

def get_variance(a):
    try:
        if len(a) == 0:
            raise MyException("list is empty.")
        sum_2 = 0
        for i in a:
            sum_2 += (i - get_average(a)) ** 2

        var = sum_2 / len(a)
        return var

    except MyException as msg:
        return msg

print(get_variance([1.3, 2.2, 10.3, 4.3]))
# >>> 12.301875000000003

print(get_variance([]))



# 問題 3

def remove_overlap(a):
    a = list(set(a))
    return a

print(remove_overlap([1, 2, 4, 2, 4, 9, 4, 8]))
print(remove_overlap(["hoge", "foo", "hoge", "bar", "foo"]))
