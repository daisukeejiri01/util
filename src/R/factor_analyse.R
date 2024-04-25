# 必要なパッケージのインストール
# if (!require(psych)) install.packages("psych", dependencies=TRUE)
# if (!require(ggplot2)) install.packages("ggplot2", dependencies=TRUE)

library(psych)
library(ggplot2)

# bfiデータセットの読み込み
data("bfi")

# データの一部を確認
head(bfi)

# 欠損データの除去
bfi_complete <- na.omit(bfi)

# 因子分析の実行
fa_result <- fa(bfi_complete[,1:25], nfactors=5, rotate="varimax")
print(fa_result)

# 因子負荷量の表示
loadings(fa_result)

# 因子得点の計算
factor_scores <- factor.scores(bfi_complete[,1:25], fa_result)

# 因子得点をデータフレームに追加
bfi_complete$Factor1 <- factor_scores$scores[,1]
bfi_complete$Factor2 <- factor_scores$scores[,2]
bfi_complete$Factor3 <- factor_scores$scores[,3]
bfi_complete$Factor4 <- factor_scores$scores[,4]
bfi_complete$Factor5 <- factor_scores$scores[,5]

# 新しいデータフレームの確認
head(bfi_complete)

# 因子スコアのプロット
ggplot(bfi_complete, aes(x=Factor1, y=Factor2)) +
  geom_point(alpha=0.5) +
  labs(x="Factor 1", y="Factor 2", title="Factor Analysis Results") +
  theme_minimal()