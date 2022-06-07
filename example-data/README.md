# example-data

Example files to put in your Azure Storage Account and query with Trino.

Example:
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
