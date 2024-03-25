# パッケージ無かったらインストール、
if (!require("pacman")) install.packages("pacman")

# Load required packages
pacman::p_load(lavaan,
               ggplot2)

# ライブラリを読み込む
library(lavaan)

# サンプルデータを作成する
data <- data.frame(
  x1 = rnorm(100),
  x2 = rnorm(100),
  x3 = rnorm(100)
)

# 共分散構造モデルを定義する
model <- '
    # 潜在変数
    latent_var1 =~ x1 + x2
    latent_var2 =~ x2 + x3

    # 相関
    latent_var1 ~~ latent_var2
'

# モデルを適合させる
fit <- sem(model, data = data)

# 結果を表示する
summary(fit)