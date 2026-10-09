import json
from pathlib import Path
from tvsummary.aggregations import Aggregation
from tvsummary.models import TVShow


class SummaryReport:
    """Combines aggregation results and writes the output JSON file."""

    def __init__(self, source_url: str, aggregations: list[Aggregation]):
        self.source_url = source_url
        self.aggregations = aggregations

    def build_summary(self, records: list[TVShow]) -> dict:
        """Runs all aggregations using polymorphism and constructs the output dict."""
        results = {}
        for agg in self.aggregations:
            # Polymorphic call to compute() on each subclass
            key_name = agg.__class__.__name__.lower()
            results[key_name] = agg.compute(records)

        return {
            "source_url": self.source_url,
            "total_records_processed": len(records),
            "aggregations": results,
        }

    def write_summary(self, summary: dict, output_path: Path) -> None:
        """Writes the summary to disk using pathlib and json.dump."""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)
        print(f"Summary written to {output_path}")
        