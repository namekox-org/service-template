# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


import random
import sqlalchemy as sa


from namekox_webserver.core.entrypoints.app import app
from namekox_timer.core.entrypoints.timer import timer
from namekox_sqlalchemy.core.dependencies import Database


from . import models, schema
from .models.base import Model
from .common.generator import generate_ip


class Ping(object):
    name = 'ping'
    db = Database(name, Model, engine_options={'pool_pre_ping': True})

    @app.api('/api/ping/<ip>/', methods=['GET'])
    def ping_res(self, request, ip=None):
        results = self.db.query(models.Result).filter(
            models.Result.ip == ip
        ).order_by(
            sa.desc(models.Result.created)
        )
        return schema.ResultListSchema(many=True).dump(results).data

    @timer(5)
    def ip_ping(self):
        result = models.Result(ip=generate_ip(), alive=random.choice([True, False]))
        self.db.add(result)
        self.db.commit()
