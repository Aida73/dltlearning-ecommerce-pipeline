"""
docker run -p 9000:9000 -p 9001:9001 \
  -e MINIO_ROOT_USER=minioadmin \
  -e MINIO_ROOT_PASSWORD=minioadmin \
  minio/minio server /data --console-address ":9001"
"""
import dlt
import os
from ingestion.sources.ecommerce import ecommerce_source

load_dotenv()

def run():

    # Credentials MinIO
    os.environ["DESTINATION__FILESYSTEM__BUCKET_URL"] = f"s3://{os.getenv('MINIO_BUCKET')}"
    os.environ["DESTINATION__FILESYSTEM__CREDENTIALS__AWS_ACCESS_KEY_ID"] = os.getenv("MINIO_ACCESS_KEY")
    os.environ["DESTINATION__FILESYSTEM__CREDENTIALS__AWS_SECRET_ACCESS_KEY"] = os.getenv("MINIO_SECRET_KEY")
    os.environ["DESTINATION__FILESYSTEM__CREDENTIALS__ENDPOINT_URL"] = os.getenv("MINIO_ENDPOINT")
    pipeline = dlt.pipeline(
        pipeline_name="ecommerce_minio",
        destination="filesystem",
        dataset_name="raw_ecommerce"
    )

    load_info = pipeline.run(ecommerce_source())
    print(load_info)


if __name__ == "__main__":
    run()