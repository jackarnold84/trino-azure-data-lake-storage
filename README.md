# Trino Azure Data Lake Storage (ADLS Gen2) Connector + Hive Metastore

Connect Trino to Azure ADLS object storage by configuring a hive metastore.  
See: 
[Hive Connector with Azure Storage](https://trino.io/docs/current/connector/hive-azure.html)
and 
[Azure Data Lake Storage Gen 2](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction)


## Design
The design uses 3 containers built and connected using docker compose.
- trino-coordinator
- mariadb
- hive-metastore


## Requirements
- docker and docker compose
- Azure Data Lake Storage Gen 2 Account (hierarchical namespace enabled)
  with access key
- [optional] python and the trino package (`pip install trino`)


## Credentials
You must replace all instances of `{{ adls account name }}` and `{{ adls account key }}`
with your corresponding Azure credentials.

*Account name* is the unique name for your Azure storage account (ex: mystorage1).  
*Account key* is the access key for the account (ex: w0jgEHgh3hj3hgs3ibBBJENej3...)  

You must modify the following files to add credentials:
- `etc/catalog/adls2.properties`
- `metastore/conf/metastore-site.xml`


## Run
- Run `docker compose up -d`
- Wait a moment for the trino server to start (check `docker ps`)
- Access the trino command line: `docker exec -it trino-azure-adls-trino-coordinator-1 trino`

### Example queries
These example queries assume your storage account is named `mystorage` and you created a 
container called `examples` and added the files located in `example-data/` to your ADLS account. 
Modify as necessary for your needs.    

```
CREATE SCHEMA adls2.examples
WITH (location = 'abfs://examples@mystorage.dfs.core.windows.net/');

CREATE TABLE adls2.examples.parquet (
    name varchar(15),
    year integer,
    age integer,
    department varchar(15)
) WITH (
    external_location = 'abfs://examples@mystorage.dfs.core.windows.net/parquet',
    format = 'PARQUET'
);

SELECT * FROM adls2.examples.parquet 
WHERE age > 30;
```

### Query using python
See `test-queries.py` for an example of querying using python instead of the command line.
Requires the `trino` package.


## Resources
- [Hive Connector with Azure Storage](https://trino.io/docs/current/connector/hive-azure.html)
- [Introduction to the Hive Connector](https://trino.io/blog/2020/10/20/intro-to-hive-connector.html)
- [Similar example using MinIO](https://github.com/bitsondatadev/trino-getting-started/tree/main/hive/trino-minio)

