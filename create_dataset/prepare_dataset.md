## Preparing the data set

#### Downloading electricity data

1. Use `download_sql.py` to download the hourly/15 minute data into CSVs.
Each home is assigned its own data id.
2. Next, convert the data into monthly energy consumption using `convert_raw_electricity_monthly.py`
This will create `~/all.h5`

#### In case we want to shift to local machine
1. Compress `~/all.h5` to `all.h5.tar.gz` using `tar -czvf all.h5.tar.gz ~/all.h5 `

#### Downloading metadata
1. Use `download_metadata.py` to download the main metadata CSV.
2.
