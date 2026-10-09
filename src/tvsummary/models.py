class TVShow:
    """Represents and cleans a single TV show record from TVMaze."""

    def __init__(self, data: dict):
        self.id = data.get("id")
        self.name = data.get("name", "Unknown Title")
        
        # Clean genres: default to ["Uncategorized"] if empty or None
        raw_genres = data.get("genres")
        self.genres = raw_genres if raw_genres else ["Uncategorized"]
        
        # Extract network name: handle nested dict or missing network object
        network_obj = data.get("network")
        if network_obj and isinstance(network_obj, dict) and network_obj.get("name"):
            self.network = network_obj["name"]
        else:
            self.network = "Unknown Network"

    def __str__(self) -> str:
        return f"{self.name} ({self.network}) - Genres: {', '.join(self.genres)}"