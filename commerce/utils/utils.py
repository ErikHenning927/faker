import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def chunked_iterable(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

def load_sql(filename, folder):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sql_path = os.path.join(base_dir, 'Pysql', folder, filename)
    
    with open(sql_path, 'r', encoding='utf-8') as file:
        return file.read()