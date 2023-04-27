import re

# rを付けることを推奨。
# バックスラッシュをそのままで分かりやすいため。
# とりあえず緯度
content = '9'
# プラスの値のみ

# 経度
# 180度以下、かつ小数点はいくらでもOK
pattern1 = '^(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:\.\d+)?$|^(?:180)$'
# 緯度
pattern2 = '^(?:[0-9]|[1-8][0-9])(?:\.\d+)?$|^(?:90)$'

result = re.match(pattern2, content)

if result:  # none以外の場合
    print(result)
else:
    print('false')
