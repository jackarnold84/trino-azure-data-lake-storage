import trino

conn = trino.dbapi.connect(
    host='localhost',  # or use external IP address of trino coordinator
    port=8080,
    user='my-python-client'
)

cur = conn.cursor()


# executes and prints the results of a query
def execute(query):
    try:
        cur.execute(query)
        [print(r) for r in cur.fetchall()]
        print()
    except Exception as e: 
        print(e, '\n')



# create schema
print('Creating Schema...')
execute("""
    CREATE SCHEMA adls2.examples
    WITH (location = 'abfs://examples@mystorage.dfs.core.windows.net/')
""")



# read parquet files
print('PARQUET FILES:')

print('Creating Table...')
execute("""
    CREATE TABLE adls2.examples.parquet (
        name varchar(15),
        year integer,
        age integer,
        department varchar(15)
    ) WITH (
        external_location = 'abfs://examples@mystorage.dfs.core.windows.net/parquet',
        format = 'PARQUET'
    )
""")


print('Running Example Query...')
execute("""
    SELECT * FROM adls2.examples.parquet 
    WHERE age > 30
""")



# read csv files
print('CSV FILES:')

print('Creating Table...')
execute("""
    CREATE TABLE adls2.examples.csv (
        name varchar,
        year varchar,
        age varchar,
        department varchar
    ) WITH (
        external_location = 'abfs://examples@mystorage.dfs.core.windows.net/csv',
        format = 'CSV'
    )
""")


print('Running Example Query...')
execute("""
    SELECT * FROM adls2.examples.csv
    WHERE department = 'CS'
""")
