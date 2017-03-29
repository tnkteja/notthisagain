#!/usr/bin/python
# coding:utf-8

def getpath(tree,value):
  path=[]
  node=tree
  while node and node.data != value:
    path.append(node)
    if node.data < value:
      node=node.left
    else:
      node=node.right
  path.append(node)
  
  return path

