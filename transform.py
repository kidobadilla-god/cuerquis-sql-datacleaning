import duckdb

output = duckdb.sql("""
COPY(
        SELECT
        DISTINCT *,
        
        SPLIT_PART(browser_os, ' ', 1) AS browser,
        SPLIT_PART(browser_os, ' ', 2) AS os,

        TRIM(device_type) AS device_clean,

        CONCAT(browser_os, ' ', device_type) AS device_type,

        customer_id,
        COALESCE(session_pages_visited, '0') AS visited,
        FROM 'bronze.parquet',
    )
TO 'silver.parquet'(FORMAT PARQUET);
""")

