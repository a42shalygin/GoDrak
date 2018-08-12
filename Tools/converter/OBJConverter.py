'''
Created on 11.08.2016

@author: BuXXe
'''
import re

import OBJClass
import os
import argparse


def convert_obj_to_reo(in_file, out_file):
    # read the obj file
    with open(in_file, 'r') as f:
        read_data = f.readlines()

    filename = os.path.basename(in_file)[:-4]
    # TODO: perhaps use only regex in future but for now keep it simple
    # TODO: perhaps we should use some kind of grammar or state machine to parse the file

    # iterate through the read_data
    linecounter = 0

    # create new object
    OBJ = OBJClass.OBJ()

    # set filename as model name
    # Change this if you want a different name
    OBJ.name = filename

    # INFO: Comments and empty lines will be ignored as for now
    while linecounter < len(read_data):
        if read_data[linecounter][0] == '#' or read_data[linecounter][0] == '\n':
            linecounter += 1
            continue

        # Build material dictionary
        elif read_data[linecounter].startswith("mtllib"):
            mtlfile = read_data[linecounter].replace("mtllib ", "", 1).replace("\n", "")
            # read the mtl file
            mtlpath = os.path.join(os.path.dirname(in_file), mtlfile)
            if not os.path.isfile(mtlpath):
                print('ERROR: Failed to open material file %s' % mtlpath)
                continue
            with open(mtlpath, 'r') as f:
                mtl_data = f.readlines()
                f.close()

            mtl_linecounter = 0
            while mtl_linecounter < len(mtl_data):
                if mtl_data[mtl_linecounter].startswith("newmtl"):
                    # get material name
                    materialname = mtl_data[mtl_linecounter].replace("newmtl ", "", 1).replace("\n", "")
                    # search for a map_Kd entry to get the texture
                if mtl_data[mtl_linecounter].startswith("map_Kd"):
                    # set only filename as texture entry
                    print "happens"
                    OBJ.materials[materialname] = os.path.basename(
                        mtl_data[mtl_linecounter].replace("map_Kd ", "", 1).replace("\n", ""))

                mtl_linecounter += 1

        # Build up lists of vertices vt and faces
        elif read_data[linecounter].startswith("v "):
            OBJ.vertices.append(read_data[linecounter].replace("v ", "", 1).replace("\n", ""))

        elif read_data[linecounter].startswith("vt "):
            OBJ.vertexTexcoord.append(read_data[linecounter].replace("vt ", "", 1).replace("\n", ""))

        elif read_data[linecounter].startswith("usemtl"):
            # set active material which will be used by the following faces
            activeMaterial = read_data[linecounter].replace("usemtl ", "", 1).replace("\n", "")
            # add entry to faces dictionary if not yet existing and initialize empty list
            if not activeMaterial in OBJ.faces:
                OBJ.faces[activeMaterial] = []

        elif read_data[linecounter].startswith("f "):
            OBJ.faces[activeMaterial].append(read_data[linecounter].replace("f ", "", 1).replace("\n", ""))
            OBJ.facecount += 1

        linecounter += 1

        # Create the .reo file
    with open(out_file, 'w') as f:
        f.write("# Riot Engine Object\n")
        f.write("# Created with the .obj to .reo converter by BuXXe\n\n")

        f.write("version " + OBJ.version + "\n")
        f.write("name " + OBJ.name + "\n")

        f.write("created by " + OBJ.author + " on " + OBJ.creationDate + "\n\n")

        f.write("Lighting " + str(OBJ.lighting) + "\n\n")

        # write materials
        f.write("materials " + str(len(OBJ.materials)) + "\n")

        # Create list with materials sorted by their number (Material1, Materal2, Material3)
        # instead if sorting strings (Materal1, Materal10, Materal100, Material2)
        sorted_materials = [None] * len(OBJ.materials)
        for key in OBJ.materials.keys():
            matcher = re.search("(\d+)$", str(key))
            index = matcher.group(0)
            sorted_materials[int(index)] = OBJ.materials[key]

        for i in range(len(sorted_materials)):
            f.write(str(i) + " texture " + sorted_materials[i] + "\n")

        f.write("\n")
        f.write("transform\n")
        for en in OBJ.transform:
            f.write(" ".join([str(d) for d in en]) + "\n")

        f.write("\n")
        f.write("vertices " + str(len(OBJ.vertices)) + "\n")

        for index, vert in enumerate(OBJ.vertices):
            f.write(str(index) + " " + vert + "\n")

        f.write("\n")
        f.write("faces " + str(OBJ.facecount) + "\n")
        f.write("\n")

        # create blocks and print them
        facecounter = 0

        # Create list with materials sorted by their number (Material1, Materal2, Material3)
        # instead if sorting strings (Materal1, Materal10, Materal100, Material2)
        sorted_faces = [None] * len(OBJ.faces)
        for key in OBJ.faces.keys():
            matcher = re.search("(\d+)$", str(key))
            index = matcher.group(0)
            sorted_faces[int(index)] = OBJ.faces[key]

		# TODO use zip to correspond faces and materials?
        for i in range(len(sorted_faces)):
            for face in sorted_faces[i]:
                f.write("polygon " + str(facecounter) + "\n")
                facecounter += 1
                fparts = face.split(" ")

                f.write("vt " + str(len(fparts)) + ":" + " ".join(
                    [str(int(d.split("/")[0]) - 1) for d in reversed(fparts)]) + "\n")
                f.write("ma " + str(i) + "\n")
                f.write("tu " + " ".join(
                    [OBJ.vertexTexcoord[(int(d.split("/")[1]) - 1)].split(" ")[0] for d in reversed(fparts)]) + "\n")
                f.write("tv " + " ".join(
                    [OBJ.vertexTexcoord[(int(d.split("/")[1]) - 1)].split(" ")[1] for d in reversed(fparts)]) + "\n")
                f.write("\n")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='OBJ to REO converter')
    parser.add_argument('--input', '-i', dest='inDir', required=True, nargs=1,
                        help='Input directory with OBJ files to process')
    parser.add_argument('--output', '-o', dest='outDir', required=True, nargs=1,
                        help='Output directory to save converted files (will be created)')
    parser.add_argument('--replace', '-r', dest='replace', required=False, action='store_true',
                        help='Replace files in output directory')
    parser.set_defaults(replace=False)

    parser.parse_args()
    arguments = parser.parse_args()
    input_dir = arguments.inDir[0]
    output_dir = arguments.outDir[0]
    replace = arguments.replace

    if not os.path.isdir(input_dir):
        print('ERROR: not a directory %s' % input_dir)
        exit(1)

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
        print('Output directory created: %s' % output_dir)

    filenames = []

    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.obj'):
            print('Processing %s' % filename)
            convert_obj_to_reo(os.path.join(input_dir, filename), os.path.join(output_dir, filename[:-3] + 'reo'))

    print('All files processed!\nGreat Success!')
    print('Check results in \'%s\'' % output_dir)

