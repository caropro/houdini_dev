# -*- coding: utf-8 -*-
import hou
import os
input_path="test"

current_path=hou.hscriptExpression("$HIPFILE")
current_file=hou.hscriptExpression("$HIPNAME")

current_folder=current_path.split("/")[-1]

abc_name=current_file+".abc"
render_ame=current_file+".$F4.exr"

root_path=current_path.split(current_folder)[0]
abc_output_path=os.path.normpath(os.path.join(root_path,"abc",current_file,abc_name))
render_path=os.path.normpath(os.path.join(root_path,"render",current_file,render_ame))

abc_in=hou.node("/obj").createNode("geo","alembic_reader")
hou.node("/obj/alembic_reader/file1").destroy()
abc_input=abc_in.createNode("alembic","Input_alembic")
abc_input.parm("fileName").set(input_path)

abc_out=hou.node("/obj").createNode("geo","alembic_output")
hou.node("/obj/alembic_output/file1").destroy()
abc_output=abc_out.createNode("rop_alembic","Output_abc")
abc_output.parm("filename").set(abc_output_path)
abc_output.parm("trange").set(1)

render=hou.node("/out").createNode("ifd","mantra_render")
render.parm("vm_picture").set(render_path)
render.parm("trange").set(1)

print
