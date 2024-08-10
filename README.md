
# Flask Web Application

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


### **Project Structure**

```
.
├── ansible/                 
│   ├── ansible.yml          # Ansible playbook file
│   └── hosts                # Inventory file with target hosts
├── app.py                   # Main application file
├── Containerfile            # Dockerfile for building the application image
├── README.md                # Project documentation
├── requirements.txt         # Project dependencies
├── templates/               # Flask HTML templates
│   ├── index.html
│   └── timer_weather.html
├── alert.rules.yml          # Prometheus alerting rules
├── deployment.yml           # Kubernetes Deployment configuration
├── ingress.yml              # Kubernetes Ingress configuration
├── namespace.yml            # Kubernetes Namespace configuration
├── prometheus.yml           # Prometheus configuration
├── role.yml                 # Kubernetes Role-based access configuration
├── service.yml              # Kubernetes Service configuration
├── my-helm-chart/           # Helm chart directory
│   ├── charts               # Helm charts
│   ├── Chart.yaml           # Helm chart definition
│   ├── templates/          # Helm templates
│   └── values.yaml          # Helm values
├── CHANGELOG.md             # Change log for project updates
├── LICENSE                  # Project license information
├── myenv/                   # Python virtual environment
├── photos/                  # Project photos
├── __pycache__/             # Python bytecode cache
└── tests/                   # Test files and configurations
```

## System Architecture 
![system architecture](photos/system%20architecture%20.png)


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

## Minikube Deployment

To deploy the application using Minikube:

1. Start Minikube:

   ```bash
   minikube start
   ```

2. Ensure that your deployment YAML files (e.g., deployment.yml, service.yml, ingress.yml) are correctly configured. If you need to make any changes, apply them using:

   ```bash
   # Apply namespace
   kubectl apply -f namespace.yml

   # Deploy the application
   kubectl apply -f deployment.yml

   # Create the service
   kubectl apply -f service.yml

   # Set up ingress
   kubectl apply -f ingress.yml

   # Apply additional roles
   kubectl apply -f role.yml
   ```

## Monitoring and Visualization

To monitor and visualize your application using Prometheus and Grafana:

1. **Port forward Grafana and Prometheus services:**

   ```bash
   kubectl port-forward svc/grafana -n monitoring 3000:80
   kubectl port-forward svc/prometheus-server -n monitoring 9090:80
   ```

2. **Access Grafana at** [http://127.0.0.1:3000/](http://127.0.0.1:3000/) **and Prometheus at** [http://127.0.0.1:9090/](http://127.0.0.1:9090/).

![Grafana representation](photos/Grafana%20representation.jpeg)
![Prometheus representation](photos/Prometheus%20representation.jpeg)



## Helm Deployment

### Prerequisites

- Ensure Helm is installed on your system. For installation instructions, refer to the [Helm documentation](https://helm.sh/docs/intro/install/).
- Ensure `kubectl` is configured to interact with your Kubernetes cluster.

### Deploying the Application with Helm

1. **Add Helm Chart Repository (if not already added):**
   ```bash
   helm repo add my-repo https://example.com/helm-charts
   helm repo update
   ```

2. **Install the Helm Chart:**
   Replace `my-helm-chart` with the name of your chart directory if different.

   ```bash
   helm install my-flask-app my-helm-chart -f my-helm-chart/values.yaml -n devops-depi
   ```

   - `my-flask-app`: The name of the Helm release.
   - `my-helm-chart`: The path to your Helm chart directory.
   - `-f my-helm-chart/values.yaml`: Specifies the values file for configuration.
   - `-n devops-depi`: The namespace where the application will be deployed.

3. **Upgrade the Helm Chart:**
   If you need to update your Helm chart with new changes, use:

   ```bash
   helm upgrade my-flask-app my-helm-chart -f my-helm-chart/values.yaml -n devops-depi
   ```

4. **Uninstall the Helm Chart:**
   To remove the Helm release, use:

   ```bash
   helm uninstall my-flask-app -n devops-depi
   ```

### Kubernetes Commands

After deploying with Helm, you may need to use the following Kubernetes commands to manage and inspect your deployment:

1. **List Helm Releases:**
   ```bash
   helm list -n devops-depi
   ```

2. **Check the Status of Helm Release:**
   ```bash
   helm status my-flask-app -n devops-depi
   ```

3. **Get Kubernetes Pods:**
   ```bash
   kubectl get pods -n devops-depi
   ```

4. **Get Kubernetes Services:**
   ```bash
   kubectl get services -n devops-depi
   ```

5. **View Logs of a Specific Pod:**
   Replace `pod-name` with the name of the pod you want to inspect.
   ```bash
   kubectl logs pod-name -n devops-depi
   ```

6. **Port Forward to Access the Application Locally:**
   ```bash
   kubectl port-forward svc/devops-depi 5000:5000 -n devops-depi
   ```

7. **Describe a Specific Pod:**
   Replace `pod-name` with the name of the pod.
   ```bash
   kubectl describe pod pod-name -n devops-depi
   ```

### Helm Chart Configuration

The Helm chart configuration can be customized by editing the `values.yaml` file in the Helm chart directory. Key configuration options include:

- `replicaCount`: Number of replicas for the application.
- `image`: Docker image repository and tag.
- `service`: Configuration for the Kubernetes Service.
- `resources`: Resource requests and limits.
- `livenessProbe` and `readinessProbe`: Health check configurations.
- `ingress`: Ingress settings for external access.
- `autoscaling`: Auto-scaling configuration.

For a detailed explanation of each configuration option, refer to the `values.yaml` file in the Helm chart directory.


## License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to contribute to this project by submitting issues or pull requests.
=======
## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fterra-farm%2Fterraform-provider-virtualbox.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fterra-farm%2Fterraform-provider-virtualbox?ref=badge_large)
>>>>>>> 2aabe91 (Initial commit)
