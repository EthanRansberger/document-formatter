import os
from datetime import datetime

def init_logging():
    log_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "logs")
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    log_file = os.path.join(log_folder, "error.log")
    with open(log_file, 'w') as f:
        f.write(f"Log initialized at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    return log_file

def log_error(e):
    log_file = init_logging()
    with open(log_file, 'a') as log:
        log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {str(e)}\n")
    print(f"Error logged to {log_file}")
