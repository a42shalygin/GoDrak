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
                        an = []
                        # an.append(data[1])
                        # an.append(data[4])
                        # an.append(data[7])
                        # an.append(data[7])
                        # an.append(data[10])
                        # an.append(data[2])
                        # an.append(data[5])
                        # an.append(data[8])
                        # an.append(data[11])
                        # an.append(data[3])
                        # an.append(data[6])
                        # an.append(data[9])
                        # an.append(data[12])
                        # an = an + ['0', '0', '0', '1']
                        an.append(data[1])
                        an.append(data[2])
                        an.append(data[3])
                        an.append("0")
                        an.append(data[4])
                        an.append(data[5])
                        an.append(data[6])
                        an.append("0")
                        an.append(data[7])
                        an.append(data[8])
                        an.append(data[9])
                        an.append("0")
                        an.append(data[10])
                        an.append(data[11])
                        an.append(data[12])
                        an.append("1")
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
    conv.get_animations(r"C:\Games\Drakan_ed\Psygnosis\Drakan\Drakan Dump\Common\System\System [root]\Animations\Anim507 run.txt", 'Anim507_run')
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
            sampler = ET.SubElement(animation_tag, 'sampler')
            sampler.set('id', fullname + '-sampler')
            channel = ET.SubElement(animation_tag, 'channel')
            channel.set('source', '#' + sampler.get('id'))
            channel.set('target', 'Armature_%s/transform' % anim.name)

            input_array = ET.SubElement(source_input, 'float_array')
            input_array.set('id', fullname + '-input-array')
            input_array.set('count', str(len(anim.timestamps)))
            input_array.text = '\n' + '\n'.join(anim.timestamps) + '\n'

            input_technique_common = ET.SubElement(source_input, 'technique_common')
            input_accessor = ET.SubElement(input_technique_common, 'accessor')
            input_accessor.set('source', '#' + input_array.get('id'))
            input_accessor.set('count', str(len(anim.timestamps)))
            input_accessor.set('stride', '1')

            input_accessor_param = ET.SubElement(input_accessor, 'param')
            input_accessor_param.set('name', 'TIME')
            input_accessor_param.set('type', 'float')

            output_array = ET.SubElement(source_output, 'float_array')
            output_array.set('id', fullname + '-output-array')
            output_array.set('count', str(len(anim.timestamps)*16))
            output_array.text = '\n'
            for an in anim.animations:
                output_array.text += ' '.join(an) + '\n'

            output_technique_common = ET.SubElement(source_output, 'technique_common')
            output_accessor = ET.SubElement(output_technique_common, 'accessor')
            output_accessor.set('source', '#' + output_array.get('id'))
            output_accessor.set('count', str(len(anim.timestamps) * 16))
            output_accessor.set('stride', '16')

            output_accessor_param = ET.SubElement(output_accessor, 'param')
            output_accessor_param.set('name', 'TRANSFORM')
            output_accessor_param.set('type', 'float4x4')

            interpolation_array = ET.SubElement(source_interpolation, 'Name_array')
            interpolation_array.set('id', source_interpolation.get('id') + '-array')
            interpolation_array.set('count', str(len(anim.timestamps)))
            nametext = 'LINEAR ' * len(anim.timestamps)  #WORNG ELEMENTS NUMER IS PRINTED. NOT COUNT, TEXT!
            interpolation_array.text = '\n' + '\n'.join(nametext.split(' '))

            interpolation_technique_common = ET.SubElement(source_interpolation, 'technique_common')
            interpolation_accessor = ET.SubElement(interpolation_technique_common, 'accessor')
            interpolation_accessor.set('source', '#' + interpolation_array.get('id'))
            interpolation_accessor.set('count', str(len(anim.timestamps)))
            interpolation_accessor.set('stride', '1')

            interpolation_accessor_param = ET.SubElement(interpolation_accessor, 'param')
            interpolation_accessor_param.set('name', 'INTERPOLATION')
            interpolation_accessor_param.set('type', 'name')

            sampler_input = ET.SubElement(sampler, 'input')
            sampler_input.set('semantic', 'INPUT')
            sampler_input.set('source', '#' + source_input.get('id'))
            sampler_output = ET.SubElement(sampler, 'input')
            sampler_output.set('semantic', 'OUTPUT')
            sampler_output.set('source', '#' + source_output.get('id'))
            sampler_interpolation = ET.SubElement(sampler, 'input')
            sampler_interpolation.set('semantic', 'INTERPOLATION')
            sampler_interpolation.set('source', '#' + source_interpolation.get('id'))



            indent(animation_tag)
            out_file.write(ET.tostring(animation_tag))



