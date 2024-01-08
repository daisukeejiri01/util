# import library
from datetime import datetime
import pandas as pd
import jpholiday

# 現在の日付を取得
today = datetime.today().strftime('%Y-%m-%d')

# 任意の日付（今回は仮で2022年1月1日）から今日までの日付を生成しデータフレームに変換
dates = pd.date_range(start='2022-01-01', end=today)
df = pd.DataFrame(dates, columns=['date'])

# 日付から曜日を取得（月曜が0、日曜が6）
df['day_of_week'] = df['date'].dt.dayofweek

# 土日のフラグ列を追加（土曜と日曜なら1、それ以外は0）
df['is_weekend'] = df['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)

# 祝日のフラグ列を追加（祝日なら1、それ以外は0）
df['is_holiday'] = df['date'].map(jpholiday.is_holiday).astype(int)

# 休日列を追加（土曜と日曜もしくは祝日なら1、それ以外は0）
df['is_offday'] = df.apply(lambda row: 1 if row['is_weekend'] == 1 or row['is_holiday'] == 1 else 0, axis=1)

print(df)