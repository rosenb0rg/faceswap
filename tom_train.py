import os
import argparse
from char_dir import *

parser = argparse.ArgumentParser(description='converter!!!')
# parser.add_argument("-s", "--Sce", type=str, required=False, default='in',
# 	help="scene name")
parser.add_argument("-c", "--Char", type=str, required=False, default='out',
	help="character name")
# parser.add_argument("-S", "--Src", type=str, required=False, default='in',
# 	help="source number")
# parser.add_argument("-t", "--Targ", type=str, required=False, default='out',
# 	help="target number")
args = parser.parse_args()

# scene_name = args.Sce
character_name = args.Char
# source_number = args.Src
# target_number = args.Targ

character_info = Character(character_name, scene='nada', source=000, target=00)

imgA_dir = character_info.imgA_dir
imgB_dir = character_info.imgB_dir
model_dir = character_info.model_dir	

print ('imgA dir\n', imgA_dir,'imgB dir\n', imgB_dir, model_dir)

os.system("python C:/local/src/faceswap/faceswap.py train -A %s -B %s --model-dir %s -t GAN128 -bs 8 -p -pl -ag -v" % (imgA_dir, imgB_dir, model_dir))