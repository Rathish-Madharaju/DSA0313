from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = ["NLP is fun", "I love NLP", "Machine learning"]
query = ["NLP"]

tfidf = TfidfVectorizer()
vectors = tfidf.fit_transform(docs + query)

scores = cosine_similarity(vectors[-1], vectors[:-1])
print(scores)
