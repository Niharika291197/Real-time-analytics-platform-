from kafka import KafkaConsumer
import json
import sqlite3  # Import the SQLite library

# Configure Kafka consumer
consumer = KafkaConsumer('fleet_data_topic', bootstrap_servers='your_kafka_broker_url', group_id='fleet_analytics_group')

# Create a SQLite database and table (one-time setup)
conn = sqlite3.connect('fleet_data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS fleet_data (
        vehicle_id TEXT,
        fuel_consumption REAL,
        driver_behavior TEXT,
        timestamp TEXT
    )
''')
conn.commit()
conn.close()

# Function to insert data into the SQLite database
def insert_data_into_db(data):
    conn = sqlite3.connect('fleet_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO fleet_data (vehicle_id, fuel_consumption, driver_behavior, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (data['vehicle_id'], data['fuel_consumption'], data['driver_behavior'], data['timestamp']))
    conn.commit()
    conn.close()

for message in consumer:
    data = json.loads(message.value.decode('utf-8'))
    
    # Perform real-time analysis (replace with actual analysis code)
    fuel_consumption = data['fuel_consumption']
    driver_behavior = data['driver_behavior']
    
    # Store results in the SQLite database
    insert_data_into_db(data)
