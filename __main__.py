from jsonc_parser.parser import JsoncParser
import rawdcparser
import argparse
import os

# Create Parser Object
parser = argparse.ArgumentParser(description='RawDC format parser')

# Add arguments
parser.add_argument('-i', '--input', type=str, help='.jsonc file path')
parser.add_argument('-o', '--output', type=str, help='output .txt file path')

# Parse arguments
args = parser.parse_args()

# Check, is input file exists, and is readable
if not os.path.isfile(args.input) or not os.access(args.input, os.R_OK):
    print(f"File {args.input} Does not exists, or it`s not readable")
    exit(1)
readfile = open(args.input, mode="r", encoding="UTF-8")
data = '\n'.join(readfile.readlines())
# Parse RawDC file
parsed_data = rawdcparser.parse(JsoncParser.parse_str(data)["rawtext"])

# Zapisz wynik do pliku
try:
    with open(args.output, mode='w', encoding="UTF-8") as f:
        f.write(parsed_data)
except IOError:
    print(f"Can`t write to file {args.output}.")
    exit(1)
