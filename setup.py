from setuptools import setup


setup(
    name='pytest-cldf',
    version='0.2.0',
    description="Easy quality control for CLDF datasets using pytest",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=['pytest_cldf'],
    install_requires=[
        'attrs>=18.2',  # upgrade to the new baseline within our packages.
        'pytest>=3.1',
        'pycldf>=1.2',
    ],
    entry_points={
        'pytest11': [
            'pytest_cldf = pytest_cldf.plugin',
        ]
    },
    classifiers=[
        'Framework :: Pytest',
    ],
)
