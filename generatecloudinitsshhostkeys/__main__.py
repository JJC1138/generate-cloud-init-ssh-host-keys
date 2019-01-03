import argparse
import sys

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('config_file_name', metavar='config-file-name')
    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = arg_parser.parse_args()
    
    config = "test content\n"
    
    with open(args.config_file_name, 'at') as config_file:
        config_file.write(config)
