#!/usr/bin/env bash


function showVersion
{
    echo "version 1.0"
    exit 0
}

function showHelp
{
    echo "Usage: ./agent.sh [Options]"
    echo "Options:"
    echo -e "\t-v, --version\t\t show program version number and exit"
    echo -e "\t-h, --help\t\t show this help message and exit"
    echo -e "\t-t, --ttl\t\t set agent period, default is 60s"
    echo -e "\t-m MODULE, --module=MODULE\t\t use module MODULE\n"
    echo "Modules:"
    echo -e "\tall, cpu, memory"
    exit 0
}

function get_load
{
    if [ -f /proc/loadavg ]; then
        read w1_avg w5_avg w15_avg a a < /proc/loadavg
    fi
    echo "w1_avg: $w1_avg"
    echo "w5_avg: $w5_avg"
    echo "w15_avg: $w15_avg"

}
function show_load
{
    while [ $# -gt 0 ] && [ $1 -gt 0 ]; do
        get_load
        sleep $1
    done
    if [ $# -eq 0 ]; then
        get_load
    fi
}
function get_cpu
{
    line=($(grep 'cpu ' /proc/stat))
    user=${line[1]}
    nice=${line[2]}
    system=${line[3]}
    idle=${line[4]}
    iowait=${line[5]}
    irq=${line[6]}
    softirq=${line[7]}
    steal=${line[8]}
    guest=${line[9]}
    guest_nice=${line[10]}
    total=$(($user+$nice+$system+$idle+$iowait+$irq+$softirq+$steal+$guest+$guest_nice))
    user_per=$(($user*100/$total))
    nice_per=$(($nice*100/$total))
    system_per=$(($system*100/$total))
    idle_per=$(($idle*100/$total))
    iowait_per=$(($iowait*100/$total))
    irq_per=$(($irq*100/$total))
    softirq_per=$(($softirq*100/$total))
    steal_per=$(($steal*100/$total))
    guest_per=$(($guest*100/$total))
    guest_nice_per=$(($guest_nice*100/$total))
    echo $user_per, $nice_per, $system_per, $idle_per, $iowait_per, $irq_per, \
        $softirq_per, $steal_per, $guest_per, $guest_nice_per
}

function show_cpu
{
    while [ $# -gt 0 ] && [ $1 -gt 0 ]; do
        get_cpu
        sleep $1
    done
    if [ $# -eq 0 ]; then
        get_cpu
    fi
}

function get_memory
{
    echo "get memory"
}

function show_memory
{
    while [ $# -gt 0 ] && [ $1 -gt 0 ]; do
        get_memory
        sleep $1
    done
    if [ $# -eq 0 ]; then
        get_memory
    fi
}

function show_all
{
    while [ $1 -gt 0 ]; do
        show_load
        show_cpu
        show_memory

        sleep $1
    done

}


# parse the args
if [ $# -eq 1 ];
then
    case $1 in
    "-v"|"--version")
        showVersion ;;
    "-h"|"--help")
        showHelp ;;
    *)
        showHelp ;;
    esac
elif [ $# -eq 2 ];
then
    if [ $1 = "-m" ] || [ $1 = "--module" ]; then
        times=1
        case $2 in
        "all")
            show_all $times
            ;;
        "cpu")
            show_cpu $times
            ;;
        "memory")
            show_memory $times
            ;;
        *)
            showHelp
            ;;
        esac
    else
        showHelp
    fi

elif [ $# -eq 4 ];
then
    case $1 in
    "-t"|"--ttl")
        if [ $2 -gt 0 ];
        then
            times=$2
            case $4 in
            "all")
                show_all $times
                ;;
            "cpu")
                show_cpu $times
                ;;
            "memory")
                show_memory $times
                ;;
            *)
                showHelp
                ;;
            esac
        else
            showHelp
        fi
    ;;
    "-m"|"--module")
        times=$4
        case $2 in
        "all")
            show_all $times
            ;;
        "cpu")
            show_cpu $times
            ;;
        "memory")
            show_memory $times
            ;;
        *)
            showHelp
            ;;
        esac
    ;;
    *)
        showHelp ;;
    esac
else
    showHelp
fi

