# Function to fetch image from MySQL
from my_utils.services import dbAccess


@dbAccess
def fetch_image(cursor, award_id):
    if cursor:
        sql_fetch_query = """SELECT title, img FROM awards WHERE id = %s"""
        cursor.execute(sql_fetch_query, (award_id,))
        record = cursor.fetchone()
        return record
    return None
