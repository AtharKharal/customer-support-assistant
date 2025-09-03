import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss

class Retriever:
    def __init__(self, data_path="data/faq.csv"):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.df = pd.read_csv(data_path)
        self.docs = self.df["answer"].tolist()
        self.questions = self.df["question"].tolist()

        embeddings = self.model.encode(self.docs)
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

    def search(self, query, k=1):
        q_emb = self.model.encode([query])
        distances, indices = self.index.search(q_emb, k)
        results = [(self.questions[i], self.docs[i]) for i in indices[0]]
        return results
