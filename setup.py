from setuptools import setup, find_packages

setup(
    name='switches',
    version='0.0.1',
    description='Switch Classes',
    url='git@github.com:richvigorito/switch_classes.git',
    author='Rich Vigorito',
    author_email='nicetry.bozo@gmail.com',
    license='unlicense',
    #package_dir={'switch_classes': 'src'},
    package_dir={'': 'src'},
    #packages=find_packages(),
    packages=['src','src.house','src.devices'],
    include_package_data=True,
    #packages=['src'],
    #packages=[house,devices,loadhouse]
    #python_requires='>=3.1.*, <4',
    #install_requires=['json'],
    zip_safe=False

)

