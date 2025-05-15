FROM mongo:latest

COPY mongo-init.js /docker-entrypoint-initdb.d/

ENV MONGO_INITDB_ROOT_USERNAME=admin

ENV MONGO_INITDB_ROOT_PASSWORD=securepassword

EXPOSE 27017

CMD ["mongod"]
