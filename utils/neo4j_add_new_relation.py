#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-04-08 10:54
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    neo4j_add_new_relation.py
# @Project: kgInof
from py2neo import Graph, Relationship, NodeMatcher

g = Graph('http://192.168.19.3:7474', username='neo4j', password='password')

matcher = NodeMatcher(g)

fugui = matcher.match('Person', name='⭐徐福贵').first()
youqian = matcher.match('Person', name='⭐徐有钱').first()

relation = Relationship(fugui, 'Brother', youqian)

g.create(relation)
