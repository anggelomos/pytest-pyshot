# pyshot
Pytest plugin to facilitate screenshot taking with selenium webdriver.

## Installation
```bash
pip install pyshot
```

## Usage

First you need to add the configuration file `pyshot.conf` file.
```
[pyshot]
screenshots_path = C:/Users/angel/OneDrive/Documentos/projects/pyshot/screenshots
only_pyshot_steps = false
create_folder_per_testcase = true
```

`screenshots_path`: Absolute path of the folder where the screenshots will be saved. It shouldn't have a `/` at the end.

`only_pyshot_steps`: When it is activated (true) only the functions marked with the decorator `@pyshot_step` will be screenshoted.

`create_folder_per_testcase`: When it is activated (true) a new folder will be created automatically to save the screenshots of the testcase.

Once you have created the pyshot.conf file add a fixture with the decorator `@pyshot_driver` that returns the driver you will to use during test execution, like this:

```python
@pytest.fixture(scope="module", autouse=True)
@pyshot_driver
def chrome_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver
```

If you want to take screenshots only on certain steps of the execution, activate the option `only_pyshot_steps` on the pyshot.conf and add the decorator `@pyshot_step` on the functions where you want to take screenshots.

```python
@pyshot_step
def search(cls, search_text: str):
    SearchPage.enter_search_text(search_text)
    SearchPage.make_search()
```

Once you have configured everything within your repo add the argument `--pyshot_conf` with the path to your pyshot.conf file.

```bash
pytest test_example.py --pyshot_conf=usr/test/pyshot.conf
```

## Demo
You can check the pyshot example repo to see a small demo project.

https://youtu.be/C1rKgZn5tJg
https://github.com/anggelomos/pyshot-example
