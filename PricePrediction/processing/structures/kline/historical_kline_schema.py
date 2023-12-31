from pyspark.sql.types import LongType,StringType,DoubleType,IntegerType,BooleanType,StructType,StructField,TimestampType

historicalKlineSchema = StructType([\
    StructField("timestamp",LongType(),True),
    StructField("open",DoubleType(),True),
    StructField("high",DoubleType(),True),
    StructField("low",DoubleType(),True),
    StructField("close",DoubleType(),True),
    StructField("volume",DoubleType(),True),
    StructField("close_time",LongType(),True),
    StructField("quote_asset_volume",DoubleType(),True),
    StructField("number_of_trades",IntegerType(),True),
    StructField("taker_buy_base_asset_volume",DoubleType(),True),
    StructField("taker_buy_quote_asset_volume",DoubleType(),True),
    StructField("ignore",LongType(),True),
    # StructField("1m_close_time",TimestampType(),True),
    # StructField("1m_open_time",TimestampType(),True),
    # StructField("1m_open",DoubleType(),True),
    # StructField("1m_high",DoubleType(),True),
    # StructField("1m_low",DoubleType(),True),
    # StructField("1m_close",DoubleType(),True),
    # StructField("1m_quote_asset_volume",DoubleType(),True),
    # StructField("1m_number_of_trades",DoubleType(),True),
    # StructField("1m_taker_buy_base_asset_volume",DoubleType(),True),
    # StructField("1m_taker_buy_quote_asset_volume",DoubleType(),True),
    # StructField("1m_volume",DoubleType(),True),
    # StructField("1m_open_time_day",IntegerType(),True),
    # StructField("1m_open_time_month",IntegerType(),True),
    # StructField("1m_open_time_year",IntegerType(),True),
    # StructField("1m_open_time_hour",IntegerType(),True),
    # StructField("1m_open_time_minute",IntegerType(),True),
    # StructField("1m_close_time_day",IntegerType(),True),
    # StructField("1m_close_time_month",IntegerType(),True),
    # StructField("1m_close_time_year",IntegerType(),True),
    # StructField("1m_close_time_hour",IntegerType(),True),
    # StructField("1m_close_time_minute",IntegerType(),True),
])
