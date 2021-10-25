import pandas as pd
from joblib import load
from fastapi import FastAPI
import re, string, mga_modelo
from pydantic import BaseModel


class Balita(BaseModel):
    balita: str


app = FastAPI()

LR = load("./modelo_dump/LR.bin")
DT = load("./modelo_dump/DT.bin")
RFC = load("./modelo_dump/RFC.bin")


@app.get("/")
def index():
    return {"mensahe": "dumirekta sa /docs"}


@app.post("/prediksyon")
def kunin_balita(balita: Balita):
    balitang_tutukuyin = {"balita": [balita.balita]}
    return prediktor(balitang_tutukuyin)


@app.get("/hula")
def kunin_kategorya(balita: str):
    balitang_tutukuyin = {"balita": [balita]}
    return prediktor(balitang_tutukuyin)

def prediktor(balita):
    panibagong_balitang_susuriin = pd.DataFrame(balita)
    panibagong_balitang_susuriin["balita"] = panibagong_balitang_susuriin[
        "balita"
    ].apply(linisin_pangungusap)
    x_panibagong_balitang_susuriin = panibagong_balitang_susuriin["balita"]
    susuriing_balita = mga_modelo.tfidf_vectorizer.transform(
        x_panibagong_balitang_susuriin
    )

    LR_resulta_kategorya = LR.predict(susuriing_balita)[0]
    DT_resulta_kategorya = DT.predict(susuriing_balita)[0]
    RFC_resulta_kategorya = RFC.predict(susuriing_balita)[0]

    LR_resulta_porsyento = round(LR.predict_proba(susuriing_balita)[0][1] * 100)
    DT_resulta_porsyento = round(DT.predict_proba(susuriing_balita)[0][1] * 100)
    RFC_resulta_porsyento = round(RFC.predict_proba(susuriing_balita)[0][1] * 100)

    average = round((LR_resulta_porsyento + DT_resulta_porsyento + RFC_resulta_porsyento) / 3)
    truth_table = (
        LR_resulta_kategorya == "TUNAY"
        and DT_resulta_kategorya == "TUNAY"
        and RFC_resulta_kategorya == "TUNAY"
    )
    husga = "TUNAY" if truth_table else "PEKE"

    return {
        "LR Prediksyon": LR_resulta_kategorya,
        "DT Prediksyon": DT_resulta_kategorya,
        "RFC Prediksyon": RFC_resulta_kategorya,
        "Husga": husga,
        "LR Porsyento": LR_resulta_porsyento,
        "DT Porsyento": DT_resulta_porsyento,
        "RFC Porsyento": RFC_resulta_porsyento,
        "Average ": average
    }

def linisin_pangungusap(nilalaman):
    nilalaman = nilalaman.lower()
    nilalaman = re.sub("\[.*?\]", "", str(nilalaman))
    nilalaman = re.sub("\\W", " ", str(nilalaman))
    nilalaman = re.sub("https?://\S+|www\.\S+", "", str(nilalaman))
    nilalaman = re.sub("<.*?>+", "", str(nilalaman))
    nilalaman = re.sub("[%s]" % re.escape(string.punctuation), "", str(nilalaman))
    nilalaman = re.sub("\n", "", str(nilalaman))
    nilalaman = re.sub("\w*\d\w*", "", str(nilalaman))
    return nilalaman
