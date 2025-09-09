from dlt.sources.sql_database import sql_database
import dlt


def main():
    source = sql_database(
        table_names=["family", "family_stats"],
        reflection_level="table_and_columns"
    )

    pipeline = dlt.pipeline(
        pipeline_name="postgres_to_json",
        destination="filesystem",
        dataset_name="postgres_data",
        dev_mode=False,
    )

    load_info = pipeline.run(source)
    print(f"pipeline finalizado {load_info}")

    return pipeline


if __name__ == "__main__":
    main()