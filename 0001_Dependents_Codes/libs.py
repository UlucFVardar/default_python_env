# -*- coding: UTF-8 -*-
from datetime import date
import re
import json
import time
import os
import sys
import copy
import uuid
import datetime
import boto3
from dateutil.relativedelta import *


class my_functions:
    # Use this class as globaly in manager
    def __init__(self, build_params_path="./CodeBuild_templateParameter.json"):
        print("YARATILAN api_f OBJESIIII")
        self.build_params_json = json.loads( open(build_params_path, "r", encoding="utf-8").read() )["Parameters"]

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
