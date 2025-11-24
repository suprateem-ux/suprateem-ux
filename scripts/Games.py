import requests
from datetime import datetime

def download_lichess_games(username="supratsa"):
    url = f"https://lichess.org/api/games/user/{username}"
    params = {
        "tags": "true",
        "clocks": "true",
        "evals": "true",
        "opening": "true",
        "literate": "false"
    }

    print("Downloading games…")
    response = requests.get(url, params=params, stream=True)

    if response.status_code != 200:
        print("Error:", response.status_code)
        return
    
    filename = f"lichess_games_{username}_{datetime.now().strftime('%Y-%m-%d')}.pgn"
    
    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    print(f"Saved to {filename}")

if __name__ == "__main__":
    download_lichess_games()
