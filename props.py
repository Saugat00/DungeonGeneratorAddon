import bpy
import os


# get paths to find assets directory based on where addon is installed
addon_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(addon_dir, "assets")


# property group is needed in order for operators and UI to access them
class CustomProperties(bpy.types.PropertyGroup):
    matrix_rows: bpy.props.IntProperty(
        name="Length",
        description="Number of rows in the matrix",
        default=10,
        min=1, max=100,
    )

    matrix_columns: bpy.props.IntProperty(
        name="Width",
        description="Number of columns in the matrix",
        default=10,
        min=1, max=100,
    )

    assets_path: bpy.props.StringProperty(
        name="Assets",
        description="Object file directory",
        default=assets_dir,
        subtype='DIR_PATH',
    )

    delete_on_generate: bpy.props.BoolProperty(
        name="Auto Delete",
        description="If enabled, generating a new dungeon will delete the old one first",
        default=True,
    )

    maze_algorithm: bpy.props.EnumProperty(
        name="Algorithm",
        description="Select which maze generation algorithm should be used",
        items=(
            ('OP1', "Wilson's", ""),
            ('OP2', "Placeholder", ""),
        ),
    )

    maze_startx: bpy.props.IntProperty(
        name="x:",
        description="X-coordinate of dungeon starting point",
        default=0,
    )

    maze_starty: bpy.props.IntProperty(
        name="y:",
        description="Y-coordinate of dungeon starting point",
        default=0,
    )


def register():
    bpy.utils.register_class(CustomProperties)
    bpy.types.Scene.custom_props = bpy.props.PointerProperty(type=CustomProperties)

def unregister():
    bpy.utils.unregister_class(CustomProperties)
    del bpy.types.Scene.custom_props
