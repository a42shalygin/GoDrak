import os
import shutil
import unittest
import REOConverter
import OBJConverter


class TestOBJConverter(unittest.TestCase):

    def test(self):
        pass


class TestREOConverter(unittest.TestCase):

    def test(self):
        pass

    def test_zero_materials(self):
        # If there is a model with no texture the entry is ex.: 0 Texture(0)
        # For these definitions the converter would crash due index out of range
        pass


class IntegrationTests(unittest.TestCase):

    def test_back_and_forth(self):
        in_reo = 'reo/original'
        temp_obj = 'obj/1st_pass'
        out_reo = 'reo/recovnerted'
        out_obj = 'obj/2nd_pass'
        if os.path.exists(temp_obj):
            shutil.rmtree(temp_obj)
        if os.path.exists(out_reo):
            shutil.rmtree(out_reo)
        if os.path.exists(out_obj):
            shutil.rmtree(out_obj)
        os.makedirs(temp_obj)
        os.makedirs(out_reo)
        os.makedirs(out_obj)
        REOConverter.convert_reo_to_obj(in_reo + '/SmallHouse(M)01.reo', temp_obj + '/SmallHouse(M)01.obj')
        OBJConverter.convert_obj_to_reo(temp_obj + '/SmallHouse(M)01.obj', out_reo + '/SmallHouse(M)01.reo')
        # self.assertEquals(out_reo_file, in_reo_file)
        REOConverter.convert_reo_to_obj(out_reo + '/SmallHouse(M)01.reo', out_obj + '/SmallHouse(M)01.obj')
        # self.assertEquals(first_obj, reconverted_obj)

