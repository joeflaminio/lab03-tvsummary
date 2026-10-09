from tvsummary.models import TVShow


class Aggregation:
    """Base class for all data aggregations."""

    def compute(self, records: list[TVShow]) -> dict[str, int]:
        """Override this method in subclasses to return aggregation results."""
        raise NotImplementedError("Subclasses must implement compute()")


class GenreAggregation(Aggregation):
    """Aggregates show counts per genre."""

    def compute(self, records: list[TVShow]) -> dict[str, int]:
        genre_counts: dict[str, int] = {}
        for show in records:
            for genre in show.genres:
                genre_counts[genre] = genre_counts.get(genre, 0) + 1
        return genre_counts


class ChannelAggregation(Aggregation):
    """Aggregates show counts per network/channel."""

    def compute(self, records: list[TVShow]) -> dict[str, int]:
        channel_counts: dict[str, int] = {}
        for show in records:
            channel_counts[show.network] = channel_counts.get(show.network, 0) + 1
        return channel_counts