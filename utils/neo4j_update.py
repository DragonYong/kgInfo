#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-04-08 10:49
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    neo4j_update.py
# @Project: kgInof

from py2neo import Graph, Node, Relationship, NodeMatcher, Subgraph

g = Graph('http://192.168.19.3:7474', username='neo4j', password='password')

from py2neo import Graph, NodeMatcher

tx = g.begin()
# 找到你要找的Nodes
matcher = NodeMatcher(g)

# 修改单个节点
# init_node = matcher.match("Person", name="福贵")
# new_node = init_node.first()
# new_node['name'] = "徐福贵"
# sub = Subgraph(nodes=[new_node])
# tx.push(sub)
# tx.commit()

# 修改多个节点
init_node = matcher.match("Person")
new_nodes = []
for node in init_node.all():
    node['name'] = '⭐'+node['name']
    new_nodes.append(node)

sub = Subgraph(nodes=new_nodes)
tx.push(sub)
tx.commit()