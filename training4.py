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

'''
正解ですが、ちょっと書き方がまどろっこしいですね。

正規表現を使うと美しく書けます。
re を復習しときましょ。

def eliminate_parameters(s):
    return re.sub("\?.*", "", st)

'''


# print(dict(one=1, two=2))

# 問題 2

# 作戦
# 1."?"以降を切り取る。
# 2."&"でsplit()
# 3.","でjoin()
# 4.dict()


# ↓↓↓↓↓↓↓↓↓1回目の回答↓↓↓↓↓↓↓↓


# def create_parameter_dict(s):
#     s1 = s.replace(eliminate_parameters(s)+"?", "")  # "?"以降を切り取る
#     s2 = s1.replace("&", ", ")
#     # >> location=Tokyo, escore=3.0
#
#     return dict(s2)
#
#     # なんでこれでうまくいかないのかわかりません...
#
#
# print(create_parameter_dict("http://scouty.co.jp/search?location=Tokyo&escore=3.0"))

'''
作戦2まではGood。

    s1 = s.replace(eliminate_parameters(s)+"?", "")  # "?"以降を切り取る

これめっちゃまどろっこしいですねw
s1 = s.split('?')[1]
とかってキレイにかけます　あと正規表現のgroupを使うとキレイに書けるよ。

なんか dict を勘違いしてないか？
dict は文字列を 辞書にしてくれる関数じゃないぞー
なので作戦 3, 4 はワークしないよー

作戦2以降は 2で&でsplitしたものを、 = の左辺と右辺で分けて、　左辺を key, 右辺をvalueにもつ辞書をつくってくことだ


'''


# 作り直しました。（２回目の回答）


def create_parameter_dict(s):
    parameter_string = s.split("?")[1]
    value_pair_list = parameter_string.split("&")
    parameter_dict = {}

    for value_pair in value_pair_list:
        key, value = value_pair.split("=")
        parameter_dict[key] = value

    aa = [value_pair.split("=") for value_pair in s.split("?")[1].split("&")]
    return {key:value for key, value in aa}

    return parameter_dict

print(create_parameter_dict("http://scouty.co.jp/search?location=Tokyo&escore=3.0"))
# >>> {'location': 'Tokyo', 'escore': '3.0'}





# 問題 3

# 最初の問題

# showwin[at]gmail.com
# showwin at gmail.com
# showwin@gmail dot com
# showwin [at] gmail dot com
# showwin _at_ gmail [dot] com
# showwin _atmk_ gmail.com

# showwinさんの追加課題

# psychedesire(gmail account)
# my-sirname on gmail
# smihica_gmail_com
# 2tacatakataca2(gmail)
# mchachimituserver.gmail.com
# sepeth + gmail.com
# linshao512#gmail.com



# 絶対 "gmail" が入っている。
# アカウント固有文字列の次は "[,  , @, (, _, ., #" のみ
# つまり、アカウント固有文字列を除くことだけ考えればアドレスは
# ".*?(\[| |\(|_|\.|#).*?(\]| |\(|\)|_|\.|#)gmail.*"
# となる。
#
# つまり"(\[| |\(|_|\.|#).*?(\]| |\(|\)|_|\.|#)"を"@"で置き換えて、
# "gmail.*"を"gmail.com"で置き換えたら解決！

import re

'''
def correct_email_address(raw_email):
    if re.match():
        correct_email = re.sub("@.*?@", "@", re.sub("gmail.*", r"gmail.com", re.sub("(\[|\]| |\(|_|\.|#).*?(\]|\[| |\(|\)|_|\.|#)", "@", raw_email)))
        return correct_email
    else:
        correct_email = re.sub(".gmail.*", r"@gmail.com", raw_email)
        return correct_email
'''


# ひろきさんの問題を解くための関数↓↓↓↓
def correct_email_address(raw_email):
    correct_email = re.sub("@.*?@", "@", re.sub("gmail.*", r"gmail.com", re.sub("(\[|\]| |\(|_|\.|#).*?(\]|\[| |\(|\)|_|\.|#)", "@", raw_email)))
    return correct_email

'''
島田コメント

これはテストケースに対してだけうまく働くコードで、実際は使えませんね。
正しいとはいえません！

たとえば
gmaillover@gmail.com
みたいなメアドに対する出力が、gmail.com になってしまいます。

re.sub("gmail.*", r"gmail.com")
はバッドアイディアです。@前のgmailにも反応しますし、gmail以外にはもちろん使えないからです。

i_am_hiroki@gmail.com
みたいなメアドに対する出力も、i@gmail.comになっちゃいます。

また、問題設定には書いてませんでしたが現実問題gmailだけではないので、gmailという形を想定せずほかのドメイン hiroki@yahoo.co.jpみたいな形にも対応できるようにしましょう。


あと、無理して1行で書かなくても全然良いので、複数行でも見やすいコードで書きましょう。

'''


'''
def correct_email_address(raw_email):
    correct_email = re.sub("@.*?@", "@", re.sub("(\[|\]| |\(|_|\.|#).*?(\]|\[| |\(|\)|_|\.|#)", "@", re.sub(".gmail.*", r"@gmail.com", raw_email)))
    return correct_email
'''



# テスト用
def correct_email_address1(raw_email):
    correct_email = re.sub(".gmail.*", r"@gmail.com", raw_email)
    return correct_email


# どちらでもうまくいく
print(correct_email_address("showwin@gmail dot com"))

# 上しかうまくいかない
print(correct_email_address("showwin[at]gmail.com"))
print(correct_email_address("showwin at gmail.com"))
print(correct_email_address("showwin [at] gmail dot com"))
print(correct_email_address("showwin _at_ gmail [dot] com"))
print(correct_email_address("showwin _atmk_ gmail.com"))
print(correct_email_address("my-sirname on gmail"))
print(correct_email_address("sepeth + gmail.com"))

# 下しかうまくいかない
print(correct_email_address("psychedesire(gmail account)")) # >>> psychedesire@account)
print(correct_email_address("smihica_gmail_com")) # >>> smihica@com
print(correct_email_address("2tacatakataca2(gmail)")) # >>> 2tacatakataca2@
print(correct_email_address("mchachimituserver.gmail.com")) # >>> mchachimituserver@com
print(correct_email_address("linshao512#gmail.com")) # >>> linshao512@com
















####
