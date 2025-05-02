from sentence_transformers import SentenceTransformer
import chromadb
from chromadb import PersistentClient

def main():
    # 1. Initialize embedding model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # 2. Sample text data
    documents = ["cat", "dog", "horse", "tree", "car", "ocean", "mountain", "river", "city", "computer"]

    # 3. Vectorize the text data
    embeddings = model.encode(documents).tolist()

    # 4. Initialize local VectorDB (Chroma)
    client = PersistentClient(path="./vector_db")


    collection = client.get_or_create_collection(name="example_collection")

    # 5. Add documents and embeddings to the collection
    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=[str(i) for i in range(len(documents))]
    )

    # 6. Example query: find vectors similar to the query text
    query = "laptop"
    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    print(f"\nQuery: {query}")
    print("Top results:")
    for doc in results['documents'][0]:
        print(f"- {doc}")

if __name__ == "__main__":
    main()
