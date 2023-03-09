FROM python:3.6

# 设置北京时间
RUN rm -f /etc/localtime && \
    ln -sv /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone


# 更新apt源
RUN sed -i s/deb.debian.org/mirrors.163.com/g /etc/apt/sources.list && \
    cat /etc/apt/sources.list && \
    apt-get clean && \
    apt-get update
#    apt-get install -y python36-devel
#    apt-get install -y uwsgi-plugin-python

RUN mkdir /app
WORKDIR /app

COPY . .

# 更新镜像源并启动
RUN /usr/local/bin/python3 -m pip install --upgrade pip -i https://pypi.douban.com/simple && \
    pip3 install  -r /app/wl-backend/reqiurements.txt -i https://pypi.douban.com/simple

CMD ["/usr/local/bin/python3","/app/main.py"]