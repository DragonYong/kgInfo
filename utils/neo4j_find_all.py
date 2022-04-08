#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-04-08 10:08
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    neo4j_find_all.py
# @Project: kgInof
from py2neo import Graph

graph = Graph('http://192.168.19.3:7474', username='neo4j', password='password')

nodes = graph.nodes.match()

for node in nodes:
    print(node)
print(node.items())
print('-')
print(node.labels)
