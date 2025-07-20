# FinTech Transaction Monitoring System

## Overview
Real-time transaction monitoring for fraud and AML using Kafka, GCP Dataflow, BigQuery, and Looker.

## Features
- Kafka-based real-time ingestion
- Fraud detection with Apache Beam
- Storage in BigQuery
- Alerting system
- Looker dashboards

## Getting Started
1. Run Kafka stack: `docker-compose up -d`
2. Start producer: `python kafka/producer.py`
3. Deploy Dataflow job
4. Monitor in BigQuery and Looker

## Terminal 1: Start Kafka infrastructure
cd docker
docker-compose up -d

## Terminal 2: Start transaction producer
cd ../kafka
source ../venv/bin/activate
python producer.py

## Terminal 3: Monitor with consumer
cd ../kafka
source ../venv/bin/activate
python consumer.py

## Terminal 4: Run Dataflow (modify to read from Kafka)
cd ../dataflow
source ../venv/bin/activate
python dataflow_job.py