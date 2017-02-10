# 正規表現

# 問題 1

def eliminate_parameters(s):
    if "?" in s:
        return s[0:s.find("?")]
    else:
        return s

print(eliminate_parameters("html://scouty.co.jp/search?location=Tokyo&escore=3.0"))
# >>> html://scouty.co.jp/search

print(eliminate_parameters("html://scouty.co.jp/search"))
# >>> html://scouty.co.jp/search


# print(dict(one=1, two=2))

# 問題 2

# 作戦
# 1."?"以降を切り取る。
# 2."&"でsplit()
# 3.","でjoin()
# 4.dict()


def create_parameter_dict(s):
    s1 = s.replace(eliminate_parameters(s)+"?", "")  # "?"以降を切り取る
    s2 = s1.replace("&", ", ")
    # >> location=Tokyo, escore=3.0

    return dict(s2)

    # なんでこれでうまくいかないのかわかりません...


print(create_parameter_dict("http://scouty.co.jp/search?location=Tokyo&escore=3.0"))
