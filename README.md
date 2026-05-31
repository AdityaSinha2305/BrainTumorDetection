# 🧠 Brain Tumor Detection using CNN with Explainable AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow 2.12+](https://img.shields.io/badge/TensorFlow-2.12+-orange.svg)](https://www.tensorflow.org/)

A comprehensive web application for automated brain tumor detection from MRI images using deep learning models (CNN and MobileNet) with explainable AI capabilities. This project combines medical image analysis with interpretable machine learning to provide reliable and transparent predictions.

## 📋 Table of Contents

- [Features](#features)
- [Project Overview](#project-overview)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Models](#models)
- [Database Schema](#database-schema)
- [API Endpoints](#api-endpoints)
- [Results & Accuracy](#results--accuracy)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Dual Model Architecture**: Implements both CNN and MobileNet models for comparison and validation
- **Explainable AI**: Provides accuracy metrics, training history visualization, and model comparison charts
- **User Authentication**: Secure login/signup system with encrypted password storage
- **Patient Management**: Complete patient data management system with medical history
- **Real-time Predictions**: Fast MRI image analysis with instant results
- **Interactive Visualizations**: Training accuracy/loss plots and prediction visualizations
- **Responsive Web Interface**: User-friendly Flask-based web application
- **Database Integration**: MySQL database for persistent user and patient data storage

## 🎯 Project Overview

This project addresses the critical need for automated medical image analysis in detecting brain tumors. By leveraging deep learning and explainable AI, it provides:

1. **Automated Detection**: High-accuracy classification of MRI scans (healthy vs. tumor)
2. **Model Transparency**: Visual explanations of model decisions through training metrics
3. **Clinical Integration**: Professional interface suitable for medical environments
4. **Multi-Model Comparison**: Comparative analysis between CNN and MobileNet architectures

### Problem Statement
Early and accurate detection of brain tumors is crucial for patient outcomes. This application automates the detection process while maintaining transparency about model confidence and performance.

## 🛠️ Technology Stack

| Category | Technology |
|----------|-----------|
| **Backend** | Flask 2.2.3, Python 3.8+ |
| **Deep Learning** | TensorFlow 2.12.0, Keras 2.12.0 |
| **Database** | MySQL, SQLAlchemy |
| **Authentication** | Flask-Login, Werkzeug |
| **Data Processing** | NumPy, Pillow, scikit-image |
| **Visualization** | Matplotlib 3.7.1 |
| **Frontend** | HTML5, Jinja2 Templates |

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- MySQL Server installed and running
- Git
- Virtual Environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/AdityaSinha2305/BrainTumorDetection.git
cd BrainTumorDetection
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r reqiurements.txt
```

### Step 4: Download Pre-trained Models
Ensure the following model files are in the project root:
- `bestmodel.h5` - CNN model weights
- `bestmodelmobilenet.h5` - MobileNet model weights (included in repo)

## ⚙️ Configuration

### Database Configuration
Edit `main.py` and update the database connection string:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/database_name'
```

### Steps to Set Up MySQL:
```sql
CREATE DATABASE database_name;
USE database_name;

-- Tables will be auto-created by SQLAlchemy
```

### Flask Configuration
Update the secret key in `main.py`:
```python
app.secret_key = 'your_secret_key_here'
```

### Dataset Path
Update the image dataset path in `main.py` (line 205):
```python
path = "your_absolute_dataset_path" + filename
```

## 🚀 Usage

### Running the Application
```bash
python main.py
```

The application will be available at `http://localhost:5000`

### Application Workflow

1. **Sign Up**: Create a new user account
   - Enter username, email, and password
   - Password is encrypted before storage

2. **Login**: Access the application with your credentials

3. **Patient Registration**: Register patient details
   - First name, last name, age, gender
   - Date of visit and contact number
   - Email linked to user account

4. **Upload MRI Image**: Submit brain MRI scan
   - Select model (CNN or MobileNet)
   - Upload MRI image file

5. **View Results**: Get prediction and analysis
   - Classification (Healthy/Tumor)
   - Model accuracy percentage
   - Training history visualizations (Accuracy & Loss plots)
   - Input image preview

## 📁 Project Structure

```
BrainTumorDetection/
├── main.py                          # Flask application & routes
├── CNN.ipynb                        # CNN model training notebook
├── MobileNet.ipynb                  # MobileNet model training notebook
├── bestmodel.h5                     # CNN model weights
├── bestmodelmobilenet.h5            # MobileNet model weights
├── reqiurements.txt                 # Python dependencies
├── acc_cnn.txt                      # CNN model accuracy
├── acc_mn.txt                       # MobileNet model accuracy
├── h_cnn.txt                        # CNN training history (JSON)
├── h_mn.txt                         # MobileNet training history (JSON)
├── templates/                       # HTML templates
│   ├── index.html                   # Home page
│   ├── signup.html                  # Sign up page
│   ├── login.html                   # Login page
│   ├── patient.html                 # Patient registration
│   ├── image.html                   # Image upload
│   └── result.html                  # Prediction results
├── static/                          # Static files (CSS, JS, images)
└── README.md                        # This file
```

## 🤖 Models

### CNN Model
- **Architecture**: Custom Convolutional Neural Network
- **Input Size**: 224x224 pixels
- **Output**: Binary classification (Healthy/Tumor)
- **Activation**: ReLU (hidden), Sigmoid (output)
- **Optimizer**: Adam
- **Loss Function**: Binary Crossentropy

### MobileNet Model
- **Architecture**: Transfer Learning with MobileNetV2
- **Pre-training**: ImageNet weights
- **Fine-tuning**: Custom dense layers for binary classification
- **Advantages**: Lightweight, faster inference
- **Model Size**: ~13.5 MB

### Model Comparison
Both models are provided for comparison:
- **CNN**: Better accuracy on this specific dataset
- **MobileNet**: Faster inference, better for deployment

## 🗄️ Database Schema

### User Table
```sql
CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50),
    email VARCHAR(50) UNIQUE,
    password VARCHAR(1000)
);
```

### Patient Table
```sql
CREATE TABLE patient (
    pid INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(50),
    fname VARCHAR(15),
    lname VARCHAR(15),
    age INT,
    gender VARCHAR(10),
    date VARCHAR(50),
    id INT,
    number VARCHAR(10)
);
```

## 🔌 API Endpoints

| Route | Method | Authentication | Description |
|-------|--------|---|---|
| `/` | GET | No | Home page |
| `/signup` | GET, POST | No | User registration |
| `/login` | GET, POST | No | User login |
| `/logout` | GET | Yes | User logout |
| `/patient` | GET, POST | Yes | Patient registration |
| `/upload` | GET, POST | Yes | MRI image upload & prediction |
| `/deleteacc` | GET | Yes | Delete user account |

## 📊 Results & Accuracy

### Model Performance Metrics
- **CNN Accuracy**: Stored in `acc_cnn.txt`
- **MobileNet Accuracy**: Stored in `acc_mn.txt`

### Visualizations Provided
1. **Accuracy Plot**: Training vs. Validation Accuracy
2. **Loss Plot**: Training vs. Validation Loss
3. **Input Image Preview**: Display of uploaded MRI scan

These metrics help users understand model reliability and make informed decisions.

## 🔐 Security Features

- **Password Encryption**: Using werkzeug.security for hashed passwords
- **Session Management**: Flask-Login for secure user sessions
- **Login Required**: Protected routes prevent unauthorized access
- **SQL Injection Prevention**: Consider using parameterized queries (to be improved)

<!-- ## 📝 Notes & Future Improvements

1. **Migrate to ORM**: Replace raw SQL queries with SQLAlchemy ORM for security
2. **Data Augmentation**: Implement augmentation techniques for better model generalization
3. **Grad-CAM Visualization**: Add attention maps to show tumor location
4. **REST API**: Convert to REST API for better integration
5. **Containerization**: Docker setup for easy deployment
6. **Unit Tests**: Add comprehensive test coverage
7. **Model Versioning**: Implement model versioning and A/B testing
8. **Batch Processing**: Support for analyzing multiple images -->

## 📚 Training Notebooks

### CNN.ipynb
Contains the complete training pipeline for the custom CNN model:
- Data loading and preprocessing
- Model architecture definition
- Training with callbacks
- Model evaluation

### MobileNet.ipynb
Implements transfer learning using MobileNetV2:
- Feature extraction from pre-trained model
- Fine-tuning strategy
- Comparison with CNN results

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Aditya Sinha**
- GitHub: [@AdityaSinha2305](https://github.com/AdityaSinha2305)

## 📧 Contact & Support

For questions or issues, please open an issue on the [GitHub repository](https://github.com/AdityaSinha2305/BrainTumorDetection/issues).

## 🙏 Acknowledgments

- TensorFlow and Keras communities for excellent deep learning tools
- Flask framework for web development
- Medical imaging datasets used for model training
- Explainable AI research community

---

**⭐ If you find this project helpful, please consider giving it a star!**