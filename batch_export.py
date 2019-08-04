#coding=utf-8
#author:Jonathon Woo
#version:1.0.0
import hou

selected_nodes = hou.selectedNodes()
for node in selected_nodes:
    #if selected node has parm "excute" then do the render
    if node.parm("execute"):
        node.render()

