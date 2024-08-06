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

Here's a section for your README file on how to make a `curl` request to interact with your Flask application. This section will guide users through making a `curl` request to your Flask API endpoint for predicting if an asteroid is potentially hazardous.

---

## How to Make a `curl` Request

To interact with the Asteroid Impact Prediction Tool API, you can use the `curl` command-line tool to send HTTP requests. Below are the steps and examples for making a `POST` request to the Flask application to get predictions.

### Prerequisites

Ensure that:
- The Flask application is running locally or is deployed on a server.
- `curl` is installed on your system. You can check this by running `curl --version` in your terminal.

### Sending a `POST` Request with `curl`

1. **Start the Flask Application**

   Make sure your Flask application is running. You should see output in your terminal indicating that Flask is serving the application, typically at `http://127.0.0.1:5000/`.

2. **Prepare the JSON Data**

   You need to send a JSON payload with the following fields:

   - `absolute_magnitude_h` (e.g., `25.0`)
   - `diameter_max_km` (e.g., `1.5`)
   - `velocity_km_s` (e.g., `20.0`)
   - `miss_distance_km` (e.g., `500000`)
   - `diameter_min_km` (e.g., `1.0`)

3. **Make the `curl` Request**

   Use the following `curl` command to send the data to the `/predict` endpoint:

   ```bash
   curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"absolute_magnitude_h": 25.0, "diameter_max_km": 1.5, "velocity_km_s": 20.0, "miss_distance_km": 500000, "diameter_min_km": 1.0}'
   ```

   - `-X POST` specifies that the request method is `POST`.
   - `-H "Content-Type: application/json"` sets the request header to indicate that the body content is JSON.
   - `-d '...'` contains the JSON payload with the asteroid features.

4. **View the Response**

   The response will be in JSON format and will indicate whether the asteroid is potentially hazardous. Example response:

   ```json
   {
     "is_potentially_hazardous_asteroid": true
   }
   ```

   If there is an error, the response will include an error message and a corresponding HTTP status code.

### Troubleshooting

- **Model Not Found**: If you get an error saying "Model not found," ensure that the `model.joblib` file is present in the `models/` directory and that the Flask application is correctly loading the model.
- **Missing Features**: If you receive an error about missing features, check that your JSON payload includes all the required fields with correct names and data types.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request on GitHub.

## Web Sources

- **[NeoWs (Near Earth Object Web Service)](http://neo.jpl.nasa.gov/)**: This service provides data about near-Earth asteroids, including their closest approach dates, lookup by specific IDs, and the ability to browse the dataset. It’s useful for accessing real-time asteroid information.

- **[Flask Documentation](https://flask.palletsprojects.com/)**: Comprehensive resource for learning Flask, the web framework used in this project.

- **[Scikit-learn Documentation](https://scikit-learn.org/stable/)**: Official documentation for Scikit-learn, the machine learning library utilized in this tool for creating and evaluating predictive models.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE.md) file for details.