Classification API

Overview

This API takes a name and predicts its gender using the Genderize API. It grabs the data, processes the response, and sends back clear results with confidence levels and the current timestamp.

Base URL

https://api.genderize.io

Endpoint

Classify Name

GET /api/classify?name={name}

Example:

GET /api/classify?name=john

Response: Success (200 OK)

{
  "status": "success",
  "data": {
    "name": "john",
    "gender": "male",
    "probability": 0.99,
    "sample_size": 1234,
    "is_confident": true,
    "processed_at": "2026-04-12T10:00:00Z"
  }
}

Error Responses

400 Bad Request

Missing or empty name parameter:

{
  "status": "error",
  "message": "Missing or empty name parameter"
}

422 Unprocessable Entity

No prediction available for that name:

{
  "status": "error",
  "message": "No prediction available for the provided name"
}

500 or 502 Server Error

{
  "status": "error",
  "message": "Upstream or server failure"
}

Processing Details

The API fetches the following from Genderize:

- gender
- probability
- count (renamed as sample_size)

It sets is_confident to true if:

- probability is at least 0.7
- and sample_size is 100 or more

You’ll also get processed_at with the current UTC time in ISO format.

Tech Stack

- Python
- FastAPI
- HTTPX for async API requests


3. Try it locally:

http://127.0.0.1:8000/api/classify?name=john

CORS

CORS is turned on for all origins:

Access-Control-Allow-Origin: *

Project Structure

app/
├── main.py
├── routes/
├── services/
├── utils/

Performance

- Answers in under 500ms (not counting delays from external APIs)
- Uses async code to handle lots of requests smoothly

Testing

You can test it with:

- Postman
- A browser
- curl


For example:

curl "http://127.0.0.1:8000/api/classify?name=john"

Notes

- Make sure the server’s running before sending requests
- You need internet access for the external API



Nissi
