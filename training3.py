# ディクショナリ


# 問題 1

def multiply_dict(dic, n):
    for key in dic:
        dic[key] *= n
    return dic

print(multiply_dict({"Tom" : 90, "Jane" : 43, "Mike" : 32}, 10))
# >>> {"Tom" : 900, "Jane" : 430, "Mike" : 320}

'''
正解です。

ディクショナリの内包表記を使うとカッコよく書けます

def multiply_dict(dic, n):
    return {key: value * n for key, value in dic.items()}
'''


# 問題 2


def merge_dict(a, b):
    for key in b:
        if key in a:
            a[key] += b[key]
        else:
            a.update({key: b[key]})
    return a

print(merge_dict({"Tom": 90, "Jane": 43, "Mike": 32}, {"Michael": 32, "Alice": 32, "Tom": 32, "Mike": 44}))
# >>> {"Tom": 122, "Jane": 43, "Mike": 76, "Michael": 32, "Alice": 32}

'''
正解です

変数名、a, bでなくdict1, dict2とかってわかりやすくつけたいですね
'''



# 問題 3


def sort_dict_by_value(a):
    list = []
    for key in a:
        list.append(key)
    return list


print(sort_dict_by_value({"Michael": 23, "Alice": 54, "Tom": 39, "Mike": 44}))
# >>> ["Michael", "Alice", "Tom", "Mike"]

'''
問題は、valueの値の大きい順に並べ替えてキーのリストを出力、ですよー
'''
