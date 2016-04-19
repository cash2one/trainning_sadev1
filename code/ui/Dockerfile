FROM daocloud.io/nginx

COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/default.conf /etc/nginx/conf.d/default.conf
COPY code/ /usr/share/nginx/ui/

EXPOSE 7777

CMD ["service", "nginx", "start"]


