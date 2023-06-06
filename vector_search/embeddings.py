import torch
from transformers import AutoTokenizer, AutoModel
import numpy as np
import faiss

class VectorSearch:
    def __init__(self, model_name='bert-base-uncased'):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name).to(self.device)

    def encode(self, texts):
        inputs = self.tokenizer(texts, padding=True, truncation=True, return_tensors="pt").to(self.device)
        with torch.no_grad():
            embeddings = self.model(**inputs).pooler_output
        return embeddings.cpu().numpy()

    def build_index(self, embeddings):
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

    def search(self, query_embeddings, k=5):
        distances, indices = self.index.search(query_embeddings, k)
        return distances, indices

if __name__ == "__main__":
    vector_search = VectorSearch()
    medical_records = ["Medical record 1", "Medical record 2", "Medical record 3"]
    embeddings = vector_search.encode(medical_records)
    vector_search.build_index(embeddings)
    query = ["New medical record"]
    query_embeddings = vector_search.encode(query)
    distances, indices = vector_search.search(query_embeddings)
    print(f"Top 5 similar medical records for '{query[0]}':", [medical_records[i] for i in indices[0]])
