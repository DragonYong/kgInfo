#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-04-08 10:56
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    neo4j_delete_links.py
# @Project: kgInof
from py2neo import Graph, NodeMatcher, RelationshipMatcher

g = Graph('http://192.168.19.3:7474', username='neo4j', password='password')

matcher = NodeMatcher(g)
r_matcher = RelationshipMatcher(g)
fugui = matcher.match('Person', name='⭐徐福贵').first()
youqian = matcher.match('Person', name='⭐徐有钱').first()

relation = r_matcher.match(nodes=[fugui, youqian]).first()
print(relation)
g.delete(relation)
