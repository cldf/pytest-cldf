from setuptools import setup


setup(
    name='pytest-cldf',
    version='0.1.1',
    description="Easy quality control for CLDF datasets using pytest",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
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
