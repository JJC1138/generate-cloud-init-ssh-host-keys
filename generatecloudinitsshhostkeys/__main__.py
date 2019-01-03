import shutil
import sys
import tempfile

def run(temp_folder_name):
    config = "test content\n"
    
    sys.stdout.write(config)

def main():
    temp_folder_name = tempfile.mkdtemp(prefix='generate-cloud-init-ssh-host-keys')
    try:
        run(temp_folder_name)
    finally:
        shutil.rmtree(temp_folder_name, ignore_errors=True)
