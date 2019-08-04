#coding=utf-8
#author:Jonathon Woo
#version:1.0.0
import hou

selected_nodes = hou.selectedNodes()
for node in selected_nodes:
    #get current location
    current_level = node.parent()
    #get node name as the rop node new name
    node_name = node.name()
    #create rop_fbx
    rop_node = current_level.createNode("rop_fbx","fbx_bk_%s"%node_name)
    #set_connected
    rop_node.setInput(0,node)
    #get node position
    tar_x, tar_y = node.position()
    tar_y -= 1
    rop_node.setPosition([tar_x,tar_y])
    #set output path to read $OS
    #rawValue()-------------get node parm raw value
    rop_node.parm("sopoutput").set("$HIP/$OS.fbx")