# import hrpyc
#
# connection,hou=hrpyc.import_remote_module()
import hou
print hou
print (dir(hou.SopNodeType.sourcePath))

# node_list_a=[]
# for node in hou.nodeTypeCategories():
#     print node
#     node_list_a.append(node)
#
# print node_list_a


for sop_node in hou.sopNodeTypeCategory().nodeTypes().values():
    print sop_node
    print dir(sop_node)
    print sop_node.name()





