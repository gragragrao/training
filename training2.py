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


'''
正解です。

例外使ってるのいいですね。
ただ、自分で if else の文で例外飛ばすなら、実質if else だけで書けるのでtryを使わない方がシンプルです。

例外を正しく使ってカッコよくかくなら、
def get_average(a):
    try:
        average = sum(a) / len(a)
        return average

    except Exception as msg:
        return msg

がbetterです。なぜなら
a = []　
のとき、len(a)が0なので、
average = sum(a) / len(a)
で数字を0で割るというでマジな例外が発生して、そいつをキャッチしてくれるからです。
'''



# 問題 2

def get_varianace(a):
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
# >>> 0

'''
正解です。

変数名にも気を遣いましょう
aという変数名はパッと見なんなのかよくわからないので、
型を連想させる名前がよいです。int_listとか
一文字がよければ、リストならlとかが通例。

'''

'''
# scoutyで実際に使っている get varianceはこちら。
def get_variance(l):
    average = get_average(l)
    return get_average([(e - average)**2 for e in l])

# ちなみに上級レベルの質問ですが、
def get_variance(l):
    return get_average([(e - get_average(l))**2 for e in l])

# と書かないのは何故かわかりますか？ （もちろん正常に動きます）
'''

# 問題 3

def remove_overlap(a):
    a = list(set(a))
    return a

print(remove_overlap([1, 2, 4, 2, 4, 9, 4, 8]))
# >>> [1, 2, 4, 9, 8]

print(remove_overlap(["hoge", "foo", "hoge", "bar", "foo"]))
# >>> ["hoge", "foo", "bar"]

'''
正解！

def remove_overlap(a):
    return list(set(a))

の方がシンプルでいいですね
'''
