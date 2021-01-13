# Welltory.test
Репозиторий с тестовым заданием по вакансии: https://welltory.typeform.com/to/FgrW2Tib

## Installation

To install all necessary requirements, do

```bash
python3 -m pip install -r requirements.txt
```

## Usage

```bash
usage: validate.py [-h] [-s SCHEMA] [-e EVENT] [--strict]

Helps to cross-validate multiple schemas versus multiple json event files

optional arguments:
  -h, --help            show this help message and exit
  -s SCHEMA, --schema SCHEMA
                        Input schemas folder or single file
  -e EVENT, --event EVENT
                        Input events folder or single file
  --strict              Will only perform validation if 'event' field in event
                        matches schema filename
```

## Test output
The result produced by the script on the test data provided by Welltory:

Command:
```bash
./validate.py --strict --quiet -s task_folder/schema -e task_folder/event
```

Output:
```bash
Schema: task_folder/schema/cmarker_created.schema
Event: task_folder/event/fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json
  Message 1: 'cmarkers' is a required property
    Location in schema file: required
    Location in event file:  <root>
Schema: task_folder/schema/cmarker_created.schema
Event: task_folder/event/29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json
  Message 1: event file is empty
Schema: task_folder/schema/cmarker_created.schema
Event: task_folder/event/a95d845c-8d9e-4e07-8948-275167643a40.json
  Message 1: event file is empty
Schema: task_folder/schema/cmarker_created.schema
Event: task_folder/event/ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json
  Message 1: None is not of type 'integer'
    Location in schema file: properties::user_id::type
    Location in event file:  user_id
  Message 2: 'suprt marker' is not of type 'array'
    Location in schema file: properties::cmarkers::type
    Location in event file:  cmarkers
Schema: task_folder/schema/cmarker_created.schema
Event: task_folder/event/3b4088ef-7521-4114-ac56-57c68632d431.json
Schema: task_folder/schema/cmarker_created.schema
Event: task_folder/event/e2d760c3-7e10-4464-ab22-7fda6b5e2562.json
  Message 1: 'bad user id' is not of type 'integer'
    Location in schema file: properties::user_id::type
    Location in event file:  user_id
Schema: task_folder/schema/workout_created.schema
Event: task_folder/event/29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json
  Message 1: event file is empty
Schema: task_folder/schema/workout_created.schema
Event: task_folder/event/a95d845c-8d9e-4e07-8948-275167643a40.json
  Message 1: event file is empty
Schema: task_folder/schema/label_selected.schema
Event: task_folder/event/29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json
  Message 1: event file is empty
Schema: task_folder/schema/label_selected.schema
Event: task_folder/event/a95d845c-8d9e-4e07-8948-275167643a40.json
  Message 1: event file is empty
Schema: task_folder/schema/label_selected.schema
Event: task_folder/event/1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json
  Message 1: 'unique_id' is a required property
    Location in schema file: required
    Location in event file:  <root>
  Message 2: 'user' is a required property
    Location in schema file: required
    Location in event file:  <root>
  Message 3: 'user_id' is a required property
    Location in schema file: required
    Location in event file:  <root>
Schema: task_folder/schema/label_selected.schema
Event: task_folder/event/cc07e442-7986-4714-8fc2-ac2256690a90.json
  Message 1: event file has no 'data' field
Schema: task_folder/schema/sleep_created.schema
Event: task_folder/event/29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json
  Message 1: event file is empty
Schema: task_folder/schema/sleep_created.schema
Event: task_folder/event/297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json
Schema: task_folder/schema/sleep_created.schema
Event: task_folder/event/f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json
Schema: task_folder/schema/sleep_created.schema
Event: task_folder/event/a95d845c-8d9e-4e07-8948-275167643a40.json
  Message 1: event file is empty
Schema: task_folder/schema/sleep_created.schema
Event: task_folder/event/bb998113-bc02-4cd1-9410-d9ae94f53eb0.json
  Message 1: 'unique_id' is a required property
    Location in schema file: required
    Location in event file:  <root>
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

