#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-04-08 11:02
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    neo4j_batch_add.py
# @Project: kgInof

from py2neo import Graph, Node, Subgraph

g = Graph('http://192.168.19.3:7474', username='neo4j', password='password')

tx = g.begin()
node_list = [Node("Num", name=str(i)) for i in range(4)]

node_list = Subgraph(nodes=node_list)

tx.create(node_list)
tx.commit()
