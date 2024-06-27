#!/bin/sh -e

VENV="venv"

. "./$VENV/bin/activate"

flask --debug run
