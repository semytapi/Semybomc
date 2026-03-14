from fastapi import FastAPI, HTTPException
import requests
from apis import ULTIMATE_APIS

app = FastAPI()

API_KEY = "SEMY123"


@app.get("/api/semy")
def semy(key: str, number: str):

    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    responses = []

    try:

        for api in ULTIMATE_APIS:

            payload = api["data"](number)

            r = requests.request(
                method=api["method"],
                url=api["url"],
                headers=api["headers"],
                data=payload
            )

            responses.append({
                "name": api["name"],
                "status": r.status_code
            })

        return {
            "success": True,
            "number": number,
            "total": len(ULTIMATE_APIS),
            "responses": responses
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
