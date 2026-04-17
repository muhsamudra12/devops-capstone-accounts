# Customer Account Project

This project is a microservice application for managing customer accounts, developed as part of the IBM DevOps and Software Engineering courses. The project includes a CI/CD implementation using Tekton and deployment to Kubernetes.

## Key Features
- Account data management (Name, Email, Address).
- Industry-standard unit testing.
- Statistical code analysis using Pylint and Flake8.
- Automated CI/CD pipeline with Tekton.
- Deployment to Kubernetes (K8s).

## Folder Structure
- `service/`: The main source code of the Python application.
- `test/`: A collection of unit tests.
- `k8s/`: Kubernetes manifest configuration (Deployment, Service, PVC, PipelineRun).
- `Dockerfile`: Configuration for building the container image.

## Code Quality
This application has been validated against the following quality standards:
- **Pylint Score**: 10.00/10
- **Flake8**: 0 errors (PEP 8 Compliant)

## Deployment to Kubernetes
To run the application locally on Kubernetes (Docker Desktop/Minikube):
1. Apply configuration: `kubectl apply -f k8s/`
2. Verification status: `kubectl get all`

## CI/CD Pipeline (Tekton)
The automated pipeline includes the following steps:
1. Linting (Pylint & Flake8)
2. Unit Testing
3. Building the Image
4. Deploy to the Cluster
