import os
import tifftools
import re


# tifftools library used

filepath = input(" Enter the TIF Image file path: ")

output_dir = "Output"

output = filepath + "/" + output_dir

if os.path.exists(output):
	pass
else:
	os.mkdir(output)


for fname in os.listdir(filepath):
	if not fname.endswith(".tif"):
		continue
	outputname = fname
	patn = re.sub(r"\.tif", "", outputname)
	outputdir = output + "/" + patn
	tif_file = filepath + "/" + fname
	tif_split = output + "/" + fname
	tifftools.tiff_split(tif_file, outputdir + "_")

