# パッケージ無かったらインストール、
if (!require("pacman")) install.packages("pacman")
# library
pacman::p_load(tidyverse)

# dataset
set.seed(1)
sample_data <- data.frame(x = sample(LETTERS[c(10, 11, 12)],
                                  size = 100, replace = TRUE),
                       y = sample(1:100, size = 100,
                                  replace = TRUE),
                       Group = sample(LETTERS[2:3],
                                      size = 100,
                                      replace = TRUE))
 
# show.legendオプション
ggplot(sample_data, aes(x = x, y = y, fill = x)) +
  geom_boxplot(show.legend = FALSE)

# groupで塗色を分ける
ggplot(sample_data, aes(x = x, y = y, fill = Group)) +
  geom_boxplot()

# scale_fill_manual
ggplot(sample_data, aes(x = x, y = y, fill = x))+
  geom_boxplot() +
  scale_fill_manual(values = c("A" = "blue", "H" = "yellow"))

# geom_hline
ggplot(sample_data, aes(x = x, y = y, fill = x)) +
  geom_boxplot(show.legend = FALSE) +
  geom_hline(color = "red", alpha = 1,
             linewidth = 1,
             yintercept = mean(Box_data$y),
             show.legend = NA) 

# stat_summary
ggplot(sample_data, aes(x = x, y = y)) +
  geom_boxplot() +
  # 平均値にシンボルをプロット
  stat_summary(fun.y = "mean", geom = 'point',
               color = "red", shape = 16, size = 8) +
  # 平均値を線でつなげる
  stat_summary(aes(group = 1),
               fun.y = "mean", geom = 'line',
               color = "red", size = 2)

# coord_flip
ggplot(sample_data, aes(x = x, y = y)) +
  geom_boxplot() +
  # 平均値にシンボルをプロット
  stat_summary(fun.y = "mean", geom = 'point',
               color = "red", shape = 16, size = 8) +
  # 平均値を線でつなげる
  stat_summary(aes(group = 1),
               fun.y = "mean", geom = 'line',
               color = "red", size = 2) +
  # 横方向にする
  coord_flip()

# geom_dotplot()
ggplot(sample_data, aes(x = x, y = y)) +
  geom_boxplot() +
  # 平均値にシンボルをプロット
  geom_dotplot(binaxis = "y", stackdir = "center",
               binwidth = 2.5, fill = "red")

## Grouping
# fill options
ggplot(sample_data, aes(x = x, y = y, fill = Group)) +
  geom_boxplot()

# facet_wrap
ggplot(sample_data, aes(x = x, y = y)) +
  geom_boxplot() +
  facet_wrap(~Group)

## テキストを追加する
# coord_flipコマンドを使用します
ggplot(sample_data, aes(x = x, y = y)) +
  geom_boxplot() +
  annotate("text", x = 1, y = 110,
           label = "TEXT1", color = "red") +
  annotate("text", x = 2, y = 110,
           label = "TEXT2", color = "blue") +
  annotate("text", x = 3, y = 110,
           label = "TEXT3", color = "green") 