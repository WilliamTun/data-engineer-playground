
# import polars
import polars as pl 

# define schema:
# https://pola-rs.github.io/polars/py-polars/html/reference/datatypes.html
dtypes = {
    'key': pl.Categorical,
    'a': pl.Float64,
    'b': pl.Float64,
    'c': pl.Float64,
    'd': pl.Float64,
    'e': pl.Float64
}

# read csv file
df = pl.read_csv("file4_missing_vals.csv", dtypes=dtypes)

# apply lambda func 
df = df.with_column(
    pl.col("a").apply(lambda x: x + 10)
)

# apply lambda func and put results in new column
df = df.with_column(
    pl.col("a").apply(lambda x: x * 10).alias("xxx")
)

# group by, aggregate, & sort
df = df.groupby("key").agg(
    [
        pl.col("a").mean(),
        pl.col("b").mean(),
        pl.col("xxx").mean()
    ]
).sort("xxx")

print(df)

