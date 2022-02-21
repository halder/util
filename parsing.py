# parse sql query into string to be used within pySpark code
# makes for easier maintainability of large sql queries

def parse_sql(sql_file, replacement=None):
    """
    sql_file: string; relative location of .sql file e.g. "../my_query.sql"
    replacement: dict; mapping for f-string like replacement. Use curly braces within sql query to indicate variable (e.g. {date_dummy})
    """

    with open(sql_file, mode="r") as file:
        query = file.read()
    file.close()

    if replacement:
        for dummy, repl in replacement.items():
            query = query.replace(dummy, repl)

    return query
