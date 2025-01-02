#!/bin/sh
python3 create_tested_data.py
python3 preprocess_tested_data.py
python3 prepare_model.py
python3 test_model.py


