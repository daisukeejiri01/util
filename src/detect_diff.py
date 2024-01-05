# check data versions diff

import pandas as pd

# data
# sample data frame
df1 = pd.DataFrame({"column1": [5, 1, 10],
                   "column2": [5, 1, 0]})
df2 = pd.DataFrame({"column1": [5, 1, 10],
                   "column3": [5, 1, 0],
                    "column4": [5, 1, 0]})

# CSVファイルを読み込む場合は以下のように変更して読み込めば良い
# df1 = pd.read_csv('sample1.csv')
# df2 = pd.read_csv('sample2.csv')

# 列名を取得する
columns1 = df1.columns.tolist()
columns2 = df2.columns.tolist()

# 列名の差分を取得する
removed_columns = list(set(columns1) - set(columns2))
added_columns = list(set(columns2) - set(columns1))

print("Removed columns: ", removed_columns)  # 削除されたカラム名
print("Added columns: ", added_columns)  # 追加されたカラム名
