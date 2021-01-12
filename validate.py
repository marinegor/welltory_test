#!/usr/bin/env python3

import argparse
import json
import pathlib
import sys
import traceback

import jsonschema


def print_validation_message(
    schema, event, validator=jsonschema.Draft7Validator
):
    validator = validator(schema=schema)

    # dummy checks
    if not event:
        print(f"  Message 1: event file is empty")
    elif event.get("data", None) is None:
        print(f"  Message 1: event file has no 'data' field")

    else:
        # main logic
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
        "-s",
        "--schema",
        type=pathlib.Path,
        help="Input schemas folder or single file",
    )
    parser.add_argument(
        "-e",
        "--event",
        type=pathlib.Path,
        help="Input events folder or single file",
    )

    parser.add_argument(
        "--strict",
        action="store_true",
        default=False,
        help="Will only perform validation if 'event' field in event matches schema filename",
    )  # added to simplify the output and remove obviously unmatched schema and event files

    args = parser.parse_args()

    # unify folders and single files
    if args.event.is_file():
        args.event = [args.event]
    elif args.event.is_dir():
        args.event = pathlib.Path(args.event).glob("*")
        args.event = [file for file in args.event if file.is_file()]

    if args.schema.is_file():
        args.schema = [args.schema]
    elif args.schema.is_dir():
        args.schema = pathlib.Path(args.schema).glob("*")
        args.schema = [file for file in args.schema if file.is_file()]

    # main processing loop
    for schema_filename in args.schema:
        for event_filename in args.event:
            try:
                with open(schema_filename, "r") as fin:
                    schema = json.load(fin)
                with open(event_filename, "r") as fin:
                    event = json.load(fin)

                if args.strict:
                    schema_kind = schema_filename.stem
                    if event and event.get("event", None) != schema_kind:
                        continue

                print(f"Schema: {schema_filename}")
                print(f"Event: {event_filename}")
                print_validation_message(schema=schema, event=event)

            except Exception as e:
                print(
                    f"Error {e} occured during validation of {event_filename} with {schema_filename}",
                    file=sys.stderr,
                )
                traceback.print_exc(file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1:])
