# パッケージ無かったらインストール、
if (!require("pacman")) install.packages("pacman")

# library
pacman::p_load(UpSetR,
               tidyverse)

#データ例の作成
set.seed(777)
df <- data.frame(Group = paste0("Group", 1:100),
                       column1 = sample(0:1, 100, replace = TRUE),
                       column2 = sample(0:1, 100, replace = TRUE),
                       column3 = sample(0:1, 100, replace = TRUE),
                       column4 = sample(0:200, 100, replace = TRUE),
                       column5 = sample(100:300, 100, replace = TRUE))  

# upsetコマンド
upset(df)

#下にggplotをプロット
upset(df,
      attribute.plots =
        list(gridrows = 60, ncols = 2,
             plots = list(list(plot = scatter_plot, x = "Group", y = "column4"),
                          list(plot = scatter_plot, x = "Group", y = "column5"))))
                          
#sets.bar.color, sets, queriesオプション:グラフの色を指定
upset(df, sets.bar.color = "#56B4E9",
      attribute.plots = 
        list(gridrows = 60, ncols = 2,
             plots = list(list(plot = scatter_plot, x = "Group", y = "column4"),
                          list(plot = scatter_plot, x = "Group", y = "column5"))),
      sets = c("column1", "column2", "column3"),
      queries = list(list(query = intersects, params = list("column1"), active = FALSE),
                     list(query = intersects, params = list("column2"), active = TRUE)))
