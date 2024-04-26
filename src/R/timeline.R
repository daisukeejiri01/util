library(ggplot2)
library(lubridate)
library(dplyr)
library(showtext)

# データの作成
data <- data.frame(
  user_id = c("A", "A", "B", "C"),
  status = c("通常", "プレミアム", "通常", "プレミアム"),
  start = as.Date(c("2024-01-01", "2024-04-01", "2024-01-01", "2024-02-01")),
  end = as.Date(c("2024-03-31", NA, NA, NA))
)

# NAを今日の日付に置換
data$end[is.na(data$end)] <- as.Date("2024-04-30")

# showtextの自動設定を有効化
showtext_auto(enable = TRUE)

# フォントファミリーを追加（例：Hiragino Sans）
font_add("Hiragino", "ヒラギノ角ゴシック W3.ttc")

# タイムラインのプロット
ggplot(data, aes(x = start, xend = end, y = user_id, yend = user_id, color = status)) +
  geom_segment(linewidth = 10) +
  scale_color_manual(values = c("通常" = "blue", "プレミアム" = "red")) +
  labs(title = "タイムライン",
       x = "日付",
       y = "ユーザーID",
       color = "プラン") +
  theme_minimal() +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())

