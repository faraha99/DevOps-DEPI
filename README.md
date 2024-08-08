

# Flask Web Application

This is a Flask web application that provides the current adjusted time and weather information for many countries. The weather information is fetched from the OpenWeatherMap API.

## Features

- Display the current adjusted time in Cairo, Egypt in the format YYYY-MM-DD HH:MM:SS (AM|PM).
- Provides weather information for Cairo, including the weather description and temperature.

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate.ps1`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:** Create a `.env` file in the root directory and add your OpenWeatherMap API key:

   ```bash
   API_KEY=<your_openweathermap_api_key>
   ```

## Running the Application

To run the application locally:

```bash
python3 app.py
```

To run the application using Docker:

1. **Build the Docker image:**

   ```bash
   docker build -f Containerfile -t flask-app .
   ```

2. **Run the Docker container:**

   ```bash
   docker run -p 5000:5000 flask-app
   ```

The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Running Tests

To run the tests and lint the application, use the following commands:

1. **Lint with pylint:**

   ```bash
   pylint app.py
   ```

2. **Run the tests:**

   ```bash
   pytest
   ```

## Project Structure

```
.
├── ansible/                 # Ansible directory
│   ├── ansible.yml          # Ansible playbook file
│   └── hosts                # Inventory file with target hosts
├── app.py                   # Main application file
├── Containerfile            # Dockerfile for building the application image
├── README.md                # Project documentation (this file)
├── requirements.txt         # Project dependencies
├── templates/               # Flask HTML templates
│   ├── index.html
│   └── timer_weather.html
```

## Ansible Deployment

To deploy the application using Ansible:

1. Ensure Ansible is installed on your local machine or deployment server.
2. Update `ansible/ansible.yml` with your deployment tasks.
3. Edit `ansible/hosts` to include the IP addresses or hostnames of your target servers.
4. Run Ansible against your target servers:

   ```bash
   ansible-playbook ansible/ansible.yml -i ansible/hosts
   ```

![Ansible Deployment](photos/ansible.jpg)

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to contribute to this project by submitting issues or pull requests.
