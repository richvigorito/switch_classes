from setuptools import setup

setup(
    name='switch_classes',
    version='0.0.1',
    description='Switch Classes',
    url='git@github.com:richvigorito/switch-classes.git',
    author='Rich Vigorito',
    author_email='nicetry.bozo@gmail.com',
    license='unlicense',
    package_dir={'':'src'},
    packages=find_packages(where='src')
    zip_safe=False
)

install_requires=['json']
