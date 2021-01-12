#!/usr/bin/env python3

import argparse
import json
import jsonschema
import sys
import pathlib


def print_validation_message(schema, event, validator=jsonschema.Draft7Validator):
    validator = validator(schema=schema)

    # dummy checks
    if not event:
        print(f"  Message 1: event file is empty")
    elif event.get("data", None) is None:
        print(f"  Message 1: event file has no 'data' field")
    else:
        event = event["data"]
        for idx, error in enumerate(validator.descend(event, schema)):
            error_message = error.message
            schema_location = "::".join(error.absolute_schema_path)
            event_location = "::".join(error.absolute_path)

            if event_location == "":
                event_location = "<root>"
            if schema_location == "":
                schema_location = "<root>"

            if error_message == "None is not of type 'object'":
                error_message += ": the event file is probably empty"

            print(f"  Message {idx+1}: {error_message}")
            print(f"    Location in schema file: {schema_location}")
            print(f"    Location in event file:  {event_location}")


def main(args):
    parser = argparse.ArgumentParser(
        description="Helps to cross-validate multiple schemas versus multiple json event files"
    )

    parser.add_argument(
        "-s", "--schema", type=str, help="Input schemas folder or single file"
    )
    parser.add_argument(
        "-e", "--event", type=str, help="Input events folder or single file"
    )
    #  parser.add_argument(
    #  "-q",
    #  action="store_true",
    #  default=False,
    #  help="Enables silent mode that won't write warni
    #  )

    args = parser.parse_args()

    with open(args.event, "r") as fin:
        event = json.load(fin)

    with open(args.schema, "r") as fin:
        schema = json.load(fin)

    print(f"Schema: {args.schema}, event: {args.event}")
    print_validation_message(schema=schema, event=event)


if __name__ == "__main__":
    main(sys.argv[1:])
