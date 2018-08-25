import os
import re
import unittest


class RynnConverter(object):

    bones = None
    animations = None
    name = None

    def __init__(self):
        self.bones = []
        self.bones.append('wrynn')
        self.bones.append('upperbody')
        self.bones.append('torso')
        self.bones.append('chest')
        self.bones.append('neck')
        self.bones.append('head')
        self.bones.append('hair1')
        self.bones.append('hair2')
        self.bones.append('hair3')
        self.bones.append('Lcollar')
        self.bones.append('Luparm')
        self.bones.append('Lforearm')
        self.bones.append('Lhand')
        self.bones.append('Lweapon')
        self.bones.append('Rcollar')
        self.bones.append('Ruparm')
        self.bones.append('Rforearm')
        self.bones.append('Rhand')
        self.bones.append('Rweapon')
        self.bones.append('Backsheath')
        self.bones.append('lowerbody')
        self.bones.append('Rhip')
        self.bones.append('Rtigh')
        self.bones.append('Rcalf')
        self.bones.append('Rfoot')
        self.bones.append('Rtoe')
        self.bones.append('Rsheath')
        self.bones.append('Lhip')
        self.bones.append('Ltigh')
        self.bones.append('Lcalf')
        self.bones.append('Lfoot')
        self.bones.append('Ltoe')
        self.bones.append('Lsheath')


    def get_animations(self, path_to_file, name):
        self.name = name

        animations = []
        if not os.path.isfile(path_to_file):
            raise IOError('not a file %s' % path_to_file)

        with open(path_to_file) as in_file:
            current_bone = None
            for line in in_file:
                if line.count('Node') > 0:
                    number = re.search('Node (\\d+)', line)
                    if number:
                        current_bone = self.BoneAnimation(self.bones[int(number.groups()[0])])
                        print('Bone %s' % current_bone.name)
                        animations.append(current_bone)
                else:
                    data = re.findall('(-?\\d+\\.\\d+)', line)
                    if data and current_bone:
                        current_bone.timestamps.append(data[0])
                        an = data[1:] + ['0', '0', '0', '1']
                        current_bone.animations.append(an)

        self.animations = animations



    class BoneAnimation(object):

        timestamps = None
        animations = None
        name = None

        def __init__(self, name):
            self.timestamps = []
            self.animations = []
            self.name = name

# class TestRynn(unittest.TestCase):
#
#     def setUp(self):
#         self.Rynn = RynnConverter()
#
#     def test_wrynn(self):
#         self.assertEquals(self.Rynn.bones[0], 'wrynn')
#
#     def test_upperbody(self):
#         self.assertEquals(self.Rynn.bones[1], 'upperbody')
#
#     def test_lowerbody(self):
#         self.assertEquals(self.Rynn.bones[20], 'lowerbody')
#
#     def test_Ltoe(self):
#         self.assertEquals(self.Rynn.bones[31], 'Ltoe')
#
#     def test_Lsheath(self):
#         self.assertEquals(self.Rynn.bones[32], 'Lsheath')
#
#     def test_len(self):
#         self.assertEquals(len(self.Rynn.bones), 33)
#

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

if __name__ == '__main__':
    conv = RynnConverter()
    conv.get_animations(r'C:\Games\Drakan_ed\Psygnosis\Drakan\Drakan Dump\Common\System'
                                 r'\System [root]\Animations\Anim443 1handedRH.txt', 'Anim443_1handedRH')
    with open('tmp', 'w') as out_file:
        import xml.etree.ElementTree as ET
        for anim in conv.animations:
            fullname = conv.name + '_' + anim.name
            animation_tag = ET.Element('animation')
            animation_tag.set('id', fullname)
            source_input = ET.SubElement(animation_tag, 'source')
            source_input.set('id', fullname + '-input')
            source_output = ET.SubElement(animation_tag, 'source')
            source_output.set('id', fullname + '-output')
            source_interpolation = ET.SubElement(animation_tag, 'source')
            source_interpolation.set('id', fullname + '-interpolation')
            sampler = ET.SubElement(animation_tag, 'source')
            sampler.set('id', fullname + '-sampler')
            channel = ET.SubElement(animation_tag, 'source')
            channel.set('source', '#' + sampler.get('id'))
            channel.set('target', 'Armature_%s/transform' % anim.name)

            input_array = ET.SubElement(source_input, 'float array')
            input_array.set('id', fullname + '-input-array')
            input_array.set('count', str(len(anim.timestamps)))
            input_array.text = '\n' + '\n'.join(anim.timestamps) + '\n'

            input_technique_common = ET.SubElement(source_input, 'technique common')
            input_accessor = ET.SubElement(input_technique_common, 'accessor')
            input_accessor.set('source', '#' + input_array.get('id'))
            input_accessor.set('count', str(len(anim.timestamps)))
            input_accessor.set('stride', '1')

            output_array = ET.SubElement(source_output, 'float array')
            output_array.set('id', fullname + '-output-array')
            output_array.set('count', str(len(anim.timestamps)*16))
            output_array.text = '\n'
            for an in anim.animations:
                output_array.text += ' '.join(an) + '\n'

            output_technique_common = ET.SubElement(source_output, 'technique common')
            output_accessor = ET.SubElement(input_technique_common, 'accessor')
            output_accessor.set('source', '#' + output_array.get('id'))
            output_accessor.set('count', str(len(anim.timestamps) * 16))
            output_accessor.set('stride', '16')

            output_accessor_param = ET.SubElement(output_accessor, 'param')
            output_accessor_param.set('name', 'TRANSFORM')
            output_accessor_param.set('type', 'float4x4')

            indent(animation_tag)
            out_file.write(ET.tostring(animation_tag))



