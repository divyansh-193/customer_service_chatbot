# Customer Service Chatbot

This repository contains a Streamlit application that implements a customer service chatbot using the `llama3` model provided by the `ollama` package. The chatbot is trained using a CSV file containing example input and response pairs and is designed to provide professional, humble, and precise customer service responses.

## Table of Contents
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setting up the Environment](#setting-up-the-environment)
  - [Installing Ollama](#installing-ollama)
- [Running the Application](#running-the-application)
- [Using the Chatbot](#using-the-chatbot)
- [File Structure](#file-structure)
- [License](#license)

## Installation

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.8 or higher
- pip (Python package installer)
- Compatible operating system (Linux or macOS)

### Setting up the Environment

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/customer-service-chatbot.git
    cd customer-service-chatbot
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Installing Ollama

1. **Install `ollama` CLI:**

   - **macOS:**
     ```bash
     brew install ollama
     ```

   - **Linux:**
     Follow the instructions on the [Ollama website](https://ollama.ai) for your specific Linux distribution.

2. **Download the `llama3` Model:**
    ```bash
    ollama pull llama3
    ```

3. **Install the `ollama` Python Package:**
    ```bash
    pip install ollama
    ```

## Running the Application

1. Prepare your training data in a CSV file named `prepared_data.csv` with the following structure:
    ```
    input,response
    "Hello, how can I help you?","Hi, I need assistance with my order."
    ```

2. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

3. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

## Using the Chatbot

1. Enter your prompt in the input box provided.
2. Press the "Send" button to get a response from the chatbot.
3. If you wish to exit the chat, type "exit" and press the "Send" button.

## File Structure

```plaintext
customer-service-chatbot/
├── prepared_data.csv       # CSV file containing training data
├── app.py                  # Main Streamlit application script
├── requirements.txt        # List of Python dependencies
└── README.md               # This README file
