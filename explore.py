import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    return


@app.cell
def _():
    import duckdb
    import dlt

    DATABASE_URL = "/home/smovisk/PycharmProjects/PythonProject/dlt_database.duckdb"
    engine = duckdb.connect(DATABASE_URL, read_only=False)


    return (engine,)


@app.cell
def _(engine):
    engine.sql("select * from postgres_data.family")
    return


if __name__ == "__main__":
    app.run()
