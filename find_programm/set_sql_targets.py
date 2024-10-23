import sqlite3
import colorama 

def set_sql_targets():
    # اتصال به دیتابیس
    conn = sqlite3.connect('../../programs.db')
    cursor = conn.cursor()

    # حذف سطرهای تکراری بر اساس ستون‌های name, bounty, targets, platform
    cursor.execute("DELETE FROM TARGETS WHERE id NOT IN (SELECT MIN(id) FROM TARGETS GROUP BY name, bounty, targets, platform)")

    # ذخیره تغییرات
    conn.commit()

    # بستن اتصال
    conn.close()
    print(colorama.Fore.YELLOW+"DELETE DUPLICATION IS DONE"+'\n'+colorama.Style.RESET_ALL)
