import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("datos/balita.csv")
mga_kategorya = df.kategorya
x_pagsasanay, x_pagsusuri, y_pagsasanay, y_pagsusuri = train_test_split(
    df["balita"], mga_kategorya, test_size=0.2, random_state=7
)

assert x_pagsasanay.shape[0] == y_pagsasanay.shape[0]

tfidf_vectorizer = TfidfVectorizer()
vectorizer_pagsasanay = tfidf_vectorizer.fit_transform(x_pagsasanay)
vectorizer_pagsusuri = tfidf_vectorizer.transform(x_pagsusuri)