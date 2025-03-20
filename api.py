from fastapi import FastAPI

app = FastAPI()

@app.post("/analyze/")
async def analyze_log(log: str):
    matched_ttps = search_ttp(log)
    results = []

    for ttp in matched_ttps:
        response = generate_ai_recommendation(ttp["name"], "MITRE description", "Apply EDR rules")
        results.append({"technique": ttp["name"], "recommendation": response})

    return {"detections": results}

# Run the API
# uvicorn filename:app --reload
