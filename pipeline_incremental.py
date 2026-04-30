import dlt
#from dlt.sources.incremental import Incremental
from ingestion.utils.fake_source import generate_orders
from datetime import datetime


@dlt.resource(name="orders", write_disposition="merge", primary_key="order_id")
def orders_incremental(update_at=dlt.sources.incremental("created_at")):
    data = generate_orders(500)
    yield data


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="ecommerce_incremental",
        destination="duckdb",
        dataset_name="raw_ecommerce"
    )
    
    # 1er run
    print("----Run 1----")
    info = pipeline.run(orders_incremental())
    print(info)

    # 2ème run — DLT ne charge que ce qui est nouveau
    print("--- Run 2 (devrait charger moins) ---")
    info = pipeline.run(orders_incremental())
    print(info)