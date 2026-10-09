import requests
from tvsummary.models import TVShow

class TVMazeFetcher:
    """Fetches records from the TVMaze API and parses them into TVShow objects."""

    def __init__(self, url: str):
        self.url = url

    def fetch(self) -> list[TVShow]:
        """Download show records and return a list of TVShow instances."""
        try:
            response = requests.get(self.url, timeout=15)
            response.raise_for_status()
            raw_data = response.json()
            return [TVShow(item) for item in raw_data]
        except requests.exceptions.RequestException as error:
            print(f"Error: {error}")
            return []