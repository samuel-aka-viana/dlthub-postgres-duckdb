import os
from typing import Iterator, Dict, Any

import dlt
from dlt.sources.sql_database import sql_database


@dlt.transformer(standalone=True)
def aggregate_to_json_array(items: Iterator[Dict[str, Any]]) -> Iterator[Dict[str, Any]]:
    all_records = list(items)

    yield {
        "data": all_records,
        "total_records": len(all_records),
        "exported_at": dlt.common.pendulum.now().isoformat(),
        "format": "json_array"
    }


@dlt.source(name="postgres_to_json_source")
def postgres_json_source():
    sql_source = sql_database(
        table_names=["family", "family_stats"],
        reflection_level="table_and_columns"
    )

    @dlt.resource(name="family_json", write_disposition="replace")
    def family_as_json():
        family_data = sql_source.family
        aggregated = family_data | aggregate_to_json_array()
        for record in aggregated:
            yield record

    @dlt.resource(name="family_stats_json", write_disposition="replace")
    def family_stats_as_json():
        stats_data = sql_source.family_stats
        aggregated = stats_data | aggregate_to_json_array()
        for record in aggregated:
            yield record

    return family_as_json(), family_stats_as_json()


def main():
    output_path = "./data/sql_json_export"
    os.makedirs(output_path, exist_ok=True)

    pipeline = dlt.pipeline(
        pipeline_name="postgres_to_json",
        destination="filesystem",
        dataset_name="postgres_data",
        dev_mode=False,
    )

    dlt.config["destination.filesystem.bucket_url"] = output_path
    dlt.config["load.file_format"] = "jsonl"
    dlt.config["normalize.data_writer.disable_compression"] = True

    load_info = pipeline.run(postgres_json_source())
    print(f" Pipeline finalizado: {load_info}")

    return pipeline


if __name__ == "__main__":
    main()
