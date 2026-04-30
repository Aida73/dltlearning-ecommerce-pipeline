"""Pipeline dlt vers duckdb"""
import dlt
from ingestion.sources.ecommerce import ecommerce_source


def run():
    pipeline = dlt.pipeline(
        pipeline_name="ecommerce_pipeline",
        destination="duckdb",
        dataset_name="raw_ecommerce"
    )
    load_info = pipeline.run(ecommerce_source())
    print(load_info)

    # verification des données dans duckdb
    with pipeline.sql_client() as client:
        with client.execute_query("SELECT * FROM orders LIMIT 5") as cursor:
            for raw in cursor.fetchall():
                print(raw)



if __name__ == "__main__":
    run()