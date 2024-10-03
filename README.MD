# Currency Exchange Application

This is a command-line application that converts an amount of currency from a base currency to a target currency using the latest exchange rates from the ExchangeRatesAPI. The application is designed to run in a Docker container and can be integrated with Jenkins for continuous integration and deployment.

## Features

- Fetches the latest currency exchange rates.
- Converts specified amounts from a base currency to a target currency.
- Docker support for easy deployment.
- Jenkins pipeline for automated builds and execution.

## Prerequisites

- Python 3.x
- `requests` library
- Docker
- Jenkins (optional, for CI/CD)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ADMichnik/Exchanger.git
   cd Exchanger
2. **Set up your API key:**

    Sign up at ExchangeRatesAPI to obtain your API key.

3. **Set your API key in your environment variables:**
   ```bash
   export API_KEY='your_api_key_here'

4. Docker Setup:

    Build the Docker image:
    ```bash 
   docker build -t currency-exchange-app .
5. Run the Docker container:

    You can run the container with the following command, replacing 1000, USD, and PLN with your desired values:
    ```bash 
    docker run -e API_KEY='your_api_key_here' currency-exchange-app -a 1000 -b USD -t PLN

## Usage
To run the application without Docker, you can use the following command:

    python main.py -a <amount> -b <base_currency> -t <target_currency>

Parameters:

-a or --amount: Amount of currency to convert (required).

-b or --base: Base currency code (e.g., USD, EUR) (required).

-t or --target: Target currency code (e.g., USD, EUR) (required).

Example

To convert 1000 USD to PLN, you would run:

    python main.py -a 1000 -b USD -t PLN

**Dockerfile**

The Dockerfile included in this project uses Python 3.9-slim as the base image and sets up the application environment.

**Jenkins Integration**

The included Jenkinsfile defines a pipeline that automates the process of building and running the application.

**Output**

The application will output the converted amount, rounded to two decimal places.

**License**

This project is licensed under the MIT License. See the LICENSE file for details.

**Acknowledgments**

ExchangeRatesAPI for providing the currency exchange rates.