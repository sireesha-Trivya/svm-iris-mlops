# 🌸 SVM Iris Classification MLOps Project

An end-to-end Machine Learning project that classifies Iris flowers into **Setosa**, **Versicolor**, or **Virginica** using a **Support Vector Machine (SVM)** model. The application exposes a REST API built with **FastAPI**, is containerized using **Docker**, and was successfully deployed on an **AWS EC2** instance.

---

# 📌 Project Overview

This project demonstrates a complete MLOps workflow, including:

- Data preprocessing
- Model training using Support Vector Machine (SVM)
- Model serialization using Joblib
- REST API development with FastAPI
- Automatic API documentation using Swagger UI
- Docker containerization
- AWS EC2 deployment

The API accepts Iris flower measurements and predicts the corresponding species.

---

# 🛠 Tech Stack

- Python 3
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Uvicorn
- Docker
- AWS EC2
- Git & GitHub

---

# 📂 Project Structure

```
svm-iris-mlops/
│
├── app/
│   └── app.py
│
├── model/
│   ├── train.py
│   └── svm_model.joblib
│
├── data/
│   └── iris.csv
│
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

---

# 📊 Dataset

The project uses the classic **Iris Dataset**, which contains measurements of iris flowers.

### Features

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

### Target Classes

- Setosa
- Versicolor
- Virginica

---

# 🤖 Model Training

The training script performs the following steps:

- Loads the Iris dataset
- Splits the data into training and testing sets
- Trains an SVM classifier
- Evaluates model performance
- Saves the trained model as:

```
model/svm_model.joblib
```

---

# 🚀 FastAPI Application

The FastAPI application provides REST endpoints for predictions.

### Available Endpoints

### Home

```
GET /
```

Response

```json
{
  "status": "Running",
  "model": "Support Vector Machine",
  "version": "1.0.0"
}
```

---

### Health Check

```
GET /health
```

Response

```json
{
  "status": "Healthy"
}
```

---

### Prediction

```
POST /predict
```

Sample Request

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Sample Response

```json
{
  "class_id": 0,
  "prediction": "Setosa"
}
```

---

# 📖 Interactive API Documentation

FastAPI automatically generates API documentation.

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# 🐳 Dockerization

## Build Docker Image

```bash
docker build -t svm-iris-mlops:v1 .
```

## Run Docker Container

```bash
docker run -d -p 8000:8000 svm-iris-mlops:v1
```

Open the API

```
http://localhost:8000
```

---

# ☁️ AWS EC2 Deployment

This project was successfully deployed on an AWS EC2 instance using Docker.

Deployment workflow:

- Launch EC2 instance
- Install Docker
- Clone the GitHub repository
- Build Docker image
- Run Docker container
- Access the FastAPI application using the EC2 public IP

Example

```
http://<EC2-PUBLIC-IP>:8000/docs
```

> **Note:** The EC2 instance used for deployment has been terminated after successful validation to optimize cloud resource usage and avoid unnecessary costs.

---

# ▶️ Running Locally

Clone the repository

```bash
git clone https://github.com/Siri-Trivya/svm-iris-mlops.git
```

Move into the project

```bash
cd svm-iris-mlops
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start the application

```bash
uvicorn app.app:app --host 0.0.0.0 --port 8000 --reload
```

Open

```
http://localhost:8000/docs
```

---

# 🧪 Testing the API

You can test the API using:

- Swagger UI
- Postman
- curl
- Thunder Client (VS Code)

Example curl request

```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{
"sepal_length":5.1,
"sepal_width":3.5,
"petal_length":1.4,
"petal_width":0.2
}'
```

---

# 📷 Project Demo

Application Flow

```
User
   │
   ▼
FastAPI REST API
   │
   ▼
SVM Model
   │
   ▼
Predicted Iris Species
```

Replace this section with screenshots of:

- Swagger UI
- Health endpoint
- Prediction response
- Docker container running
- EC2 deployment (optional)

---

# 🚀 Future Improvements

- CI/CD pipeline using Jenkins
- Kubernetes deployment
- Model versioning with MLflow
- Monitoring with Prometheus & Grafana
- Unit and integration testing
- GitHub Actions workflow
- Request logging and metrics

---

# 🎯 Key Learning Outcomes

- Machine Learning model training
- Support Vector Machine classification
- FastAPI REST API development
- Pydantic request validation
- Docker containerization
- AWS EC2 deployment
- API documentation with Swagger
- End-to-end MLOps workflow

---

# 👩‍💻 Author

**Sireesha Buddha**

If you found this project useful, consider giving it a ⭐ on GitHub.
