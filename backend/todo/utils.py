from deep_translator import GoogleTranslator
from textblob import TextBlob


def traduzir_para_ingles(texto):
    if not texto:
        return ""

    try:
        return GoogleTranslator(source="pt", target="en").translate(texto)
    except Exception:
        return texto


def executar_nlp_raiz(texto):
    if not texto or not texto.strip():
        return "Sem Feedback", 0.0

    texto_en = traduzir_para_ingles(texto)
    blob = TextBlob(texto_en)
    polaridade = round(blob.sentiment.polarity, 4)

    if polaridade >= 0.3:
        sentimento = "Altamente Positivo / Construtivo"
    elif polaridade > 0.1:
        sentimento = "Positivo"
    elif polaridade <= -0.1:
        sentimento = "Negativo / Necessita de Atencao"
    else:
        sentimento = "Neutro / Orientacao Tecnica"

    return sentimento, polaridade
