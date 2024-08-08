<<<<<<< HEAD


# Flask Web Application
=======
[![Build Status](https://github.com/terra-farm/terraform-provider-virtualbox/workflows/CI/badge.svg)](https://github.com/terra-farm/terraform-provider-virtualbox/actions?query=branch%3Amaster)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fterra-farm%2Fterraform-provider-virtualbox.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fterra-farm%2Fterraform-provider-virtualbox?ref=badge_shield)
[![Gitter](https://badges.gitter.im/terra-farm/terraform-provider-virtualbox.svg)](https://gitter.im/terra-farm/terraform-provider-virtualbox?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
>>>>>>> 2aabe91 (Initial commit)

# VirtualBox provider for Terraform

Inspired by [terraform-provider-vix](https://github.com/hooklift/terraform-provider-vix)

<<<<<<< HEAD
- Display the current adjusted time in Cairo, Egypt in the format YYYY-MM-DD HH:MM:SS (AM|PM).
- Provides weather information for Cairo, including the weather description and temperature.
=======
Donated to the `terra-farm` group by [`ccll`](https://github.com/ccll)
>>>>>>> 2aabe91 (Initial commit)

Published documentation is located on the [Terra-Farm website](https://terra-farm.github.io/provider-virtualbox/).

<<<<<<< HEAD
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
=======
# How to install

Installation instructions for the Terra-Farm thirdparty providers can be found on the 
[Terra-Farm website](https://terra-farm.github.io/main/installation.html)

# Usage

All usage documentation for the provider is published on the Terra-Farm website under
the section of the [VirtualBox provider](https://terra-farm.github.io/provider-virtualbox/index.html).

If you want to contribute documentation changes, see the [Contribution guide](CONTRIBUTING.md).

# Limitations
>>>>>>> 2aabe91 (Initial commit)

- Experimental provider!
- The defaults here are only tested with the [vagrant insecure (packer) keys](https://github.com/hashicorp/vagrant/tree/master/keys) as the login.

<<<<<<< HEAD
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
=======
## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fterra-farm%2Fterraform-provider-virtualbox.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fterra-farm%2Fterraform-provider-virtualbox?ref=badge_large)
>>>>>>> 2aabe91 (Initial commit)
