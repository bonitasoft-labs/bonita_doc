FROM node:13-alpine

EXPOSE 4000
VOLUME ["/doc"]
RUN apk update && \
    apk add git make gcc g++ ruby==2.6.6-r2 ruby-dev==2.6.6-r2 ruby-rdoc ruby-rake ruby-irb ruby-bigdecimal py-pip curl && \
    pip install python-slugify elasticsearch && \
    gem install jekyll bundler && \
    npm install -g webpack

COPY ./entry.sh /

RUN ["chmod", "777", "/entry.sh"]

WORKDIR /doc

ENTRYPOINT ["sh", "/entry.sh"]