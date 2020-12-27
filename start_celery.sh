#!/bin/bash

celery worker -A Calendar --concurrency=4 --loglevel=info
