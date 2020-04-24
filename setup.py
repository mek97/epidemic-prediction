from io import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='epipred',  # Required
    version='0.1.0',  # Required
    description='Project to predict epidemic trends and effects',  # Optional

    long_description=long_description,  # Optional

    long_description_content_type='text/markdown',  # Optional (see note above)

    url='https://github.com/mek97/epidemic-prediction',  # Optional

    author='The Python Packaging Authority',  # Optional

    author_email='pypa-dev@googlegroups.com',  # Optional

    classifiers=[  # Optional
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='epidemic prediction time series datascience',  # Optional

    package_dir={'': 'src'},  # Optional

    packages=find_packages(where='src'),  # Required

    python_requires='>=3.5',

    install_requires=['pandas', 'scipy', 'numpy'],  # Optional

    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    package_data={  # Optional
        'epidpred': ['package_data.dat'],
    },

    data_files=[],  # Optional

    entry_points={
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/mek97/epidemic-prediction/issues',
        'Source': 'https://github.com/mek97/epidemic-prediction',
    },
)
