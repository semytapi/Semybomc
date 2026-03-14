from fastapi import FastAPI, HTTPException
import requests
import json

app = FastAPI()

API_KEY = "SEMY"

with open("semy.json") as f:
    config = json.load(f)

APIS = config["apis"]


@app.get("/api/semy")
def semy(key: str, number: str):

    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    responses = []

    try:

        for api in APIS:

            r = requests.request(
                method=api["method"],
                url=api["url"],
                headers=api["headers"],
                json={"number": number}
            )

            responses.append({
                "name": api["name"],
                "status": r.status_code
            })

        return {
            "success": True,
            "number": number,
            "total": len(APIS),
            "responses": responses
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
