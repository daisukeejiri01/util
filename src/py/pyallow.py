import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# サンプルデータフレームの作成
# csv読み込みなど必要に応じて変更
data = {
    'column1': [1, 2, 3, 4],
    'column2': ['a', 'b', 'c', 'd'],
    'column3': [0.1, 0.2, 0.3, 0.4]
}
df = pd.DataFrame(data)

# Pandas DataFrameをApache Arrow Tableに変換
table = pa.Table.from_pandas(df)

# Parquetファイルに書き出し
file_name = "output"
pq.write_table(table, f'{file_name}.parquet')