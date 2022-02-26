#!/bin/sh -l

echo "Action Started - $1"
time=$(date)
echo "::set-output name=time::$time"
