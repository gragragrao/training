# ディクショナリ


# 問題 1

def multiply_dict(dic, n):
    for key in dic:
        dic[key] *= n
    return dic

print(multiply_dict({"Tom" : 90, "Jane" : 43, "Mike" : 32}, 10))




# 問題 2


def merge_dict(a, b):
    for key in b:
        if key in a:
            a[key] += b[key]
        else:
            a.update({key: b[key]})
    return a

print(merge_dict({"Tom": 90, "Jane": 43, "Mike": 32}, {"Michael": 32, "Alice": 32, "Tom": 32, "Mike": 44}))




# 問題 3
