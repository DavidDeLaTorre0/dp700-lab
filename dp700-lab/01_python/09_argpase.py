import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--clean-output", default="clean.json")
args=parser.parse_args()
print(args.input)
