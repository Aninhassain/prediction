# 🏠 Property Estimator - Advanced ML-Powered Real Estate Valuation

A sophisticated real estate price prediction web application built with Flask, machine learning, and modern web technologies. This project provides instant property valuations for Bangalore real estate using advanced machine learning algorithms.

## ✨ Features

- **🎯 ML-Powered Predictions**: Advanced linear regression model trained on real Bangalore housing data
- **🌐 Modern Web Interface**: Beautiful, responsive design with glass-morphism effects
- **📊 Real-time Valuation**: Instant price predictions based on property specifications
- **📍 Location Intelligence**: Support for 1200+ Bangalore locations
- **🎨 Professional UI**: Luxury home background with semi-transparent interface
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices



## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, NumPy, Pandas
- **Frontend**: HTML5, CSS3, JavaScript, jQuery
- **Data**: Bangalore House Prices Dataset
- **Deployment**: GitHub Pages / Heroku Ready

## 📋 Prerequisites

- Python 3.8+
- pip (Python package installer)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/property-estimator.git
cd property-estimator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python Server.py
```

### 4. Access the Application
Open your browser and navigate to: `http://127.0.0.1:5000`

## 📊 How It Works

### Model Training
The application uses a sophisticated machine learning pipeline:

1. **Data Preprocessing**: Cleans and validates Bangalore housing data
2. **Feature Engineering**: Extracts meaningful features from property data
3. **Model Training**: Linear regression with intelligent pricing logic
4. **Validation**: Cross-validation and outlier detection
5. **Deployment**: Model served via Flask API

### Prediction Features
- **Area (Square Feet)**: Total property area
- **BHK Configuration**: Number of bedrooms (1-5)
- **Bathroom Count**: Number of bathrooms (1-5)
- **Prime Location**: 1200+ Bangalore locations

## 🎯 Usage

1. **Enter Property Details**:
   - Input the total area in square feet
   - Select the number of BHK (bedrooms)
   - Choose the number of bathrooms
   - Pick the location from the dropdown

2. **Get Instant Valuation**:
   - Click "⚡ Get Instant Valuation →"
   - View the predicted price in Lakhs
   - Results include validation for realistic combinations

## 📁 Project Structure

```
property-estimator/
├── Server.py                 # Flask application server
├── util.py                   # ML model utilities and prediction logic
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── Bengaluru_House_Data.csv # Training dataset
├── templates/
│   └── app.html             # Main web interface
├── static/
│   ├── app.css              # Styling and animations
│   ├── app.js               # Frontend functionality
│   └── house.jpg            # Background image
├── artifacts/
│   ├── columns.json         # Model feature columns
│   └── banglore_home_prices_model.pickle # Trained ML model
└── images/
    └── house.jpg            # Additional assets
```

## 🔧 Model Details

### Training Data
- **Dataset**: Bangalore House Prices from Kaggle
- **Records**: 12,420+ validated property records
- **Features**: Area, BHK, Bathrooms, Location
- **Locations**: 1200+ unique Bangalore areas

### Model Performance
- **Algorithm**: Linear Regression with feature engineering
- **Validation**: Cross-validation and outlier detection
- **Accuracy**: Optimized for realistic property combinations
- **Features**: Intelligent pricing logic for edge cases

## 🌟 Key Features

### Smart Validation
- **Area per BHK validation**: Ensures realistic property configurations
- **Price range validation**: Filters out unrealistic predictions
- **Location validation**: Handles unknown locations gracefully

### Enhanced UI/UX
- **Glass-morphism design**: Modern semi-transparent interface
- **Responsive layout**: Works on all device sizes
- **Professional styling**: Luxury real estate aesthetic
- **Intuitive navigation**: Clear, user-friendly interface

## 🚀 Deployment

### Local Development
```bash
python Server.py
```

### Production Deployment
The application is ready for deployment on:
- **Heroku**: Add `Procfile` and configure environment variables
- **AWS**: Deploy using Elastic Beanstalk or EC2
- **Google Cloud**: Use App Engine or Compute Engine
- **Azure**: Deploy using App Service

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Dataset**: Bangalore House Prices from Kaggle
- **Inspiration**: Real estate valuation challenges
- **Technologies**: Flask, Scikit-learn, Modern Web Technologies

## 📞 Contact

- **Project Link**: [https://github.com/yourusername/property-estimator](https://github.com/yourusername/property-estimator)
- **Issues**: [GitHub Issues](https://github.com/yourusername/property-estimator/issues)

---

⭐ **Star this repository if you found it helpful!**
