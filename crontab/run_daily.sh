#!/bin/bash
cd /app
echo "run_daily.sh run at $(date)"
python /app/src/daily.py
echo "run_daily.sh finish at $(date)"
