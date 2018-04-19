# pytest-cldf

[![PyPI](https://img.shields.io/pypi/v/pytest-cldf.svg)](https://pypi.org/project/pytest-cldf)


This pytest plugin can be used to run validation of CLDF datsets via the pytest
test runner. In particular, this allows hooking up continuous validation with
CI services like travis-ci easily.


## Continuous validation via Travis-CI

To make sure a dataset - curated in a git repository on GitHub - is continuously,
i.e. after each commit, validated, you have to
- hook up the repository with Travis-CI
- add a Travis configuration file `.travis.yml` with the following content:
```yaml
language: python
python: "3.6"
cache: pip
before_cache: rm -f $HOME/.cache/pip/log/debug.log
install: pip install pytest-cldf
script: pytest --cldf-metadata=cldf/cldf-metadata.json test.py
```

- add the python file implementing the tests `test.py`:
```python
def test_valid(cldf_dataset, cldf_logger):
    assert cldf_dataset.validate(log=cldf_logger)
```


## Extended validation

TODO

