import duckdb, os, glob

DB_PATH = "dev.duckdb"
RAW_DIR = "data/raw"

con = duckdb.connect(DB_PATH)
con.execute("CREATE SCHEMA IF NOT EXISTS raw")

for csv_file in glob.glob(f"{RAW_DIR}/*.csv"):
    table_name = os.path.basename(csv_file).replace(".csv", "")
    # DROP + CREATE pour l'idempotence
    con.execute(f"DROP TABLE IF EXISTS raw.{table_name}")
    con.execute(f"""
        CREATE TABLE raw.{table_name} AS
        SELECT * FROM read_csv_auto('{csv_file}', header=true)
    """)
    count = con.execute(f"SELECT COUNT(*) FROM raw.{table_name}").fetchone()[0]
    print(f"✓ {table_name} : {count:,} lignes")