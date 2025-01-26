from setuptools import setup, find_packages

setup(
    name='Simple_Testcase_Maker',
    version='0.0.1',
    description='tcmaker package creation written by csvega',
    author='csvega',
    author_email='vega4792@gmail.com',
    url='https://github.com/csvega/tcmaker',
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
