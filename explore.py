import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import duckdb
    import dlt

    DATABASE_URL = "/home/smovisk/PycharmProjects/PythonProject/dlt_database.duckdb"
    engine = duckdb.connect(DATABASE_URL, read_only=False)

    return dlt, engine


@app.cell
def _(engine):
    engine.sql("select * from postgres_data.family")
    return


@app.cell
def _(dlt):
    pipe = dlt.attach("postgres_to_duckdb")
    conn = pipe.dataset().ibis
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM postgres_data.family LIMIT 100
        """,
        engine=engine
    )
    return


if __name__ == "__main__":
    app.run()
