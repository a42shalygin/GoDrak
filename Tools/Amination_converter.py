import os
import re
import unittest


class RynnConverter(object):

    bones = None
    animations = None

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


    def get_animations(self, path_to_file):

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
                        current_bone.animations.append(data[1:] + [0, 0, 0, 1])

        return animations



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

if __name__ == '__main__':
    conv = RynnConverter()
    animations = conv.get_animations(r'C:\Games\Drakan_ed\Psygnosis\Drakan\Drakan Dump\Common\System'
                                 r'\System [root]\Animations\Anim443 1handedRH.txt')
    pass
