import re


def fetch_data_from_sql_query():
    try:
        user_id_and_time_stamp = []
        with open("add_data.sql", "r") as file:
            for line in file:
                values = re.search(r"values \('(\d+)', '(.*)'\)", line)
                user_id = int(values.group(1))
                time_stamp = values.group(2)
                user_id_and_time_stamp.append((user_id, time_stamp))

            return user_id_and_time_stamp

    except Exception as e:
        raise Exception(f"An error occurred while fetching data from SQL query: {e}")
