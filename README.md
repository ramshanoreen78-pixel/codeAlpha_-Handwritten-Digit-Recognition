# Handwritten Digit Recognition App

A machine learning web app built with **Python**, **scikit-learn** and **Streamlit** that recognizes handwritten digits (0-9) from an uploaded image.

## Demo

Live app: _add your Streamlit Community Cloud link here after deploying_

## Features

- Upload a digit image (PNG / JPG)
- Image is converted to grayscale and resized to 28x28 pixels
- Model predicts the digit with a confidence score
- Simple and clean Streamlit interface

## Tech Stack

- Python 3
- scikit-learn
- NumPy, Pandas
- Pillow
- Streamlit

## Project Structure

```
.
├── app.py              # Streamlit app
├── model.pkl           # Trained model
├── requirements.txt    # Dependencies
└── README.md
```

## Installation

```bash
git clone https://github.com/ramshanoreen78-pixel/<your-repo-name>.git
cd <your-repo-name>
pip install -r requirements.txt
```

## Run Locally

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

## How to Use

1. Open the app.
2. Upload an image of a single digit (white digit on a black background works best, like MNIST samples).
3. View the predicted digit.

## requirements.txt (example)

```
streamlit
scikit-learn
numpy
pandas
pillow
```

## Deploy on Streamlit Community Cloud

1. Push this project to a GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Click **Create app**, select your repo, branch `main` and file `app.py`.
4. Click **Deploy**.

## Author

**Ramsha Noreen**
Machine Learning & Python Developer

- GitHub: [ramshanoreen78-pixel](https://github.com/ramshanoreen78-pixel)
- LinkedIn: [Ramsha Noreen](https://www.linkedin.com/in/ramsha-noreen-591159422)

## License

This project is for learning and portfolio purposes.