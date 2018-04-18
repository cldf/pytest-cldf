import logging

import pytest


def pytest_addoption(parser):
    parser.addoption('--cldf-metadata', default='cldf/cldf-metadata.json', help='')


@pytest.fixture(scope='session')
def cldf_dataset(pytestconfig):
    from pycldf import Dataset

    return Dataset.from_metadata(pytestconfig.getoption('cldf_metadata'))


@pytest.fixture
def cldf_logger():
    logger = logging.getLogger('pycldf')
    logger.propagate = False
    logger.addHandler(logging.StreamHandler())
    return logger

