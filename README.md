# Cloud-Based Learning Platform

## Project Overview
This project aims to build a comprehensive **cloud-based learning platform** that integrates **AI-powered educational services** with **enterprise-grade cloud infrastructure**. Students and educators will interact with various educational tools and microservices, including **speech-to-text**, **text-to-speech**, **document processing**, **chat AI**, and **quiz generation**. The platform leverages modern technologies such as **AWS**, **Docker**, **Kubernetes**, **Apache Kafka**, and **microservices architecture**.

---

## Features
- **Text-to-Speech (TTS)**: Converts text input into natural-sounding speech using AI-powered models.
- **Speech-to-Text (STT)**: Transcribes audio to text with support for multiple languages and formats.
- **Chat Service**: AI-driven conversational capabilities to interact with users and maintain conversation history.
- **Document Reader**: Upload and process documents, extracting text and generating summaries or notes.
- **Quiz Generation**: Automatically generates quizzes from uploaded documents and assesses student responses.

---

## Architecture
The platform is built using **microservices** deployed as **containers** and orchestrated using **Docker** and **Kubernetes**. Key components include:

1. **AWS Infrastructure**:
   - **Elastic Compute Cloud (EC2)** instances for container hosting.
   - **Elastic Load Balancer (ELB)** for service routing.
   - **Relational Database Service (RDS)** for service-specific databases.
   - **Simple Storage Service (S3)** for isolated storage.
   - **Kafka** for event-driven communication between services.

2. **Microservices**:
   - **TTS Service**: Dockerized Python service that converts text to speech.
   - **STT Service**: Dockerized Python service that transcribes speech to text.
   - **Chat Service**: Provides conversational AI capabilities.
   - **Document Reader Service**: Processes documents to extract and generate notes.
   - **Quiz Service**: Automatically generates quizzes based on document contents.

3. **CI/CD Pipeline**: 
   - **GitHub Actions** for automating the build, test, and deployment process.
   - **Amazon ECR** for container image storage.
   - **AWS ECS** or **Fargate** for container orchestration and deployment.

---

## Setup Instructions

### Prerequisites
- **Docker**: Ensure Docker is installed on your machine for building and running containers locally.
- **AWS Account**: For deploying to AWS services like EC2, RDS, and S3.
- **GitHub Account**: For repository management and CI/CD integration.

### Local Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/cloud-based-learning-platform.git
   cd cloud-based-learning-platform


### Code Genetated by
1. Yousef
2. Hassan x2
3. Mido

## Testing lINE