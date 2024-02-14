# library
library(dplyr)
library(purrr)

# sample 
data <- data.frame(
  date = c("2021/01/01", "2021/01/01", "2021/01/01", "2021/01/01", "2021/01/02", "2021/01/02", "2021/01/02"),
  id = c(1, 1, 2, 2, 1, 2, 2),
  score = c("A", "B", "A", "C", "A", "A", "D"),
  stringsAsFactors = FALSE # 文字列をファクターとして扱わない
)

# dplyrとpurrrを使用してデータを集約し、リスト形式でserviceを結合
# summriseでリストの長さを出力させる
result <- data %>%
  group_by(date, id) %>%
  summarise(scores = list(score), .groups = "drop") %>%
  summarise(counts = n(), .groups = "drop") %>%
  arrange(date, id)

# 結果
print(result)