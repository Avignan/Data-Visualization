import json
import traceback
import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd

def get_db_data(job_title, year):
    try:
        # Connect to the database
        conn = psycopg2.connect(database="your_database", user="your_user", password="user_password",
                                host="your_host", port="your_port")
        # Open a cursor to perform database operations
        cur = conn.cursor(cursor_factory=RealDictCursor)
        # Execute a SELECT query
        cur.execute("SELECT * FROM public.job_growth_dataset WHERE job_title=%s and year=%s", (job_title, year))
        # Fetch the results
        rows = cur.fetchall()
        # Process the results
        data_list_dict = []
        for row in rows:
            data_list_dict.append(dict(row))

        # Close the cursor and connection
        cur.close()
        conn.close()
        return data_list_dict
    except Exception as error:
        traceback.print_stack(error)
        return {}



if __name__ == "__main__":
    get_db_data('Data Scientist', '2022')