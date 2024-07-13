#/usr/bin/env bash

if [ "$1" = "-p" ]; then
    python ~/desktop/cs/cpu/to_floating_point.py
fi

if [ "$1" = "-d" ]; then
    docker run -it --rm -d -p 8080:80 --name web -v /home/shingo/desktop/cs/content:/usr/share/nginx/html nginx
    
    if [ "$2" = "--stop" ]; then
        docker stop web
    fi
fi
