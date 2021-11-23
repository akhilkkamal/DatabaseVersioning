import sqlparse
from typing import Iterator, List

def read_sql_file(file_loc: str) -> str:
    with open(file_loc, 'r') as _f:
        _data = _f.read()
        return _data

def sql_split_file(_data: str) -> List[str]:
    split_sql = read_sql_file(_data)
    return sqlparse.split(split_sql)

def sql_file_generator(file_loc: str) -> Iterator[str]:
    _data = read_sql_file(file_loc)
    split_sql = sql_split_file(_data)
    for s in split_sql:
        yield(s)

