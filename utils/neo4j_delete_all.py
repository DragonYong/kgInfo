#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-04-08 11:23
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    neo4j_delete_all.py
# @Project: kgInof
from py2neo import Graph

graph = Graph('http://192.168.19.3:7474', username='neo4j', password='password')
graph.delete_all()
