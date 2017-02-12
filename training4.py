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


def create_parameter_dict(s):
    s1 = s.replace(eliminate_parameters(s)+"?", "")  # "?"以降を切り取る
    s2 = s1.replace("&", ", ")
    # >> location=Tokyo, escore=3.0

    return dict(s2)

    # なんでこれでうまくいかないのかわかりません...


print(create_parameter_dict("http://scouty.co.jp/search?location=Tokyo&escore=3.0"))

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




'''
問題3は難しい！
がscoutyをコーディングするときに実際に直面する問題はもっと難しい！
この問題は候補者のメアド取ってくるとこでshowwinが実際に書きました　（ちなみに頑張れば1行で書ける）
'''
