import json

import uvicorn
from fastapi import FastAPI

app = FastAPI()

names = ["mum_key", "mum_uuid", "months_pregnant", "expected_delivery_date", "antenatal_prenatal", "facility", "intent", "priority", "survey_name", "survey_question_text", "mum_response_answer", "updated_survey_question_text", "mum_open_response_answer"]
# from db_conn import recs

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/info")
async def root():
    _lst = []
    for rec in names:
        dct = {}
        for i, field in enumerate(names):
            dct[field] = str(rec.get(i))
        _lst.append(dct)
    return json.dumps(_lst)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug", debug=True,
                workers=1, limit_concurrency=1, limit_max_requests=1)
