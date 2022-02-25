import ultimateAlprSdk as alpr		# Ultimate ALPR python SDK
import argparse 					# Argument parser
import os							# OS interaction, files etc.
import json							# JSON
import time							# Timing
from PIL import Image 				# Pillow used to open Image

begin = time.process_time()

# Argument parsing
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input",	dest="input",	type=str,	required=True,	help="Input directory path (required).")
ap.add_argument("-o", "--output",	dest="outDir",	type=str,	required=False,	default="results.csv", 	help="Output filename(path).")
args = ap.parse_args()

# Check and walk directory.
if os.path.isdir(args.input):
	print("Given input is a directory.")
else:
	ap.error("Provide path to a directory containing jpg images using -i flag!")

# JSON Configuration
CONFIG = {
	"debug_level": "fatal",
	"debug_write_input_image_enabled": False,
	"debug_internal_data_path": "debug/",

	"assets_folder": "../../../assets",
}

# Set img format (TODO: implement checking, if needed)
format = alpr.ULTALPR_SDK_IMAGE_TYPE_RGB24

# Open/create file for result outputs.
outFile = os.open(args.outDir, os.O_CREAT|os.O_RDWR)

# Engine init
#checkResult("Init", alpr.UltAlprSdkEngine_init(json.dumps(CONFIG)))
alpr.UltAlprSdkEngine_init(json.dumps(CONFIG))
it = time.process_time() - begin
print("Init time taken:", it)
itStr = str(it) + "\n"
os.write(outFile, (str.encode(itStr)))

# Read directory and establish loop
path = os.walk(args.input)	# Walk directory.
for r, dir, files in path:
	for file in files:
		# Load image and gather relevant info
		img = Image.open(os.path.join(args.input, file))	# Load image
		width, height = img.size							# Get image size.
		start = time.process_time()							# Start timing for LPR

		# Perform LPR
		out = alpr.UltAlprSdkEngine_process(format, img.tobytes(), width, height, 0)
		tt = time.process_time() - start					# Calcualte and log time for LPR

		# Parse JSON output and output
		output = out.json()
		outson = json.loads(output)
		print("\n" + file)
		print(outson['plates'][0]['text'])
		print("Detection time taken:", tt)

		# Create output as string and write to file.
		outStr = file + "," + outson['plates'][0]['text'] + "," + str(tt) + "\n"
		os.write(outFile, str.encode(outStr))

print("") # Output-spacer
# Pause
# input("\nPress enter to deinit engine and exit program.")

# Engine deinit and close file
alpr.UltAlprSdkEngine_deInit()
os.close(outFile) # Close output file.

# EOF
print("Seems like it worked!")
