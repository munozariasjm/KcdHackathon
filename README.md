
# Decentralized Medical Records System (DeMeRS)
---


By: Jose M Munoz
KCD Colombia 2023

This little project proposal for **KCD Colombia 2023's hackathon** aims to provide a secure, interoperable, and efficient system for managing patient medical records. We utilize Blockchain for secure and decentralized data storage, Kubernetes for scalable deployment, and large language models (LLMs) with vector search to help healthcare providers (all along the world) find similar cases and their treatment.

This would be a great solution for optimizing the healthcare system in Colombia for the variety of health suppliers, and it could be easily adapted to other countries.

## Table of Contents

- [Decentralized Medical Records System (DeMeRS)](#decentralized-medical-records-system-demers)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Installation \& Setup](#installation--setup)
  - [Usage](#usage)
  - [Testing](#testing)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contributors](#contributors)

## Project Structure

```bash
/project
    /blockchain
        /chaincode
            medicalrecords_cc.py
        docker-compose.yaml
    /api
        app.py
        requirements.txt
        Dockerfile
    /kubernetes
        api-deployment.yaml
        api-service.yaml
    /vector_search
        embeddings.py
        Dockerfile
    /ui
        index.html
    /tests
        test_medicalrecords.py
        test_api.py
        test_embeddings.py
```

## Installation & Setup

1. **Clone the repository**
```
git clone https://github.com/munozariasjm/DeMeRS.git
cd project
```

2. **Build and start the blockchain network**

Navigate to the `blockchain` directory and start the network using Docker Compose.
```
cd blockchain
docker-compose up -d
```

3. **Build and deploy the API service**

In the `api` directory, build the Docker image and deploy it using Kubernetes.
```
cd ../api
docker build -t api:1.0 .
kubectl apply -f ../kubernetes/api-deployment.yaml
kubectl apply -f ../kubernetes/api-service.yaml
```

4. **Build and deploy the vector search service**

Similarly, in the `vector_search` directory, build the Docker image and deploy it using Kubernetes.
```
cd ../vector_search
docker build -t vector-search:1.0 .
kubectl apply -f ../kubernetes/vector-search-deployment.yaml
kubectl apply -f ../kubernetes/vector-search-service.yaml
```

5. **Access the UI**

Open `ui/index.html` in your web browser.

## Usage

The system provides an API for adding and retrieving medical records, and a user interface for interacting with the API.

## Testing

Work in progress

## Contributing

Contributions are welcome. Please submit a pull request, or create an issue for any bugs or feature requests.

## License

This project is licensed under the terms of the MIT license.

## Contributors

[munozariasjm](https://github.com/munozariasjm)