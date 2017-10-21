bl_info = {
    "name": "Blender2Urho3D_RenameNode",
    "description": "A Blender plugin to rename all the Empty Scaffolding from Name.001, Name.002, etc to just Name",
    "author": "stark7",
    "version": (0,0),
    "blender": (2, 66, 0),
    "location": "Properties > Render > Blender2Urho3D_RenameNode",
    "warning": "99 little bugs in the code. 99 little bugs in teh code. Take one down, patch it around. 127 little bugs in the code...",
    "wiki_url":"",
    "tracker_url":"",
    "category": "Object",
}

import bpy

class Blender2Urho3D_RenameNode(bpy.types.Operator):
    """My Object Moving Script"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "blender2urho3d.renamenode"        # unique identifier for buttons and menu items to reference.
    bl_label = "RenameNode"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.

        # The original script
        scene = context.scene
        for obj in scene.objects:
            if not obj.type == 'EMPTY':
                continue

            nameArr = obj.name.split('.')

            if len(nameArr) < 2:
                continue

            name = nameArr[0]

            if not name.endswith('Node'):
                continue

            obj.name = nameArr[0]

        return {'FINISHED'}            # this lets blender know the operator finished successfully.

def register():
    bpy.utils.register_class(Blender2Urho3D_RenameNode)


def unregister():
    bpy.utils.unregister_class(Blender2Urho3D_RenameNode)

if __name__ == "__main__":
	register()