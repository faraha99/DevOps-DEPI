# Flask Web Application

This is a Flask web application that provides the current adjusted time and weather information for many countries. The weather information is fetched from the OpenWeatherMap API.

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
    source venv/bin/activate  # On Windows use `venv\Scripts\activate.ps1`
    pip install -r requirements.txt  # Install the dependencies
    ```

3. Set up environment variables: Create a `.env` file in the root directory and add your OpenWeatherMap API key:

    ```bash
    API_KEY=<your_openweathermap_api_key>
    ```

## Running the Application

To run the application:

```bash
python3 app.py
To run the application using Podman, make sure you have Podman installed on your machine.

Build the Podman image:
bash

podman build -t flask-app .
Run the Podman container:
bash

podman run -p 5000:5000 flask-app
The application will be accessible at http://127.0.0.1:5000/.

Running Tests
To run the tests for the application, use the following command:

bash

pytest
Project Structure
bash

.
├── ansible/                # Ansible directory
│   ├── ansible.yml         # Ansible playbook file
│   ├── deploy.yml          # Example deployment playbook (if applicable)
│   ├── hosts               # Inventory file with target hosts
│   └── ansible-env/        # Ansible environment (roles, group_vars, etc.)
├── app.py                  # Main application file
├── Containerfile           # Podman file for building the application image
├── README.md               # Project documentation (this file)
├── requirements.txt        # Project dependencies
├── templates/              # Flask HTML templates
│   ├── index.html
│   └── timer_weather.html
├── main.tf             # Terraform main configuration file
├── variables.tf        # Terraform variables file

Ansible Deployment
To deploy the application using Ansible:

Ensure Ansible is installed on your local machine or deployment server.
Update ansible/ansible.yml with your deployment tasks.
Edit ansible/hosts to include the IP addresses or hostnames of your target servers.
Run Ansible against your target servers:
bash

ansible-playbook ansible/ansible.yml -i ansible/hosts
Terraform Infrastructure Provisioning
To provision infrastructure for the application using Terraform:

![WhatsApp Image 2024-07-12 at 17 52 53_2597bab7](https://github.com/user-attachments/assets/cee0e4ca-3bf6-4868-8a4d-1b31dac260be)



Initialize Terraform:
bash

terraform init
Review and apply the Terraform configuration:
bash

terraform apply

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to contribute to this project by submitting issues or pull requests.
