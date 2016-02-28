#!/usr/bin/env bash
PID='/tmp/supervisord.pid'
# 在docker容器中的目录
CONF_FILE='/code/agent/deploy/supervisor.conf'
# 自己机器上的目录
# CONF_FILE='/home/taohao/codes/NetEase/trainning_sadev1/trainning_sadev1/code/agent/deploy/supervisor.conf'
function start
{
    echo "starting..."
    if [ ! -f $PID ]; then
        supervisord -c $CONF_FILE
        echo "started"
    else
        echo "the process is exist now"
    fi
}

function stop
{
    echo "stopping..."
    if [ -f $PID ]; then
        kill `cat $PID`
        rm -f `cat $PID`
        echo "stopped"
    else
        echo "the process is not exist"
    fi
}

function restart
{
    echo "restarting..."
    if [ -f $PID ]; then
        stop
        start
    else
        echo "process is not exist"
    fi
}

case "$1" in
    "start")
        start
        ;;
    "stop")
        stop
        ;;
    "restart")
        restart
        ;;
    *)
        echo "Usage $0 {start|stop|restart}"
        ;;
esac