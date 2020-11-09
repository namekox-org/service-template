# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


import sqlalchemy as sa
import sqlalchemy_utils as su


from .base import Model


class Result(Model, su.Timestamp):
    __tablename__ = 'result'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    ip = sa.Column(su.IPAddressType, nullable=False)
    alive = sa.Column(sa.Boolean, nullable=False)
