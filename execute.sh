#!/bin/bash

echo "==> Running test suite:"
python ./auction/index.py ./auction/test_config.json ./auction/test_input.json
python  ./auction/unit_test.py
