from setuptools import setup, find_packages

setup(
    name='Simple Testcase Maker',
    version='0.0.1',
    description='PYPI tutorial package creation written by csvega',
    author='csvega',
    author_email='vega4792@gmail.com',
    url='https://github.com/teddylee777/teddynote',
    install_requires=['random', 'os', 're',],
    packages=find_packages(exclude=[]),
    keywords=['testcase', 'online judge', 'OJ', 'hustoj'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)
