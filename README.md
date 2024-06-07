# Flask Web Application

This is a Flask web application that provides the current adjusted time and weather information for Cairo, Egypt. The time is adjusted by subtracting one hour from the current time in Cairo, and the weather information is fetched from the OpenWeatherMap API.

## Features

- Display the current adjusted time in Cairo, Egypt in the format `YYYY-MM-DD HH:MM:SS (AM|PM)`.
- Provides weather information for Cairo, including the weather description and temperature.

## Setup and Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate.ps1`
    pip install -r requirements.txt # Install the dependencies
    ```

3. Set up environment variables: Create a `.env`` file in the root directory and add your OpenWeatherMap API key:

    ```bash
    API_KEY=<your_openweathermap_api_key>
    ```

## Running the Application

To run the application:
python3 app.py

To run the application using Podman, make sure you have Podman installed on your machine.

1. Build the Podman image:

    ```bash
    podman build -t flask-app .
    ```

2. Run the Podman container:

    ```bash
    podman run -p 5000:5000 --env-file .env flask-app
    ```

The application will be accessible at <http://127.0.0.1:5000/>.
## Managing Containers with Podman-Compose

This project uses Podman-Compose to manage the containers. Podman-Compose is a tool for defining and running multi-container Docker applications using Podman. It uses a `docker-compose.yml` file to configure the application's services.

### Installation

To install Podman-Compose, you can use the following steps:

1. Download the Podman-Compose binary for your system from the Podman GitHub releases page.

2. Extract the downloaded binary to a directory in your PATH, such as `/usr/local/bin`.

3. Ensure the Podman service is running.

### Usage

Once Podman-Compose is installed, you can use it to manage your containers. Here are some common commands:

- `podman-compose up`: Start the containers defined in the `docker-compose.yml` file.
- `podman-compose down`: Stop and remove the containers.
- `podman-compose ps`: List the running containers.

For more information and options, you can refer to the [Podman-Compose documentation](https://github.com/containers/podman-compose).


## Running Tests

To run the tests for the application, use the following command:

```bash
pytest
```

## Project Structure

```bash
.
├── app.py                  # Main application file
├── tests
│   └── test_app.py         # Test cases
├── templates
│   └── index.html
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── .env                    # Environment variables (not included in version control)
├── Containerfile           # Dockerfile for building the application image
└── docker-compose.yml      # Docker Compose configuration for running the application

```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to contribute to this project by submitting issues or pull requests.
