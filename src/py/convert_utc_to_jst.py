# 必要なライブラリをインポート
import pandas as pd
from pytz import timezone

# データフレームを作成
df = pd.DataFrame({
    'day': ['2023-06-17 22:22:36', '2023-06-17 20:52:12']
})

# 文字列をdatetime型に変換
df['day'] = pd.to_datetime(df['day'])

# UTCをJSTに変換
df['day'] = df['day'].dt.tz_localize('UTC').dt.tz_convert('Asia/Tokyo')

# 新しいカラムを作成
df['date'] = df['day'].dt.date
df['month'] = df['day'].dt.to_period('M').dt.to_timestamp()
df['week'] = df['day'].dt.to_period('W-SUN').dt.to_timestamp()

# 結果を表示
print(df)