import faiss
import numpy as np

# Load saved embeddings
with open("mitre_embeddings.pkl", "rb") as f:
    mitre_ttp_embeddings = pickle.load(f)

# Convert to FAISS index
dimension = len(list(mitre_ttp_embeddings.values())[0][1])  # Vector size
index = faiss.IndexFlatL2(dimension)

# Store mapping of FAISS index to TTP IDs
id_to_ttp = {}
vectors = []

for i, (ttp_id, (name, vector)) in enumerate(mitre_ttp_embeddings.items()):
    vectors.append(vector)
    id_to_ttp[i] = ttp_id

index.add(np.array(vectors))  # Insert into FAISS index

# Function: Retrieve most similar TTP
def search_ttp(log_text, top_k=3):
    log_vector = embedder.encode(log_text).reshape(1, -1)
    distances, indices = index.search(log_vector, top_k)

    results = []
    for idx in indices[0]:
        ttp_id = id_to_ttp[idx]
        results.append({"technique_id": ttp_id, "name": mitre_ttp_embeddings[ttp_id][0]})

    return results

# Example Usage: Search for a log event
incident_log = "PowerShell script execution detected"
matched_ttps = search_ttp(incident_log)

print("\n🔹 Matched MITRE ATT&CK Techniques:")
for ttp in matched_ttps:
    print(f"{ttp['technique_id']} - {ttp['name']}")
