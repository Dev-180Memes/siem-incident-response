import pandas as pd
import numpy as np
import joblib
import time

# Load the model and scaler
model = joblib.load('weights/isolation_forest_model.pkl')
scaler = joblib.load('weights/scaler.pkl')

# Load the dataset
data = pd.read_csv('data/data.csv')
data.columns = data.columns.str.lower()  # Ensure column headings are lowercase

# List to keep track of blocked IP addresses
blocked_ips = []


# Function to check if an IP is blocked
def is_ip_blocked(ip_address):
    return ip_address in blocked_ips


# Incident response logic
def block_ip(ip_address):
    blocked_ips.append(ip_address)
    print(f"Blocking IP address: {ip_address}")
    # Simulate blocking IP address logic (e.g., updating firewall rules)


def send_notification(ip_address, data):
    print(f"Sending notification for IP address: {ip_address}")
    print(f"Anomalous traffic detected: {data}")
    # Simulate sending notification logic (e.g., email, SMS, etc.)


# Function to select a random traffic instance, predict, and respond if necessary
def check_traffic_instance():
    # Select a random traffic instance (row)
    random_instance = data.sample(n=1)

    # Extract IP address from the 'ipv4_src_addr' column
    random_ip = random_instance['ipv4_src_addr'].values[0]

    # Check if the IP address is already blocked
    if is_ip_blocked(random_ip):
        print(f"IP address {random_ip} is already blocked.")
        return

    # Drop unnecessary columns
    columns_to_drop = ['attack', 'label', 'ipv4_src_addr', 'ipv4_dst_addr']
    random_instance = random_instance.drop(columns=columns_to_drop, errors='ignore')

    # Standardize the instance
    random_instance_scaled = scaler.transform(random_instance)

    # Predict anomaly
    prediction = model.predict(random_instance_scaled)
    is_anomalous = prediction[0] == -1

    # Output the result
    print(f"Random Traffic Instance:\n{random_instance}")
    print(f"Prediction: {'Anomalous' if is_anomalous else 'Normal'}")

    if is_anomalous:
        print("Anomaly detected! Initiating incident response...")
        block_ip(random_ip)
        send_notification(random_ip, random_instance)


# Run the check for random traffic instances in a loop for 10 seconds
start_time = time.time()
while time.time() - start_time < 10:
    check_traffic_instance()
    time.sleep(1)  # Add a short delay to avoid excessive CPU usage
