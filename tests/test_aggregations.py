from tvsummary.aggregations import ChannelAggregation, GenreAggregation
from tvsummary.models import TVShow


def test_genre_aggregation():
    sample_data = [
        {"name": "Show A", "genres": ["Drama", "Sci-Fi"], "network": {"name": "HBO"}},
        {"name": "Show B", "genres": ["Drama"], "network": {"name": "Netflix"}},
    ]
    shows = [TVShow(item) for item in sample_data]
    agg = GenreAggregation()
    result = agg.compute(shows)

    assert result["Drama"] == 2
    assert result["Sci-Fi"] == 1


def test_channel_aggregation():
    sample_data = [
        {"name": "Show A", "genres": ["Drama"], "network": {"name": "HBO"}},
        {"name": "Show B", "genres": ["Comedy"], "network": {"name": "HBO"}},
        {"name": "Show C", "genres": ["Action"], "network": None},
    ]
    shows = [TVShow(item) for item in sample_data]
    agg = ChannelAggregation()
    result = agg.compute(shows)

    assert result["HBO"] == 2
    assert result["Unknown Network"] == 1
    