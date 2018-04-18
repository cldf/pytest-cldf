from setuptools import setup


setup(
    name='pytest-cldf',
    version='0.1.0',
    packages=['pytest_cldf'],
    install_requires=[
        'pytest>=3.1', 
        'pycldf>=1.2',
    ],
    entry_points={
        'pytest11': [
            'pytest_clld = pytest_cldf.plugin',
        ]
    },
    classifiers=[
        'Framework :: Pytest',
    ],
)
