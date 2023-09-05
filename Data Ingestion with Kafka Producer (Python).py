from kafka import KafkaProducer
import json
import random  # For generating random data (replace with real data source)

# Configure Kafka producer
producer = KafkaProducer(bootstrap_servers='your_kafka_broker_url')

# Simulate data from fleet (replace with real data source)
def generate_random_data():
    vehicle_id = random.randint(1, 100)
    fuel_consumption = round(random.uniform(4, 15), 2)
    driver_behavior = random.choice(["Normal", "Aggressive", "Safe"])
    timestamp = "2023-09-05T" + str(random.randint(0, 23)).zfill(2) + ":00:00"

    data = {
        "vehicle_id": str(vehicle_id),
        "fuel_consumption": fuel_consumption,
        "driver_behavior": driver_behavior,
        "timestamp": timestamp
    }
    return data

while True:
    data = generate_random_data()
