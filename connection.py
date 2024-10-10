import socket
import json

def check_tcp_connection(host="8.8.8.8", port=53, timeout=1):
    try:
        # Create a TCP socket
        with socket.create_connection((host, port), timeout):
            return {"text": "Connected","class":"connected"}
    except Exception:
        return {"text": "Disconnected"}

def main():
    connection_status = check_tcp_connection()
    print(json.dumps(connection_status))

if __name__ == "__main__":
    main()
