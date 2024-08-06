# Asteroid Impact Prediction Tool

## Overview

The **Asteroid Impact Prediction Tool** is a Flask-based web application that predicts whether a given asteroid is potentially hazardous to Earth using machine learning. The tool utilizes the **RandomForestClassifier** for prediction and leverages object serialization for model persistence. Data is sourced from the **NeoWs (Near Earth Object Web Service)**, a RESTful API providing comprehensive asteroid information.

## Features

- **Predict Hazardous Asteroids**: Input asteroid characteristics to predict if an asteroid is potentially hazardous.
- **Retrieve Asteroid Information**: Access asteroid data based on their closest approach date, ID lookup, or browse the overall dataset.
- **Object Serialization**: Use `joblib` to serialize and deserialize the trained model for efficient storage and retrieval.
- **User-Friendly Interface**: A responsive HTML interface for easy user interaction.

## Prerequisites

- **Python 3.x**: Make sure you have Python 3.9 or later installed.
- **Flask**: For web application development.
- **Scikit-Learn**: For machine learning tasks.
- **Pandas**: For data manipulation.
- **Requests**: For making HTTP requests to NeoWs API.
- **Joblib**: For model serialization.
- **Dotenv**: For environment variable management.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/joery0x3b800001/Asteroid-Impact-Prediction-Tool
   cd Asteroid-Impact-Prediction-Tool
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your NASA API key:

   ```plaintext
   API_KEY=your_nasa_api_key
   ```

## Project Structure

- `src/`
  - `app.py`: Contains the code that extracts data from NASA API.
  - `data_preprocessing.py`: Handles data preprocessing tasks.
  - `model_training.py`: Contains code to train and serialize the model.
- `asteroidApp/`
  - `app.py`: Contains the Flask application and API endpoints.
  - `templates/`
    - `index.html`: HTML interface for user input and prediction results.
  - `models/`
    - `model.joblib`: Serialized machine learning model (will be created after training).
- `requirements.txt`: Python dependencies.

## Running the Application

1. **Train the Model**

   Before running the application, ensure that the model is trained and serialized. Run the training script:

   ```bash
   python src/model_training.py
   ```

   This will generate `model.joblib` in the `models/` directory.

2. **Start the Flask Application**

   Run the Flask app:

   ```bash
   python asteroidApp/app.py
   ```

   The application will be available at `http://127.0.0.1:5000`.

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000`.
2. Enter the asteroid details in the form fields and click the **Predict** button.
3. The result will be displayed below the form, indicating whether the asteroid is potentially hazardous.

## API Endpoints

- **`/predict`**: Accepts a POST request with asteroid details and returns the prediction result.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE.md) file for details.

## Web Sources

- **[NeoWs (Near Earth Object Web Service)](http://neo.jpl.nasa.gov/)**: This service provides data about near-Earth asteroids, including their closest approach dates, lookup by specific IDs, and the ability to browse the dataset. It’s useful for accessing real-time asteroid information.

- **[Flask Documentation](https://flask.palletsprojects.com/)**: Comprehensive resource for learning Flask, the web framework used in this project.

- **[Scikit-learn Documentation](https://scikit-learn.org/stable/)**: Official documentation for Scikit-learn, the machine learning library utilized in this tool for creating and evaluating predictive models.
