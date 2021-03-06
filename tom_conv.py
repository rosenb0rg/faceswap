import os
import argparse
from char_dir import *
import shutil

parser = argparse.ArgumentParser(description='converter!!!')
parser.add_argument("-s", "--Sce", type=str, required=False, default='in',
	help="scene name")
parser.add_argument("-c", "--Char", type=str, required=False, default='out',
	help="character name")
parser.add_argument("-S", "--Src", type=str, required=False, default='in',
	help="source number")
parser.add_argument("-t", "--Targ", type=str, required=False, default='out',
	help="target number")
args = parser.parse_args()

scene_name = args.Sce
character_name = args.Char
source_number = args.Src
target_number = args.Targ

character_info = Character(character_name, scene_name, source_number, target_number)

in_dir = character_info.align_crop_dir
out_dir = character_info.align_conv_dir
model_dir = character_info.model_dir

if not os.path.exists(in_dir):
	os.makedirs(in_dir)

if os.path.exists(out_dir):
	shutil.rmtree(out_dir, ignore_errors=True)
	os.makedirs(out_dir)

if not os.path.exists(out_dir):
	os.makedirs(out_dir)

print (in_dir, out_dir, model_dir)

os.system("python C:/local/src/faceswap/faceswap.py convert -i %s -o %s --model-dir %s -t GAN128 -b 0" % (in_dir, out_dir, model_dir))