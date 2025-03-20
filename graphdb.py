from neo4j import GraphDatabase

# Connect to Neo4j
uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"

driver = GraphDatabase.driver(uri, auth=(username, password))

# Function: Insert TTP relationships into Neo4j
def add_attack_chain(tx, src_ttp, dst_ttp):
    query = """
    MERGE (a:TTP {id: $src_ttp})
    MERGE (b:TTP {id: $dst_ttp})
    MERGE (a)-[:LEADS_TO]->(b)
    """
    tx.run(query, src_ttp=src_ttp, dst_ttp=dst_ttp)

# Example: Define attack relationships
with driver.session() as session:
    session.write_transaction(add_attack_chain, "T1059", "T1203")  # PowerShell -> Exploitation
    session.write_transaction(add_attack_chain, "T1203", "T1071")  # Exploitation -> C2 Communication

print("✅ Attack chains stored in Neo4j")
