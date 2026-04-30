"""Pipeline dlt vers duckdb"""
import dlt
from ingestion.utils.fake_source import generate_orders

@dlt.resource(
    name="orders",
    write_disposition="merge",
    primary_key="order_id"
)
def orders_resource(
    updated_at=dlt.sources.incremental("created_at")
):
    """
    Resource DLT pour les commandes.
    - merge : upsert basé sur order_id
    - incremental : ne recharge que les nouvelles lignes
    """
    yield generate_orders(100)


@dlt.source(name="ecommerce")
def ecommerce_source():
    """
    Source principale qui regroupe toutes les resources.
    Ajouter ici de nouvelles resources (customers, products, etc.)
    """
    return orders_resource()