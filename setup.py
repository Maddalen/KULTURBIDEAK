from setuptools import setup, find_packages

setup(
    name = "BASQUE_RESEARCH",
    version = "1.0",
    url = '',
    license = 'BSD',
    description = "Basque Research webgunea",
    author = 'Elhuyar Hizkuntza eta Teknologia',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
