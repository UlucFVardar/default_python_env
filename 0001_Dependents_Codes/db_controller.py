# -*- coding: UTF-8 -*-
#
# @author: Uluc Furkan Vardar
# @updatedDate: 17.01.2021
# @version: 1.0.0
# Universal Db Controllar class
import os
import datetime
import json


class msSQL_db_controller:
    def __init__(self, db_connection):
        import pymssql

        self.credentials = db_connection
        self.cnxn = pymssql.connect(
            server=self.credentials["server"],
            user=self.credentials["user"],
            password=self.credentials["password"],
            database=self.credentials["database"],
            host=self.credentials["host"],
        )

    def execute_only(self, sql):
        try:
            with self.cnxn.cursor() as cur:
                cur.execute(sql)
                self.cnxn.commit()
                try:
                    self.lastrowid = cur.lastrowid
                except Exception as e:
                    print(e)
                return True, None
        except Exception as e:
            if "Duplicate entry" in str(e):
                print(str(e), "sql : ,\n%s" % (sql))
                return False, "Duplicate entry"
            else:
                raise Exception(str(e), "sql : ,\n%s" % (sql))
        return False, None

    def execute_and_return(self, sql):
        try:
            with self.cnxn.cursor(as_dict=True) as cur:
                cur.execute(sql)
                # cur.as_dict
                # self.cnxn.commit()
                r = cur.fetchone()
                if r != None:
                    return r, None
                else:
                    return False, "No returned row!"
        except Exception as e:
            raise Exception(str(e), "sql : ,\n%s" % (sql))

    def execute_and_return_all(self, sql):
        try:
            with self.cnxn.cursor(as_dict=True) as cur:
                cur.execute(sql)
                # self.cnxn.commit()

                r = cur.fetchall()
                if r == None:
                    return False, "No returned row!"
                return r, None
        except Exception as e:
            raise Exception(str(e), "sql : ,\n%s" % (sql))

    def __del__(self):
        # print ("QUIT DB")
        try:
            self.cnxn.close()
        except Exception:
            pass


class mySQL_db_controller:
    def __init__(self, db_connection):
        self.lastrowid = None
        self.credentials = db_connection
        print(self.credentials)
        import pymysql

        try:
            self.conn = pymysql.connect(
                host=self.credentials["host"],
                user=self.credentials["user"],
                passwd=self.credentials["password"],
                db=self.credentials["database"],
                connect_timeout=5,
                charset="utf8",
                cursorclass=pymysql.cursors.DictCursor,
            )
        except Exception as e:
            # print (e)
            raise Exception("DB Connection Error", e)

    def execute_only(self, sql):
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)
                self.conn.commit()
                try:
                    self.lastrowid = cur.lastrowid
                except Exception as e:
                    print(e)
                return True, None
        except Exception as e:
            if "Duplicate entry" in str(e):
                print(str(e), "sql : ,\n%s" % (sql))
                return False, "Duplicate entry"
            else:
                raise Exception(str(e), "sql : ,\n%s" % (sql))
        return False, None

    def execute_and_return(self, sql):
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)
                field_names = [i[0] for i in cur.description]
                self.conn.commit()

                r = cur.fetchone()
                if r != None:
                    return r, None
                else:
                    return False, "No returned row!"
        except Exception as e:
            raise Exception(str(e), "sql : ,\n%s" % (sql))

    def execute_and_return_all(self, sql):
        d = []
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)

                self.conn.commit()

                r = cur.fetchone()
                if r == None:
                    return False, "No returned row!"
                while r != None:
                    d.append(r)
                    r = cur.fetchone()
        except Exception as e:
            raise Exception(str(e), "sql : ,\n%s" % (sql))
        return d, None

    def execute_and_return_cursor(self, sql):
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)
                self.conn.commit()
                return cur, None
        except Exception as e:
            raise Exception(str(e), "sql : ,\n%s" % (sql))
        return d, None

    def __del__(self):
        # print ("QUIT DB")
        try:
            self.conn.close()
        except Exception:
            pass



def get_connection_from_env(self):
    connection = {}
    try:
        connection = {
            "user": os.environ["DbUser"],
            "password": os.environ["DbPassword"],
            "database": os.environ["DbDatabase"],
            "host": os.environ["DbHost"],
        }
    except Exception as e:
        print("[Error] in getting connection infos from env values")
    return connection

def run_in_db(self, sql, operation_chosee, connection):
    from db_controller import mySQL_db_controller

    db_c = mySQL_db_controller(connection)
    sql = sql.replace("None", "null")
    try:
        if operation_chosee == "execute_and_return_all":
            resp, msg = db_c.execute_and_return_all(sql)
        elif operation_chosee == "execute_and_return":
            resp, msg = db_c.execute_and_return(sql)
        elif operation_chosee == "execute_only":
            resp, msg = db_c.execute_only(sql)
        elif operation_chosee == "execute_and_return_cursor":
            resp, msg = db_c.execute_and_return_cursor(sql)
        else:
            return None, "Wrong operation choosee"
    except Exception as e:
        return None, str(e)
    return resp, msg
def ex():
    from db_controller import msSQL_db_controller

    db_c = msSQL_db_controller(mssql_config)
    resp, msg = db_c.execute_only(sql)
    if msg != None:
        return {"status": msg}

    # MY SQL

    from db_controller import mySQL_db_controller

    db_c = mySQL_db_controller(mysql_config)
    resp, msg = db_c.execute_only(sql)
    if msg != None:
        return {"status": msg}
