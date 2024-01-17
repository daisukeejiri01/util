# check data versions diff

import pandas as pd
from datetime import datetime, timedelta, timezone

# variables
JST = timezone(timedelta(hours=+9), 'JST')
d = datetime.now(JST)
YYYYMMDD = '{0:%Y%m%d}'.format(d)
form = "test"
output_file = "output"
old_version = "version_x"
new_version = "version_y"

# data
# sample data frame
sample_data1 = {
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': [7, 8, 9]
}
sample_data2 = {
    'a': [10, 11, 12],
    'b': [13, 14, 15],
    'd': [16, 17, 18],
    'e': [19, 20, 21]
}

df_sample1 = pd.DataFrame(sample_data1)
df_sample2 = pd.DataFrame(sample_data2)

# CSVファイルを読み込む場合は以下のように変更して読み込めば良い
# df1 = pd.read_csv('sample1.csv')
# df2 = pd.read_csv('sample2.csv')

# カラムの差分を取得
removed_columns = set(df_sample1.columns) - set(df_sample2.columns)
added_columns = set(df_sample2.columns) - set(df_sample1.columns)

# 削除されたカラムと追加されたカラムのDataFrameを作成
removed_columns_df = pd.DataFrame({'削除されたカラム': list(removed_columns)})
added_columns_df = pd.DataFrame({'追加されたカラム': list(added_columns)})


# 新しいExcelファイルを作成
with pd.ExcelWriter(f'{YYYYMMDD}_{form}_{output_file}.xlsx', engine='openpyxl') as writer:
    # サンプル1のカラムを出力
    columns_df1 = pd.DataFrame({'id': range(1, len(df_sample1.columns) + 1),
                                'column': df_sample1.columns})
    columns_df1.to_excel(writer, sheet_name= old_version, index=False)
    
    # サンプル2のカラムを出力
    columns_df2 = pd.DataFrame({'id': range(1, len(df_sample2.columns) + 1),
                                'column': df_sample2.columns})
    columns_df2.to_excel(writer, sheet_name= new_version, index=False)
    
    # 削除されたカラムを出力
    if not removed_columns_df.empty:
        removed_columns_df.to_excel(writer, sheet_name='削除されたカラム一覧', index=False)
        print("Removed columns: ", removed_columns)
    
    # 追加されたカラムを出力
    if not added_columns_df.empty:
        added_columns_df.to_excel(writer, sheet_name='追加されたカラム一覧', index=False)
        print("Added columns: ", added_columns)

print("process:success")