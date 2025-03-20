from sentence_transformers import SentenceTransformer
import json

# Load MITRE ATT&CK Data
with open("enterprise-attack.json", "r") as f:
    mitre_data = json.load(f)

# Load a lightweight embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Extract techniques and generate embeddings
mitre_ttp_embeddings = {}
for obj in mitre_data["objects"]:
    if obj["type"] == "attack-pattern":
        ttp_id = obj["external_references"][0]["external_id"]
        ttp_name = obj["name"]
        ttp_desc = obj.get("description", "")

        # Generate embeddings
        vector = embedder.encode(f"{ttp_id} {ttp_name} {ttp_desc}")
        mitre_ttp_embeddings[ttp_id] = (ttp_name, vector)

# Save the embeddings for vector DB insertion
import pickle
with open("mitre_embeddings.pkl", "wb") as f:
    pickle.dump(mitre_ttp_embeddings, f)
