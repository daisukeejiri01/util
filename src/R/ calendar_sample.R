# パッケージ無かったらインストール、
if (!require("pacman")) install.packages("pacman")

# library
pacman::p_load(lubridate,
               dplyr,
               zipangu)

# 2022年1月1日から今日までの日付を生成
dates <- seq(as.Date("2022-01-01"), Sys.Date(), by = "day")

# データフレームに変換
df <- data.frame(date = dates)

# 日付から曜日を取得（月曜が1、日曜が7になるようにoption変更）
options(lubridate.week.start = 1)
df <- df %>%
  mutate(day_of_week = wday(date))

# 土日のフラグ列を追加（土曜と日曜なら1、それ以外は0）
df <- df %>%
  mutate(is_weekend = ifelse(day_of_week >= 6, 1, 0))

# ここではis_holiday列をzipanguのis_jholidayを利用して取得
df <- df %>%
  mutate(is_holiday = ifelse(is_jholiday(date) == TRUE,1,0))

# is_offdayフラグ列を追加（is_weekendとis_holidayのどちらかが1なら1、それ以外は0）
df <- df %>%
  mutate(is_offday = ifelse(is_weekend == 1 | is_holiday == 1, 1, 0))

df %>%  tail(5)