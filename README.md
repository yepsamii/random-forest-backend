# Random Forest Prediction API

This project provides a Flask-based API for making predictions using a trained Random Forest model.

## Getting Started (Docker)

### 1. Build the Docker image

```bash
docker build -t random-forest-api .
```

### 2. Run the Docker container

```bash
docker run -p 5000:5000 random-forest-api
```

The API will be available at `http://localhost:5000/`.

## API Endpoints

- `GET /` — Health check, returns a welcome message.
- `POST /predict` — Make a prediction. Send a JSON body with the following fields:
  - `age` (float)
  - `hypertension` (float or int)
  - `avg_glucose_level` (float)
  - `bmi` (float)
  - `heart_disease` (float or int)
  - `gender` (float or int)

#### Example request

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"age": 45, "hypertension": 0, "avg_glucose_level": 105.5, "bmi": 27.3, "heart_disease": 1, "gender": 1}'
```
