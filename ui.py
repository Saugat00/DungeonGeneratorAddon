import bpy
import bpy.utils.previews
import os

# this class extends bpy.types.Panel and contains everything for the UI
class DungeonPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Dungeon"
    bl_label = "Generator"

    # draw function is required for a panel to show up, even if the function
    # does nothing
    def draw(self, context):
        # these statements are mostly for convenience
        # e.g. type custom_props instead of context.scene.custom_props.xxxx
        layout = self.layout
        scene = context.scene
        custom_props = scene.custom_props

        # needed for the custom icons to be shown on the buttons
        pcoll = preview_collections["main"]
        maze_icon = pcoll["maze_icon"]
        delete_icon = pcoll["delete_icon"]

        # creates a column to group the sliders together
        slider_col = layout.column(align=True)
        slider_col.label(text="Dungeon Region")
        slider_col.prop(custom_props, 'matrix_rows')
        slider_col.prop(custom_props, 'matrix_columns')
        # groups the coordinates into a row, so x and y are side by side in the panel
        start_row = slider_col.row(align=True)
        start_row.prop(custom_props, 'maze_startx')
        start_row.prop(custom_props, 'maze_starty')

        # adds additional spacing between menu components
        layout.separator()

        # assets directory
        layout.prop(custom_props, 'assets_path', text="Assets")
        # adds dropdown to select which maze generation algorithm should be used
        layout.prop(custom_props, 'maze_algorithm')

        layout.separator()

        # adds a checkbox for deleting the previous objects before generating a new dungeon
        layout.prop(custom_props, 'delete_on_generate')

        layout.separator()

        # group together the buttons
        button_col = layout.row(align=True)
        button_col.operator('object.dungeon', text='Generate', icon_value=maze_icon.icon_id)
        button_col.operator('object.delete_all', text='Delete All', icon_value=delete_icon.icon_id)

# needed for custom icons
preview_collections = {}
addon_dir = os.path.dirname(os.path.abspath(__file__))
icon_dir = os.path.join(addon_dir, "icons")
gen_icon_path = os.path.join(icon_dir, "maze.png")
del_icon_path = os.path.join(icon_dir, "delete.png")

def register():
    bpy.utils.register_class(DungeonPanel)
    pcoll = bpy.utils.previews.new()
    pcoll.load("maze_icon", gen_icon_path, 'IMAGE')
    pcoll.load("delete_icon", del_icon_path, 'IMAGE')
    preview_collections["main"] = pcoll

def unregister():
    bpy.utils.unregister_class(DungeonPanel)
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
