from setuptools import setup, find_packages

setup(
    name='pv',
    version='0.1.3',
    description='minimal wsgi framework',
    url='http://github.com/tetsuo/pv',
    author='Onur Gunduz',
    author_email='ogunduz@gmail.com',
    packages=find_packages(),
    install_requires=['simplejson', 'webob==1.4.1'],
    license='mit',
)