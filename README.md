
# Real-Time Analytics Platform

## Overview

Built a Real-time Analytics platform for a transportation company utilizing various technologies to provide insights into fleet performance, fuel consumption, and driver behavior. The platform is designed to optimize operations and reduce costs.

## Technologies Used

- **Data Storage**: AWS S3
- **Real-time Data Streaming**: Kafka
- **Data Analysis**: AWS EC2
- **Deployment**: Heroku

## Sections

### Section 1: Data Ingestion with Kafka Producer

**Explanation:**

In this section of the project, we set up a Kafka producer to ingest simulated data into a Kafka topic. This is the initial step where data from the transportation fleet is generated and sent to the Kafka messaging system.

**Summary:**

This code sets up a Kafka producer, generates simulated fleet data, and sends it to the Kafka topic 'fleet_data_topic'. Replace the simulated data with real data from your fleet.

### Section 2: Real-time Data Analysis and Storage

**Explanation:**

In this section, we consume data from the Kafka topic, perform basic analysis on the data, and store it in an SQLite database. The analysis is rudimentary and should be replaced with your specific analytical requirements.

**Summary:**

- This code sets up a Kafka consumer to subscribe to the 'fleet_data_topic'.
- It creates an SQLite database and a table for storing fleet data.
- A function `insert_data_into_db` is defined to insert data into the database.
- Inside the loop, data is consumed from Kafka, rudimentary analysis is performed (replace with actual analysis), and the data is stored in the SQLite database.

### Section 3: Data Visualization with Flask

**Explanation:**

In this section, we create a basic Flask web application to visualize real-time fleet data. The web application displays the latest data from the SQLite database.

**Summary:**

- This code sets up a Flask web application with a single route '/'.
- In the `dashboard` function, it retrieves the latest data from the SQLite database.
- The data is passed to an HTML template for rendering.


