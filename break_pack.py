#Auther:Jonathon Woo
#version:001
#edition:001
#coding=utf-8
import hou
current_selection_nodes = hou.selectedNodes()

for selected_node in current_selection_nodes:
    node_geo = selected_node.geometry()
    #get name attribute list
    name_list = list(set(node_geo.primStringAttribValues("name")))
    if not name_list:
        continue
    name_list.sort()
    #blast the geo according to the name list
    index_pos = 0
    current_name_root=""
    for name in name_list:
        name_root = name[:-3]
        blast_node = hou.node(selected_node.parent().path()).createNode("blast",name)
        blast_node.parm("group").set("@name=%s"%name)
        blast_node.parm("negate").set(1)
        blast_node.setInput(0,selected_node)
        if current_name_root not in name_root:
            index_pos+=1
        print(name_root)
        print(index_pos*5)
        blast_node.setPosition([index_pos*5,0])
        current_name_root = name_root

