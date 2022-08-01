import os
from pathlib import Path, PurePath
from setuptools import setup, find_packages

SUFFIX = '.jinja2'
ROOT_PATH = os.path.split(os.path.abspath(os.path.join(__file__)))[0]
src_path = os.path.join(ROOT_PATH, 'flask_rest_engine')


def gen_data(data_root='static'):
    """just for collect static files.
    """
    return [fpath.as_posix() for fpath in Path(
        PurePath(src_path) / data_root).glob(f'**/*{SUFFIX}')]


package_data = gen_data()
# The amount files of `rivendell[new]`
assert len(package_data) == 30, \
    'nums of tepl files error, {}'.format(len(package_data))
package_data.append('py.typed')

long_description_content_type = 'text/markdown'
try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
    long_description_content_type = 'text/x-rst'
except(OSError, ImportError):
    long_description = open('README.md').read()

setup(
    name='flask-rest-engine',
    version='1.0.0',
    python_requires='>=3.6, <4',
    description='Flask-rest-engine - A flask restful API project generator.',
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    author='Hyria PENG',
    author_email='penghanyuan@gmail.com',
    url='https://github.com/penghanyuan/flask-rest-engine',
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
    ],
    zip_safe=False,
    packages=find_packages(exclude=['tests*']),
    package_data={'flask_rest_engine': package_data},
    install_requires=[
        'Click>=8.1.0',
        'Jinja2>=3.1.2',
        'inflect>=5.6.2',
    ],
    entry_points={
        'console_scripts': ['flask_rest_engine = flask_rest_engine:main']
    },
)
