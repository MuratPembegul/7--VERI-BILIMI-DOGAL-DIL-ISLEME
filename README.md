# 7--VERI-BILIMI-DOGAL-DIL-ISLEME

# 📝 Doğal Dil İşleme (Natural Language Processing - NLP) README

## 📌 Giriş (Introduction)
Doğal Dil İşleme (NLP), bilgisayarların insan dilini anlaması, analiz etmesi ve yorumlaması için geliştirilen bir yapay zeka alanıdır.
Bu alan, dil modeli oluşturma, metin madenciliği, duygu analizi ve çeviri gibi birçok uygulamayı kapsar. 🤖📚

Bu repo, Python kullanarak NLP uygulamaları yapmanın temel yollarını öğrenmen için hazırlandı. 🚀

---

## 🚀 Kurulum (Installation)
NLP projelerinde kullanılan temel kütüphaneleri yüklemek için:

```bash
pip install nltk spacy textblob transformers gensim scikit-learn pandas numpy
```

Ayrıca **spaCy** modelini indirmek için:
```bash
python -m spacy download en_core_web_sm
```

---

## 🔥 Kullanılan Kütüphaneler (Libraries Used)

1. **NLTK** 📚 - Doğal dil işleme için temel işlemler.
2. **spaCy** 🚀 - Hızlı ve etkili metin işleme.
3. **TextBlob** 📝 - Basit duygu analizi ve dil işleme.
4. **Transformers (Hugging Face)** 🤖 - Gelişmiş derin öğrenme tabanlı modeller.
5. **Gensim** 🔍 - Konu modelleme ve kelime benzerlik analizleri.
6. **Scikit-Learn** 📊 - Makine öğrenmesi ile metin sınıflandırma.

---

## 🏗️ Örnek Kullanım (Examples)

### 📌 Basit Tokenizasyon (NLTK Kullanarak)
```python
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

text = "Merhaba, NLP dünyasına hoşgeldiniz!"
tokens = word_tokenize(text)
print(tokens)  # ['Merhaba', ',', 'NLP', 'dünyasına', 'hoşgeldiniz', '!']
```

### 🎨 spaCy ile Kelime Tabanlı Analiz
```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Natural Language Processing is fascinating!")

for token in doc:
    print(token.text, token.lemma_, token.pos_)  # Kelime, kök, kelime türü
```

### 🤖 Hugging Face Transformers ile Metin Tahmini
```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("I love NLP and AI!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.9998}]
```

---

## 📚 Ek Kaynaklar (Additional Resources)
- [NLTK Resmi Dokümanı](https://www.nltk.org/)
- [spaCy Resmi Dokümanı](https://spacy.io/)
- [TextBlob Dokümanı](https://textblob.readthedocs.io/en/dev/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Gensim Dokümanı](https://radimrehurek.com/gensim/)

---

## 📌 Katkı Yapma (Contributing)
Projeye katkıda bulunmak ister misiniz? Forklayın, geliştirin ve bir PR gönderin! 🚀

---

## 📜 Lisans (License)
Bu proje MIT lisansı altında sunulmaktadır. Serbestçe kullanabilirsiniz! 😊

