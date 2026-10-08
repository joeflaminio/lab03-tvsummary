# records.py

import json
from pathlib import Path

import requests

SOURCE_URL = "https://api.tvmaze.com/shows?page=0"
OUTPUT_PATH = Path("summary.json")

def fetch_records(url: str) -> list[dict]:
    """Downlaod the recordsand return them as python objects."""
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error: Failed Downlaod - {error}")

def shows_per_genre(shows: list[dict]) -> dict[str, int]:
            """Calculate the amount of shows per genre."""
            genre_counts: dict[str, int] = {}
            for show in shows:
                genres = show.get("genres", []) 
                if not genres:
                    genre_counts["not_categorized"] = genre_counts.get("not_categorized", 0) + 1
                else:
                    for G in genres:
                        genre_counts[G] = genre_counts.get(G, 0) + 1
            return genre_counts

def shows_per_channel(shows: list[dict]) -> dict[str, int]:
    """Calculate the amount of shows per channel."""
    channel_counts: dict[str, int] = {} 
    for show in shows:
        network_obj = show.get("network")
        if network_obj and network_obj.get("name"):
            chn_name = network_obj["name"] 
        else:
            chn_name = "unknown Network"

        channel_counts[chn_name] = channel_counts.get(chn_name, 0) + 1

    return channel_counts


def build_summary(shows: list[dict]) -> dict: 
    """combine the aggregations into one dict ready to write"""

    return {
        "source_url": SOURCE_URL,
        "total_records_processed": len(shows),
        "aggegations": {
            "shows_per_genre": shows_per_genre(shows),
            "shows_per_channel": shows_per_channel(shows),
        },
    } 

def write_summary(summary: dict, path: Path) -> None:
    """Write the summary to a JSON file using pathlib."""
    with path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
        print(f"wrote summary to {path}")

def main():
    """Main program execution pipeline."""
    print("Fetching data from TVMaze API...")
    shows = fetch_records(SOURCE_URL)

    print("Building summary aggregations...")
    summary = build_summary(shows)

    print("Writing output file...")
    write_summary(summary, OUTPUT_PATH)

if __name__ == "__main__":
    main() 
    
    

            