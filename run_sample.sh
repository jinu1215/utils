#!/bin/bash

DIR_HOME=$(pwd)

#print_usage () {
#	echo
#	echo "Usage:"
#	echo "    $0    start|stop|restart|status"
#	echo
#}
#
#case "$1" in
#	start|stop|restart|status)
#		OP=$1
#		echo "Choosed operation:" $OP
#		;;
#	*)
#		print_usage
#		exit 2
#	;;
#esac

echo "*************************************************"
echo "* Run sample code"
echo "* Sample code using each library"
echo "  - src.daemon"
echo "  - src.process_pool"
echo "  - src.base_handler"
echo "*************************************************"
sleep 2

PYTHONPATH=$DIR_HOME
echo "1. Start daemon"
echo "- create 3 forked process using process_pool"
echo "- create 2 types process (SampleHandler1, SampleHandler2)"
echo "- SampleHandler1 created one"
echo "- SampleHandler2 created two"
python $DIR_HOME/sample/sample.py start
sleep 1
echo
echo "2. Check daemon status"
echo "- print parent pid"
python $DIR_HOME/sample/sample.py status
sleep 1
echo
echo "3. Restart daemon"
echo "- each process pid will be changed"
python $DIR_HOME/sample/sample.py restart
sleep 1
echo
echo "4. Stop daemon"
python $DIR_HOME/sample/sample.py stop
echo
echo "5. Check daemon status"
python $DIR_HOME/sample/sample.py status
