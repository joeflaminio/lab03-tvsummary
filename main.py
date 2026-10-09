import sys
from tvsummary import ChannelAggregation, GenreAggregation, SummaryReport, TVMazeFetcher
from tvsummary.config import OUTPUT_PATH, SOURCE_URL


def main():
    print("Fetching data from TVMaze API...")
    fetcher = TVMazeFetcher(SOURCE_URL)
    shows = fetcher.fetch()

    if not shows:
        print("Error: Could not retrieve records. Exiting without traceback.")
        sys.exit(1)

    print(f"Successfully processed {len(shows)} records.")

    print("Running aggregations...")
    aggregations = [
        GenreAggregation(),
        ChannelAggregation(),
    ]

    report = SummaryReport(source_url=SOURCE_URL, aggregations=aggregations)
    summary = report.build_summary(shows)

    print("Writing output report...")
    report.write_summary(summary, OUTPUT_PATH)


if __name__ == "__main__":
    main()
    