import argparse
import shutil
import sys
import tempfile

def run(temp_folder_name):
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('config_file_name', metavar='config-file-name')
    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = arg_parser.parse_args()
    
    config = "test content\n"
    
    with open(args.config_file_name, 'at') as config_file:
        config_file.write(config)

def main():
    temp_folder_name = tempfile.mkdtemp(prefix='generate-cloud-init-ssh-host-keys')
    try:
        run(temp_folder_name)
    finally:
        shutil.rmtree(temp_folder_name, ignore_errors=True)
