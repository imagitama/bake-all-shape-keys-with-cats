import textwrap
import bpy

bl_info = {
    # required
    'name': 'Bake All Shape Keys With CATS',
    'blender': (3, 1, 0),
    'category': 'Object',
    # optional
    'version': (1, 0, 0),
    'author': 'Jared Williams',
    'description': 'Bakes shape keys with _bake suffix.',
}


class BakeAllShapeKeysWithCatsPanel(bpy.types.Panel):
    bl_label = 'Bake All Shape Keys With CATS'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        wrapper = textwrap.TextWrapper()
        list = wrapper.wrap(
            text='Select a mesh that has shape keys with _bake in them.')
        for text in list:
            row = layout.row(align=True)
            row.alignment = 'EXPAND'
            row.label(text=text)
        col = layout.column()
        for (prop_name, _) in PROPS:
            row = col.row()
            row.prop(context.scene, prop_name)
        layout.operator('baskwc.bake_all_shape_keys_with_cats', text='Bake')

    def execute(self, context):
        if self.action == 'CLEAR':
            self.do_it(context=context)

    def do_it(context):
        print('Doing it!')


class BakeAllShapeKeysWithCats(bpy.types.Operator):
    bl_idname = "baskwc.bake_all_shape_keys_with_cats"
    bl_label = "Bake All Shape Keys With CATS"
    bl_options = {"UNDO"}

    def invoke(self, context, event):
        mesh = context.scene.Mesh
        mesh.select_set(True)
        bpy.context.view_layer.objects.active = mesh
        print('Applying shape keys to basis...')
        bpy.ops.object.shape_key_add(from_mix=True)
        bpy.ops.cats_shapekey.shape_key_to_basis()
        for index, shape_key in enumerate(mesh.data.shape_keys.key_blocks):
            if '_bake' in shape_key.name:
                print('Found shape key', shape_key.name)
                mesh.shape_key_remove(shape_key)
        print('Job complete')
        return {"FINISHED"}


CLASSES = [
    BakeAllShapeKeysWithCats,
    BakeAllShapeKeysWithCatsPanel
]

PROPS = [
    ('Mesh', bpy.props.PointerProperty(name="Mesh", type=bpy.types.Object)),
]


def register():
    for (prop_name, prop_value) in PROPS:
        setattr(bpy.types.Scene, prop_name, prop_value)

    for klass in CLASSES:
        bpy.utils.register_class(klass)


def unregister():
    for (prop_name, _) in PROPS:
        delattr(bpy.types.Scene, prop_name)

    for klass in CLASSES:
        bpy.utils.unregister_class(klass)


if __name__ == '__main__':
    register()
