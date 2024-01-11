# 必要なパッケージを読み込む
library(lubridate)
library(dplyr)

# データフレームを作成
df <- data.frame(
  day = as.POSIXct(c("2023-06-17 22:22:36", "2023-06-17 20:52:12"), tz = "UTC")
)

# UTCをJSTに変換し、新しいカラムを作成
df <- df %>%
  mutate(
    day_jst = with_tz(day, "Japan"),
    date = as.Date(day_jst,tz = "Japan"),
    month = floor_date(date, "month"),
    week = floor_date(date, "week")
  )