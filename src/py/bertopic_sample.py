from bertopic import BERTopic
from transformers import pipeline
import numpy as np

# 日本語の文章データ
docs = [
    "富士山は日本一の山です。",
    "東京は日本の首都で、多くの人々が住んでいます。",
    "大阪は日本の食文化が豊かな都市です。",
    "京都は歴史的な建物が多いです。",
    "日本の経済は非常に強い。",
    "富士山周辺は自然が豊かで美しい。",
    "東京タワーは日本の有名な観光地の一つです。",
    "大阪でたこ焼きを食べるのが楽しみです。",
    "京都は古い寺院と神社が魅力的です。",
    "日本の技術は世界をリードしています。"
]

# 日本語のBERTモデルを用いたテキスト埋め込みの準備
embedding_model = pipeline("feature-extraction", model="cl-tohoku/bert-base-japanese", device=0)

# 文章をベクトルに変換する関数
def embed_documents(documents):
    embeddings = [embedding_model(doc)[0][0] for doc in documents]
    return np.array(embeddings)

# 文書の埋め込み
embeddings = embed_documents(docs)

# BERTopicのインスタンスを作成
topic_model = BERTopic(language="multilingual", calculate_probabilities=False, verbose=True)

# トピックモデリングを実行
topics, _ = topic_model.fit_transform(docs, embeddings)

# トピックとその文書を表示
for topic_num in set(topics):
    print(f"Topic {topic_num}:")
    for doc, topic in zip(docs, topics):
        if topic == topic_num:
            print(f" - {doc}")

# トピックごとの単語を表示
topic_info = topic_model.get_topic_info()
print(topic_info)