from typing import List, Tuple
import MySQLdb
from MySQLdb import cursors

from typing import Tuple

def inquire_new_posts(cur: cursors.Cursor, after_datetime : str) -> Tuple[Tuple[str, int]]:
    """指定時刻以降のPostをDBに問い合わせ、本文とスレッドIDを返す"""
    cur.execute("SELECT text, thread_id FROM board_post WHERE created_at > %s;", [after_datetime])
    return cur.fetchall()

