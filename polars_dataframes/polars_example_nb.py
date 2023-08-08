# source: https://www.youtube.com/watch?v=CByx7XjYMhw&ab_channel=ThePyCoach

# import polars
import polars as pl 

# read csv file
df = pl.read_csv("file.csv")
print(df)

# get column names
print(df.columns)

# ==== Select columns =======
# select 1 col
df.select(pl.col("a"))

# select 2+ col 
df.select(pl.col(["a", "b"]))

# select all columns
df.select(pl.col('*'))

# ==== Create columns =======
# create a new column that sums the value of col a & b
df.with_columns(
    (pl.col("a") + pl.col("b")).alias("ab")
)

# ==== Filter =================
# single filter
print(df.filter(pl.col("a") > 2))

# multiple filter
print(df.filter( (pl.col("a") == 1) & (pl.col("b") == 2)))

# ==== GroupBy =================
df.groupby("a").count()

# ==== Join DF =================
df2 = pl.read_csv("file2.csv")
df3 = df.join(df2, on="key")

# ===== concat =================

# horizontal concatenation
# - will not work if two columns of same name exist
# pl.concat([df, df2], how="horizontal") # makes dataframe wider
df4 = pl.read_csv("file3.csv")
print(pl.concat([df, df4], how="vertical")) # makes dataframe longer