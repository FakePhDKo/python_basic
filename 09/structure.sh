#!/bin/bash

DIR=test
mkdir -p $DIR && rm -rf $DIR/*
BASEDIR=$DIR/game
mkdir -p $BASEDIR/{sound,graphic}
touch $BASEDIR/__init__.py
touch $BASEDIR/{sound,graphic}/__init__.py
