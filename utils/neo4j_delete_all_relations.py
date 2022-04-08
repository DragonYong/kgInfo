#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-04-08 11:03
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    neo4j_delete_all_relations.py
# @Project: kgInof
from py2neo import Graph, Subgraph, RelationshipMatcher

g = Graph('http://192.168.19.3:7474', username='neo4j', password='password')
matcher = RelationshipMatcher(g)
tx = g.begin()
relationship_list = matcher.match().all()

node_list = Subgraph(relationships=relationship_list)

tx.separate(node_list)
tx.commit()
