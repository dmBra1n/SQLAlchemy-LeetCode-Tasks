from typing import List

from sqlalchemy import inspect, text

from utils.database import sync_engine


def delete_all_tables(tables: List[str]):
    if tables:
        with sync_engine.connect() as conn:
            for table_name in tables:
                stmt = f"""DROP TABLE "{table_name}" CASCADE;"""
                conn.execute(text(stmt))
                print(f'[INFO] Table "{table_name}" has been deleted')

            conn.commit()
    else:
        print("[INFO] There are no tables in the database")


def main():
    inspector = inspect(sync_engine)
    tables = inspector.get_table_names()
    delete_all_tables(tables)


if __name__ == '__main__':
    main()
