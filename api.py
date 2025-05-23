from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from agents import pull_request


class ReviewRequest(BaseModel):
    user_message: str
app = FastAPI()

@app.post("/api/v1/review-pull-request")
async def review_pull_request(request: ReviewRequest):
    try:
        # Call the function to process the pull request
        response = await pull_request(request.user_message)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
