# 🐔 End-to-End Deep Learning Project: Chicken Disease Classification with MLOps

## 📌 Project Overview

This project is a production-ready Deep Learning application that classifies chicken diseases from feather images using Transfer Learning and MLOps best practices. The solution automates the complete machine learning lifecycle, from data ingestion and model training to deployment on cloud platforms such as AWS and Azure.

The project leverages:

- TensorFlow & Keras
- Transfer Learning (VGG16)
- DVC (Data Version Control)
- GitHub Actions (CI/CD)
- Docker
- Flask
- AWS & Azure Cloud Services

---

## 🚀 Features

✅ End-to-End Deep Learning Pipeline

✅ Automated Data Ingestion

✅ Transfer Learning with VGG16

✅ Model Training & Evaluation

✅ Flask Web Application

✅ DVC Pipeline Tracking

✅ GitHub Actions CI/CD

✅ Docker Containerization

✅ AWS Deployment (ECR + EC2)

✅ Azure Deployment (ACR + Web App)

---

## 🏗️ Project Architecture

```text
├── config/
├── artifacts/
│   ├── data_ingestion/
│   ├── prepare_base_model/
│   ├── training/
│   └── evaluation/
├── logs/
├── research/
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── config/
│   ├── entity/
│   ├── utils/
│   └── constants/
├── templates/
├── static/
├── app.py
├── main.py
├── params.yaml
├── config.yaml
├── dvc.yaml
├── Dockerfile
├── requirements.txt
└── .github/workflows/
```

---

## 🔄 Workflow

### 1. Data Ingestion
- Download chicken feather image dataset
- Extract and organize images
- Store data in artifact directory

### 2. Prepare Base Model
- Load pre-trained VGG16 model
- Freeze feature extraction layers
- Add custom classification layers

### 3. Prepare Callbacks
- Model checkpoints
- TensorBoard logging
- Training monitoring

### 4. Model Training
- Data preprocessing
- Data generators
- Fine-tuning and training

### 5. Model Evaluation
- Evaluate trained model
- Generate performance metrics
- Store results in JSON format

### 6. Prediction Pipeline
- Load trained model
- Preprocess user image
- Generate disease prediction

### 7. Web Application
- Upload chicken feather images
- Trigger predictions
- Display classification results

---

## 🧠 Model Details

| Parameter | Value |
|------------|---------|
| Model | VGG16 |
| Input Size | 224 × 224 × 3 |
| Framework | TensorFlow/Keras |
| Batch Size | 16 |
| Learning Method | Transfer Learning |
| Task | Binary Image Classification |

### Classes

- Healthy
- Coccidiosis Disease

---

## ⚙️ MLOps Implementation

### DVC (Data Version Control)

Used for:

- Dataset versioning
- Pipeline tracking
- Experiment reproducibility
- Dependency management

Pipeline stages:

```text
data_ingestion
prepare_base_model
model_training
model_evaluation
```

Run DVC pipeline:

```bash
dvc repro
```

Visualize pipeline:

```bash
dvc dag
```

---

## 🔄 CI/CD with GitHub Actions

Automated workflow:

1. Push code to GitHub
2. GitHub Actions triggered
3. Build Docker image
4. Run tests
5. Deploy to cloud environment

Workflow location:

```text
.github/workflows/main.yaml
```

---

## 🐳 Docker Deployment

Build Docker image:

```bash
docker build -t chicken-disease-classifier .
```

Run container:

```bash
docker run -p 8080:8080 chicken-disease-classifier
```

---

## ☁️ AWS Deployment

### Services Used

- AWS Elastic Container Registry (ECR)
- AWS EC2
- GitHub Actions

### Deployment Flow

```text
GitHub
   ↓
GitHub Actions
   ↓
Docker Build
   ↓
AWS ECR
   ↓
AWS EC2
   ↓
Application Running
```

---

## ☁️ Azure Deployment

### Services Used

- Azure Container Registry (ACR)
- Azure Web App for Containers

### Deployment Flow

```text
GitHub
   ↓
GitHub Actions
   ↓
Docker Build
   ↓
Azure Container Registry
   ↓
Azure Web App
```

---

## 🖥️ Web Application

The Flask-based web interface allows users to:

- Upload chicken feather images
- Predict disease status
- Trigger model retraining
- View results instantly

---

## 📊 Technologies Used

### Programming

- Python

### Deep Learning

- TensorFlow
- Keras

### MLOps

- DVC
- GitHub Actions

### Backend

- Flask

### Containerization

- Docker

### Cloud

- AWS
- Azure

### Utilities

- YAML
- Logging
- JSON
- TensorBoard

---

## 📈 Future Improvements

- Multi-class disease classification
- Hyperparameter tuning
- MLflow integration
- Kubernetes deployment
- Model monitoring and drift detection
- Automated retraining pipelines

---

## 🎯 Learning Outcomes

This project demonstrates:

- Deep Learning Pipeline Development
- Transfer Learning Implementation
- Production-Grade MLOps Practices
- CI/CD Automation
- Docker Containerization
- Cloud Deployment on AWS & Azure
- Software Engineering Best Practices for ML Systems

---

## 📷 Sample Application Workflow

```text
User Uploads Image
          ↓
Image Preprocessing
          ↓
Trained VGG16 Model
          ↓
Prediction
          ↓
Result Displayed on Flask UI
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## ⭐ Acknowledgements

This project follows an industry-standard MLOps workflow inspired by modern machine learning deployment practices and demonstrates how to take a Deep Learning model from experimentation to production.

---

## 📜 License

This project is licensed under the MIT License.
