import nltk
import spacy
import pandas as pd
import numpy as np
from textblob import TextBlob
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# 📌 1. Örnek Metin
metin = "Merhaba böcücüğüm! Bugün doğal dil işleme konusunu öğreneceğiz. NLP çok güçlü bir alandır."

# 📌 2. Tokenization (Kelime ve Cümle Ayrıştırma)
nltk.download("punkt")
kelimeler = word_tokenize(metin)
cumleler = sent_tokenize(metin)

print("🔹 Kelimeler:", kelimeler)
print("🔹 Cümleler:", cumleler)

# 📌 3. Stopwords (Gereksiz Kelimeleri Çıkarma)
nltk.download("stopwords")
stop_words = set(stopwords.words("turkish"))  # Türkçe stopwords kullanıyoruz
temiz_kelime_listesi = [kelime for kelime in kelimeler if kelime.lower() not in stop_words]

print("🔹 Temizlenmiş Kelimeler:", temiz_kelime_listesi)

# 📌 4. Lemmatization (Kelime Köküne İndirme)
nlp = spacy.load("en_core_web_sm")  # İngilizce için, Türkçe destekli model yok
doc = nlp("running jumped eating cars mice")

kelime_kokleri = [token.lemma_ for token in doc]
print("🔹 Lemmatization Sonucu:", kelime_kokleri)

# 📌 5. Duygu Analizi (Sentiment Analysis)
text_blob = TextBlob(metin)
print("🔹 Duygu Puanı:", text_blob.sentiment.polarity)  # -1 negatif, +1 pozitif

# 📌 6. Kelime Frekansı Analizi
kelime_frekansi = pd.Series(temiz_kelime_listesi).value_counts()
print("🔹 Kelime Frekansları:\n", kelime_frekansi)

