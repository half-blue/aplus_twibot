from typing import List, Tuple
import MySQLdb
from MySQLdb import cursors, connections

def mysql_connect(user: str, password: str, host: str, db_name: str, port: int = 3306) -> connections.Connection:
    """MySQLのコネクションを得る"""
    conn = MySQLdb.connect(host=host, port=port,
                           db=db_name, user=user, password=password)
    return conn


def inquire_new_posts(cur: cursors.Cursor, after_datetime: str) -> Tuple[Tuple[str, int]]:
    """指定時刻以降のPostをDBに問い合わせ、本文とスレッドIDを返す"""
    cur.execute("SELECT text, thread_id FROM board_post WHERE created_at > %s;", [
                after_datetime])
    return cur.fetchall()
