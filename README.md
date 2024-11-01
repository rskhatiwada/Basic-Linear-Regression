# SAT Score Predictor

This project is a simple web application built using Streamlit that predicts SAT scores based on student input.
The application loads a pre-trained linear regression model to estimate the SAT score.

## Features
- Simple and interactive web interface using Streamlit
- Predicts SAT scores based on user-provided input data
- Provides basic error handling for invalid input

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/sat-score-predictor.git
   cd sat-score-predictor
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   streamlit run enhanced_app.py
   ```

4. **Usage**:
   - Open the provided URL in your browser (usually `http://localhost:8501`).
   - Enter your data in the input field, and click "Submit" to see the prediction.

## Requirements
- Python 3.x
- Libraries: `streamlit`, `numpy`, `pickle`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
