import pandas as pd
from joblib import dump
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
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

LR = LogisticRegression()
LR.fit(vectorizer_pagsasanay, y_pagsasanay)
pred_lr = LR.predict(vectorizer_pagsusuri)
LR.score(vectorizer_pagsusuri, y_pagsusuri)
iskor = accuracy_score(y_pagsusuri, pred_lr)
print(classification_report(y_pagsusuri, pred_lr))
print(f"Katumpakan: {round(iskor*100,2)}%")

DT = DecisionTreeClassifier()
DT.fit(vectorizer_pagsasanay, y_pagsasanay)
pred_dt = DT.predict(vectorizer_pagsusuri)
DT.score(vectorizer_pagsusuri, y_pagsusuri)
iskor = accuracy_score(y_pagsusuri, pred_dt)
print(classification_report(y_pagsusuri, pred_dt))
print(f"Katumpakan: {round(iskor*100,2)}%")

RFC = RandomForestClassifier(random_state=0)
RFC.fit(vectorizer_pagsasanay, y_pagsasanay)
pred_rfc = RFC.predict(vectorizer_pagsusuri)
RFC.score(vectorizer_pagsusuri, y_pagsusuri)
iskor = accuracy_score(y_pagsusuri, pred_rfc)
print(classification_report(y_pagsusuri, pred_rfc))
print(f"Katumpakan: {round(iskor*100,2)}%")

dump(LR, "./modelo_dump/LR.bin")
dump(DT, "./modelo_dump/DT.bin")
dump(RFC, "./modelo_dump/RFC.bin")