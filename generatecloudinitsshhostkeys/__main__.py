import os.path
import shutil
import subprocess
import sys
import tempfile

import ruamel.yaml
from ruamel.yaml.scalarstring import PreservedScalarString

def run(temp_folder_name):
    def generate_keys(key_type):
        private_key_filename = os.path.join(temp_folder_name, key_type)
        subprocess.check_call(['ssh-keygen', '-q', '-N', '', '-t', key_type, '-f', private_key_filename], stdout=sys.stderr, stderr=sys.stderr)
        public_key_filename = '%s.pub' % private_key_filename
        
        with open(private_key_filename, 'rt') as private_key_file:
            private_key = private_key_file.read()
        with open(public_key_filename, 'rt') as public_key_file:
            public_key = public_key_file.read()
        
        return (private_key, public_key)
    
    keys = {}
    
    for key_type in ['ecdsa', 'ed25519', 'rsa']:
        (private_key, public_key) = generate_keys(key_type)
        keys['%s_private' % key_type] = PreservedScalarString(private_key)
        keys['%s_public' % key_type] = PreservedScalarString(public_key)
    
    ruamel.yaml.YAML().dump({'ssh_keys': keys}, sys.stdout)

def main():
    temp_folder_name = tempfile.mkdtemp(prefix='generate-cloud-init-ssh-host-keys')
    try:
        run(temp_folder_name)
    finally:
        shutil.rmtree(temp_folder_name, ignore_errors=True)
