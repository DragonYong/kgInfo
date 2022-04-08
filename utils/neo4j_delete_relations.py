#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-04-08 10:57
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    neo4j_delete_relations.py
# @Project: kgInof
from py2neo import Graph, NodeMatcher, RelationshipMatcher

g = Graph('http://192.168.19.3:7474', username='neo4j', password='password')

matcher = NodeMatcher(g)
r_matcher = RelationshipMatcher(g)
cat = matcher.match('Person', name='⭐cat').first()
dog = matcher.match('Person', name='⭐dog').first()

relation = r_matcher.match(nodes=[cat, dog]).first()
print(relation)
g.separate(relation)
