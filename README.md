# Stock Service with OTEL Instrumentation

[![pipeline status](https://gitlab.com/sa-demo-group/ben-bertka-demo-group/stock-service/badges/main/pipeline.svg)](https://gitlab.com/sa-demo-group/ben-bertka-demo-group/stock-service/-/commits/main)

## Overview

This Flask-based application allows users to fetch real-time stock prices from Yahoo Finance. It is designed to showcase advanced CI/CD practices using GitLab's Auto DevOps and Kubernetes for orchestration.

## Features

- **Real-Time Stock Prices**: Users can enter stock symbols to get current prices.
- **Responsive Interface**: User-friendly web interface suitable for all devices.

## Technology Stack

- **Flask**: Back-end web framework.
- **yFinance**: Library to fetch stock data from Yahoo Finance.
- **jQuery**: For dynamic front-end interactions.

## Getting Started

### Prerequisites

- Python 3.8+
- Docker
- Kubernetes CLI (kubectl)
- GitLab account with CI/CD capabilities


## CI/CD Pipeline Using GitLab Auto DevOps

This project utilizes GitLab Auto DevOps for continuous integration and delivery, automating the lifecycle from build to deployment:

### Pipeline Stages

- **Build**: Constructs the Docker image from the Dockerfile and pushes it to GitLab's container registry.
- **Test**: Runs automated tests to ensure functionality before deployment.
- **Review**: Deploys the application to a dynamic review environment for manual testing.
- **DAST**: Conducts dynamic application security testing to detect vulnerabilities.
- **Production**: Deploys the application to the production environment using Kubernetes.

### Configuration

The `.gitlab-ci.yml` file contains the pipeline configuration. This file orchestrates the entire process, utilizing various GitLab CI features such as jobs, stages, and environments.
