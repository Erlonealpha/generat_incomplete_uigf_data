import os
import json
from typing import List, Dict, Set
import pandas as pd

samplejson: dict = json.load(open('./samplejson.json', encoding='utf-8'))

class TPoolType():
    def __init__(self) -> None:
        self.type = '100' | '200' | '301' | '302' | '400'

class UigfJsonType():
    class uigfinfo():
        def __init__(self) -> None:
            self.uid = None
            self.lang = None
            self.export_time = None
            self.export_timestamp = None
            self.export_app = None
            self.export_app_version = None
            self.uigf_version = None
    class uigflist():
        def __init__(self) -> None:
            self.gacha_type = None
            self.time = None
            self.name = None
            self.item_type = None
            self.rank_type = None
            self.id = None
            self.uigf_gacha_type = None

    def __init__(self) -> None:
        self.info = self.uigfinfo()
        self.list = self.uigflist()
        self.lst_col = []
        self.lst_data = []
        self.time_lst = []
        self.tmpcontex = {
        'info':
            {
            'uid': self.info.uid,
            'lang': self.info.lang,
            'export_time': self.info.export_time,
            'export_timestamp': self.info.export_timestamp,
            'export_app': self.info.export_app,
            'export_app_version': self.info.export_app_version,
            'uigf_version': self.info.uigf_version
            },
        'list':
            {
            'gacha_type': self.list.gacha_type,
            'time': self.list.time,
            'name': self.list.name,
            'item_type': self.list.item_type,
            'rank_type': self.list.rank_type,
            'id': self.list.id,
            'uigf_gacha_type': self.list.uigf_gacha_type
            }
        }
        self.lst = []

    def parse(self, info, list):
        try:
            self.info.uid = info['uid'] if info['uid'] else None
            self.info.lang = info['lang'] if info['lang'] else None
            self.info.export_time = info['export_time'] if info['export_time'] else None
            self.info.export_timestamp = info['export_timestamp'] if info['export_timestamp'] else None
            self.info.export_app = info['export_app'] if info['export_app'] else None
            self.info.export_app_version = info['export_app_version'] if info['export_app_version'] else None
            self.info.uigf_version = info['uigf_version'] if info['uigf_version'] else None

            self.list.gacha_type = list['gacha_type'] if list['gacha_type'] else None
            self.list.time = list['time'] if list['time'] else None
            self.list.name = list['name'] if list['name'] else None
            self.list.item_type = list['item_type'] if list['item_type'] else None
            self.list.rank_type = list['rank_type'] if list['rank_type'] else None
            self.list.id = list['id'] if list['id'] else None
            self.list.uigf_gacha_type = list['uigf_gacha_type'] if list['uigf_gacha_type'] else None
        except:
            pass
        self.lst.append(self.tmpcontex)

        self.parse_to_df_lst()
    
    def parse_to_df_lst(self):
        for key, val in self.tmpcontex['info'].items():
            self.lst_col.append(key)
            self.lst_data.append(val)
        for key_, val_ in self.tmpcontex['list'].items():
            self.lst_col.append(key_)
            self.lst_data.append(val_)
            self.time_lst.append(self.list.time)

for key, val in samplejson.items():
    if key == "properties":
        info = val['info']["properties"]
        list = val['list']["items"]
        uigf = UigfJsonType()
        uigf.parse(info, list)

# 数据统计
df = pd.Series(column= uigf.lst_col, row= uigf.lst_data, index=uigf.time_lst)
