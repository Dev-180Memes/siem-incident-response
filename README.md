# siem-incident-response
This project demonstrates a simple Security Information and Event Management (SIEM) system that uses an Isolation Forest model for anomaly detection and includes incident response capabilities.
## Prerequisites
- Python 3.6 or higher
- internet connection to download the dataset and dependencies
## Getting Started
### Step 1: Download the Dataset
1. Download the dataset from the following link: [Dataset Link](https://drive.google.com/drive/folders/14DyvzBf3mtbC40zMY89aBb-JhDYfCMgv?usp=sharing)
### Step 2: Set Up the Project
1. Clone this repository or download the project files to your local machine.
2. Navigate to the project directory
```bash
cd path/to/project
```
3. Place the downloaded dataset file into a folder named `data`.
4. Create a virtual environment (optional but recommended):
```bash
python -m venv venv

# on Windows
.\venv\Scripts\activate

# on macOs and linux
source venv/bin/activate
```
5. Install the required dependencies
```bash
pip install -r requirements.txt
```
6. Run the project
```bash
python main.py 
```

## Example output

```bash
Random Traffic Instance:
    l4_src_port  l4_dst_port  protocol  ...  num_pkts_1024_to_1514_bytes  tcp_win_max_in  tcp_win_max_out
10           80        12345         6  ...                           2             1024             2048

Prediction: Anomalous
Anomaly detected! Initiating incident response...
Blocking IP address: 192.168.1.1
Sending notification for IP address: 192.168.1.1
Anomalous traffic detected:
    l4_src_port  l4_dst_port  protocol  ...  num_pkts_1024_to_1514_bytes  tcp_win_max_in  tcp_win_max_out
10           80        12345         6  ...                           2             1024             2048

```