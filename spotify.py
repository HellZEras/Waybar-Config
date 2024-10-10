import subprocess
import json

def spotify_status():
    result = subprocess.run(["playerctl", "--player=spotify", "status"], capture_output=True, text=True)
    result = result.stdout.strip()
    if result == "Paused":
        return "Paused"
    elif result == "No players found":
        return "Not Found"
    elif result == "Playing":
        return "Playing"
    else:
        return "Unknown"

def parse_spotify_data(data):
    parsed_data = {}
    title = None # Initialize artist and title
    
    lines = data.splitlines()
    for line in lines:
        if "title" in line:
            index = line.find("title") + len("title")
            title = line[index:].strip()

    if title:
        return f"{title}"
    else:
        return "Unknown song"

def main():
    status = spotify_status()
    data = {}
    if status == "Paused":
        data = {'text': "Paused"}
    elif status == "Playing":
        result = subprocess.run(["playerctl", "--player=spotify", "metadata"], capture_output=True, text=True)
        to_write = parse_spotify_data(result.stdout)
        data = {'text': to_write}
    else:
        data = {'text': "No Songs"}
    
    print(json.dumps(data))

if __name__ == "__main__":
    main()
