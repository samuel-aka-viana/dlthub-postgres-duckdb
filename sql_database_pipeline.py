from dlt.sources.sql_database import sql_database
import dlt
import duckdb

source = sql_database(
    table_names=["family", "family_stats"],
    reflection_level="table_and_columns"
)

pipeline = dlt.pipeline(
    pipeline_name="postgres_to_duckdb",
    destination="duckdb",
    dataset_name="postgres_data",
    dev_mode=False,
)

load_info = pipeline.run(source)
print(load_info)

conn = duckdb.connect("dlt_database.duckdb")

tables = conn.execute("SHOW TABLES").fetchall()
for table in tables:
    print(f"- {table[0]}")

family_data = conn.execute("SELECT * FROM postgres_data.family LIMIT 10").fetchall()
for row in family_data:
    print(row)

stats_data = conn.execute("SELECT * FROM postgres_data.family_stats LIMIT 10").fetchall()
for row in stats_data:
    print(row)

family_count = conn.execute("SELECT COUNT(*) FROM postgres_data.family").fetchone()[0]
stats_count = conn.execute("SELECT COUNT(*) FROM postgres_data.family_stats").fetchone()[0]

print(f"- family: {family_count}")
print(f"- family_stats: {stats_count}")

conn.close()