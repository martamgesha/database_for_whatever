FROM mongo:latest

COPY mongo-init.js /docker-entrypoint-initdb.d/

ENV MONGO_INITDB_ROOT_USERNAME=root

ENV MONGO_INITDB_ROOT_PASSWORD=root123

EXPOSE 27017

CMD ["mongod"]
