# MinIO Deployment Guide

This guide describes how to deploy MinIO for local development using Docker and Kubernetes.

---

## 🐳 Docker Setup

### Requirements:
- Docker installed and running.

### Steps:

Run MinIO using Docker:

```bash
docker run -it -p 9000:9000 -p 9001:9001 quay.io/minio/minio server /data --console-address ":9001"
```

- MinIO Console UI will be available at:  
  `http://127.0.0.1:9001`
- S3 API endpoint will be available at:  
  `http://127.0.0.1:9000`
- Default credentials:
  - Access Key: `minioadmin`
  - Secret Key: `minioadmin`

---

## ☸️ Kubernetes Setup

### Requirements:
- kubectl installed
- kind installed
- k9s installed (for cluster management)

### Steps:

1. Create a kind cluster:

```bash
kind create cluster --name ml-in-production
```

2. Run k9s to monitor the cluster:

```bash
k9s -A
```

3. Deploy MinIO using Kubernetes manifest:

```bash
kubectl create -f minio_storage/minio-standalone-dev.yaml
```

---

## 🌐 Access MinIO UI and API via Port Forwarding

Forward ports to access MinIO Console and API:

```bash
kubectl port-forward --address=0.0.0.0 pod/minio 9000:9000
kubectl port-forward --address=0.0.0.0 pod/minio 9001:9001
```

- Access Console UI: `http://127.0.0.1:9001`
- Access S3 API: `http://127.0.0.1:9000`

> Note: See the related issue if you encounter problems accessing the UI via port-forward.

---

## 🔐 Default Credentials

- **Access Key:** `minioadmin`
- **Secret Key:** `minioadmin`

---

## 🛠️ S3 Access to MinIO via AWS CLI

You can interact with MinIO as if it were an S3 storage service.

1. Set environment variables:

```bash
export AWS_ACCESS_KEY_ID=minioadmin
export AWS_SECRET_ACCESS_KEY=minioadmin
export AWS_ENDPOINT_URL=http://127.0.0.1:9000
```

2. Perform S3 operations with AWS CLI:

```bash
aws s3 ls
aws s3api create-bucket --bucket test
aws s3 cp --recursive . s3://test/
```

---

## 🧪 MinIO Client Unit Tests

You can run unit tests for the MinIO client:

```bash
pytest -ss ./minio_storage/test_minio_client.py
```