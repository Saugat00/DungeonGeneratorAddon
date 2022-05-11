from .maze_parser.wilsons_algorithm import wilsons_algorithm
import bpy
from bpy import context
import time as ti
import os
import random
import math


# generate dungeon button operator
class FMDun(bpy.types.Operator):
    """Dungeon Generator"""
    bl_idname = "object.dungeon"
    bl_label = "Dungeon Generator"
    bl_options = {'REGISTER'}
         
    def execute(self, context):
        scene = context.scene
        custom_props = scene.custom_props
        obj = context.active_object

        if (custom_props.delete_on_generate):
            self.delete_collection()

        #  M = self.binary_tree_populate(custom_props.matrix_rows, custom_props.matrix_columns)
        # for i in range(custom_props.matrix_rows):
        #     for j in range(custom_props.matrix_columns):
        M = wilsons_algorithm(h=15, w=15)
        M.print_path()
        for i in range(15):
            for j in range(15):
                self.make_object_model(M.path[i][j], obj, i, j, custom_props)

        return {'FINISHED'}

    # deletes all objects in the default collection
    def delete_collection(self):
        collection_name = "Collection"
        collection = bpy.data.collections[collection_name]
        meshes = set()

        for cur_obj in [o for o in collection.objects if o.type == 'MESH']:
            meshes.add(cur_obj.data)
            bpy.data.objects.remove(cur_obj)

        for mesh in [m for m in meshes if m.users == 0]:
            bpy.data.meshes.remove(mesh)
        return "SuccessFul"


    # returns a matrix populated with random letters corresponding to our
    # modeled .obj files
    def randomly_populate_matrix(self, h, w):
        mat = [[0 for i in range(w)] for j in range(h)]
        object_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "s", "t", "u", "v"]

        for i in range(h):
            for j in range(w):
                mat[i][j] = random.choice(object_list)
                
        return mat




    # -------------------------------------------------------------------------
    # |                     Ignore this for now                               |
    # -------------------------------------------------------------------------
    # returns a matrix populated with letters corresponding to our modeled
    # .obj files using binary tree algorithm
    # def binary_tree_populate(self, length, width):
    #     mat = [[0 for i in range(width)] for j in range(length)]

    #     north = ["a", "e", "f"]
    #     south = ["a", "c", "d"]
    #     west = ["b", "c", "f"]
    #     east = ["b", "d", "e"]

    #     not_north = ["b", "c", "d"]
    #     not_west = ["a", "d", "e"]

    #     not_north_west = ["0", "d"]

    #     # north = ["a"]
    #     # west = ["b"]
    #     # north_or_west = ["a", "b"]

    #     for i in range(length):
    #         for j in range(width):

    #             # top row
    #             if (i == 0):
    #                 mat[i][j] = random.choice(not_north)

    #             # left column
    #             elif (j == 0):
    #                 mat[i][j] = random.choice(not_west)

    #             else:
    #                 mat[i][j] = random.choice(not_north_west)

    #     return mat

        # HALLWAYS
            # a = NS
            # b = EW

        # CORNERS
            # c = SW
            # d = SE
            # e = NE
            # f = NW

        # DEADENDS
            # g = S
            # h = E
            # i = N
            # j = W

        # ENTRANCES
            # s
            # t = W opening, WE
            # u
            # v = E opening, WE


    # takes the an element of the matrix and places it in Blender
    def make_object_model(self, letter, obj, x, y, custom_props, *args, **kwargs):
        if(letter == "0"):
            return

        def_object_string_name = letter + ".obj"
        def_value=(x * 3 + custom_props.maze_startx, y * 3 + custom_props.maze_starty, 0.0)
        def_orient_type='GLOBAL'
        def_orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))
        def_orient_matrix_type='GLOBAL'
        def_mirror=True
        def_use_proportional_edit=False
        def_proportional_edit_falloff='SMOOTH'
        def_proportional_size=1
        def_use_proportional_connected=False
        def_use_proportional_projected=False
        if "value" in kwargs:
            def_value = kwargs.get("value")
        if "orient_type" in kwargs:
            def_orient_type = kwargs.get("orient_type")
        if "orient_matrix" in kwargs:
            def_orient_matrix = kwargs.get("orient_matrix")
        if "orient_matrix_type" in kwargs:
            def_orient_matrix_type  = kwargs.get("orient_matrix_type")
        if "mirror" in kwargs:
            def_mirror = kwargs.get("mirror")
        if "use_proportional_edit" in kwargs:
            def_use_proportional_edit = kwargs.get("use_proportional_edit") 
        if "proportional_edit_falloff" in kwargs:
            def_proportional_edit_falloff = kwargs.get("proportional_edit_falloff")
        if "proportional_size" in kwargs:
            def_proportional_size = kwargs.get("proportional_size")
        if "use_proportional_connected" in kwargs:
            def_use_proportional_connected = kwargs.get("use_proportional_connected") 
        if "use_proportional_projected" in kwargs:
            def_use_proportional_projected = kwargs.get("use_proportional_projected")

        try:
            obj_model = bpy.ops.import_scene.obj(filepath = os.path.join(custom_props.assets_path,
                def_object_string_name))
        except:
            # if user sets invalid path, reset to default
            custom_props.property_unset("assets_path")
            obj_model = bpy.ops.import_scene.obj(filepath = os.path.join(custom_props.assets_path,
                def_object_string_name))

        bpy.ops.transform.translate(
                value=def_value,
                orient_type=def_orient_type,
                orient_matrix=def_orient_matrix,
                orient_matrix_type=def_orient_matrix_type,
                mirror=def_mirror,
                use_proportional_edit=def_use_proportional_edit,
                proportional_edit_falloff=def_proportional_edit_falloff,
                proportional_size=def_proportional_size,
                use_proportional_connected=def_use_proportional_connected,
                use_proportional_projected=def_use_proportional_projected
        )
        bpy.ops.transform.rotate(value=3.0*math.pi/2.0, orient_axis='Z')



# delete button operator
class Delete(bpy.types.Operator):
    bl_idname = "object.delete_all"
    bl_label = "Delete All"

    def execute(self, context):
        scene = context.scene
        collection_name = "Collection"
        collection = bpy.data.collections[collection_name]
        meshes = set()

        for cur_obj in [o for o in collection.objects if o.type == 'MESH']:
            meshes.add(cur_obj.data)
            bpy.data.objects.remove(cur_obj)

        for mesh in [m for m in meshes if m.users == 0]:
            bpy.data.meshes.remove(mesh)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(FMDun)
    bpy.utils.register_class(Delete)

def unregister():
    bpy.utils.unregister_class(FMDun)
    bpy.utils.unregister_class(Delete)
