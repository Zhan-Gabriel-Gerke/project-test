from dbquery import *
from TkinterFile import *
import random
def del_record(current_user,ID):
    opendb()
    try:
        sql = (f"DELETE FROM {current_user} WHERE ID={ID}")
        curs.execute(sql)
        conn.commit()
        return True
    except sqlite3.Error as e:
        tk.messagebox.showerror("showerror def del_record", e)