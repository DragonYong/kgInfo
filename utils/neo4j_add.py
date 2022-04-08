#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-04-08 10:49
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    neo4j_add.py
# @Project: kgInof
from py2neo import Graph, Node, Relationship
from py2neo import Subgraph

graph = Graph('http://192.168.19.3:7474', username='neo4j', password='password')
print(graph)
tx = graph.begin()
jiazhen = Node("Person", name='陈家珍', age=66)
fugui = Node("Person", name='徐福贵', age=67)
youqian = Node("Person", name='徐有钱')
renxing = Node("Person", name='徐任性')

cat = Node("Person", name='cat')
dog = Node("Person", name='dog')

wife = Relationship(fugui, "WIFE", jiazhen)
brother_1 = Relationship(fugui, "BROTHER", youqian)
brother_2 = Relationship(fugui, "BROTHER", renxing)
hus = Relationship(jiazhen, 'HUS', fugui)
know = Relationship(cat, 'KNOWS', dog)

relation_list = Subgraph(relationships=[wife, brother_2, brother_1, hus, know])

tx.create(relation_list)
tx.commit()