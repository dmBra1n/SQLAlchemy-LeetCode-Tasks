from models import metadata_obj
from sqlalchemy import text
from tabulate import tabulate

from utils.database import session_factory, sync_engine


class SyncCore:
    @staticmethod
    def create_tables():
        metadata_obj.reflect(bind=sync_engine)
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)

    @staticmethod
    def insert_data(sql_file_path):
        try:
            with session_factory() as session, open(sql_file_path, "r") as file:
                sql_queries = file.readlines()
                for query in sql_queries:
                    session.execute(text(query.strip()))
                session.commit()

        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")

    @staticmethod
    def followers_count():
        with session_factory() as session:
            query = (
                """SELECT user_id, COUNT(follower_id) AS followers_count
                FROM Followers
                GROUP BY user_id
                ORDER BY user_id"""
            )
            res = session.execute(text(query))
            result = res.all()
            headers = ["user_id", "followers_count"]
            print(tabulate(result, headers=headers, tablefmt='psql'))
