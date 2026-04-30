# Ecommerce pipeline: Mise en place d'un ETL avec de données générées

## Stack
- **DLT** : ingestion + normalisation
    C'est un framework Python qui automatise la création de pipelines ELT.
    On décores les fonctions avec @dlt.resource / @dlt.source
    Il gère seul : inférence de schéma, normalisation du JSON imbriqué, chargement incrémental. On a deux write_disposition : append (ajoute) et merge (upsert)
- **DuckDB** : warehouse local
    Base SQL embarquée, zéro serveur, un seul fichier .duckdb
    Très rapide sur des fichiers Parquet et des données analytiques
    Utilisé ici comme destination DLT et comme moteur de lecture pour dbt
    L'équivalent local de BigQuery ou Snowflake
- **MinIO** : object storage (S3-like)
    Object storage open-source, compatible API S3
    On y stocke les fichiers Parquet bruts produits par DLT
    L'équivalent self-hosted de AWS S3 ou Google Cloud Storage
    Lancé via Docker, interface web sur localhost:9001
- **dbt** : transformation SQL
    Outil de transformation SQL, il lit depuis DuckDB et écrit des modèles
    Deux couches créées :
        staging/ → nettoyage brut (cast, filtre des annulés)
        marts/ → agrégations métier (CA par pays, commandes, clients uniques)
    sources.yml → déclare les tables sources à dbt
    profiles.yml → dit à dbt où est la base de données

## Architecture
```
JSON Source → DLT → DuckDB → dbt → marts
                 └→ MinIO (Parquet)
```

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # remplis les valeurs

## Run
```bash
# Ingestion vers DuckDB
python -m ingestion.pipelines.pipeline_duckdb

# Ingestion vers MinIO
python -m ingestion.pipelines.pipeline_minio

# Transformation dbt
cd ecommerce_transform && dbt run
```