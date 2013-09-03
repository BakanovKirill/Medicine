import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#Dependencies - python eggs
install_requires = [
    'setuptools>=0.6',
    'Django == 1.5', # main framework
    'south', #creates migrations
    ]

#List of paths, where parser may find packages
dependency_links = [
    'http://dist.plone.org/thirdparty/',
    'http://pypi.pinaxproject.com/',
    ]

#Execute function to handle setuptools functionality
setup(name="medicine",
      version="0.1",
      description="Medicine test project",
      long_description = read('README.rst'),
      author="Kirill Bakanov",
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      dependency_links=dependency_links,
      entry_points="""
              # -*- Entry points: -*-
              """,
      classifiers = [
          'Development Status :: 4 - Beta',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: Medicine/HTTP',
          ]
      )