import warnings

try:
    from polars.polars import version
except ImportError:

    def version() -> str:
        return ""

    # this is only useful for documentation
    warnings.warn("polars binary missing!")

from polars import testing
from polars.cfg import Config
from polars.convert import (
    from_arrow,
    from_dict,
    from_dicts,
    from_numpy,
    from_pandas,
    from_records,
)
from polars.datatypes import (
    Boolean,
    Categorical,
    DataType,
    Date,
    Datetime,
    Duration,
    Field,
    Float32,
    Float64,
    Int8,
    Int16,
    Int32,
    Int64,
    List,
    Null,
    Object,
    PolarsDataType,
    Struct,
    Time,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
    Utf8,
    get_idx_type,
)
from polars.exceptions import (
    ArrowError,
    ComputeError,
    DuplicateError,
    NoDataError,
    NotFoundError,
    PanicException,
    SchemaError,
    ShapeError,
)
from polars.internals.expr import Expr

# TODO remove need for wrap_df
from polars.internals.frame import wrap_df  # noqa: F401
from polars.internals.frame import DataFrame
from polars.internals.functions import concat, cut, date_range, get_dummies
from polars.internals.io import read_ipc_schema, read_parquet_schema
from polars.internals.lazy_frame import LazyFrame
from polars.internals.lazy_functions import _date as date
from polars.internals.lazy_functions import _datetime as datetime
from polars.internals.lazy_functions import (
    all,
    any,
    apply,
    arange,
    arg_where,
    argsort_by,
    avg,
    col,
    collect_all,
    concat_list,
    concat_str,
    count,
    cov,
    duration,
    element,
    exclude,
    first,
    fold,
    format,
    groups,
    head,
    last,
    lit,
    map,
    max,
    mean,
    median,
    min,
    n_unique,
    pearson_corr,
    quantile,
    repeat,
    select,
    spearman_rank_corr,
    std,
    struct,
    sum,
    tail,
)
from polars.internals.lazy_functions import to_list as list
from polars.internals.lazy_functions import var

# TODO: remove need for wrap_s
from polars.internals.series import wrap_s  # noqa: F401
from polars.internals.series import Series
from polars.internals.whenthen import when
from polars.io import (
    read_avro,
    read_csv,
    read_excel,
    read_ipc,
    read_json,
    read_parquet,
    read_sql,
    scan_csv,
    scan_ds,
    scan_ipc,
    scan_parquet,
)
from polars.string_cache import StringCache, toggle_string_cache
from polars.utils import threadpool_size

__all__ = [
    "exceptions",
    "NotFoundError",
    "ShapeError",
    "SchemaError",
    "ArrowError",
    "ComputeError",
    "NoDataError",
    "DuplicateError",
    "PanicException",
    "DataFrame",
    "Series",
    "LazyFrame",
    # polars.datatypes
    "DataType",
    "Int8",
    "Int16",
    "Int32",
    "Int64",
    "UInt8",
    "UInt16",
    "UInt32",
    "UInt64",
    "Float32",
    "Float64",
    "Boolean",
    "Utf8",
    "List",
    "Date",
    "Datetime",
    "Time",
    "Duration",
    "Object",
    "Categorical",
    "Field",
    "Struct",
    "Null",
    "PolarsDataType",
    "get_idx_type",
    # polars.io
    "read_csv",
    "read_excel",
    "read_parquet",
    "read_json",
    "read_sql",
    "read_ipc",
    "scan_csv",
    "scan_ipc",
    "scan_ds",
    "scan_parquet",
    "read_ipc_schema",
    "read_parquet_schema",
    "read_avro",
    # polars.stringcache
    "StringCache",
    "toggle_string_cache",
    # polars.config
    "Config",
    # polars.internal.when
    "when",
    # polars.internal.expr
    "Expr",
    # polars.internal.functions
    "arg_where",
    "concat",
    "date_range",
    "get_dummies",
    "repeat",
    "element",
    "cut",
    # polars.internal.lazy_functions
    "col",
    "count",
    "std",
    "var",
    "max",
    "min",
    "sum",
    "mean",
    "avg",
    "median",
    "n_unique",
    "first",
    "last",
    "head",
    "tail",
    "lit",
    "pearson_corr",
    "spearman_rank_corr",
    "cov",
    "map",
    "apply",
    "fold",
    "any",
    "all",
    "groups",
    "quantile",
    "arange",
    "argsort_by",
    "concat_str",
    "concat_list",
    "collect_all",
    "exclude",
    "format",
    "datetime",  # named _datetime, see import above
    "date",  # name _date, see import above
    "list",  # named to_list, see import above
    "select",
    "var",
    "struct",
    "duration",
    # polars.convert
    "from_dict",
    "from_dicts",
    "from_records",
    "from_numpy",
    "from_arrow",
    "from_pandas",
    # testing
    "testing",
    "threadpool_size",
]

__version__ = version()

import os

os.environ["POLARS_ALLOW_EXTENSION"] = "true"
