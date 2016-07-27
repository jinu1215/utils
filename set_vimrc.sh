#!/bin/bash

DIR_HOME=$(pwd)

rm -fR $USER_HOME/.vimrc
rm -fR $USER_HOME/.vimrc_python
cp $DIR_HOME/vimrc_python $HOME/.vimrc_python
cp $DIR_HOME/vimrc $HOME/.vimrc
touch $HOME/.vimrc
