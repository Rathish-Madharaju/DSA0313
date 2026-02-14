from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = ["NLP is interesting.", "It is a field of AI."]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(text)

score = cosine_similarity(vectors[0], vectors[1])
print("Coherence Score:", score[0][0])
