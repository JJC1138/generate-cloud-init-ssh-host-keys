import setuptools

setuptools.setup(
    name = 'generate-cloud-init-ssh-host-keys',
    version = '1.0.0dev',
    packages = setuptools.find_packages(),
    entry_points = {'console_scripts': [
        'generate-cloud-init-ssh-host-keys = generatecloudinitsshhostkeys.__main__:main',
    ]},
    install_requires = ['pyyaml'],
)
