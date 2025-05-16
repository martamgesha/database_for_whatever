// mongo-init.js

db = db.getSiblingDB('SkinSight');

db.createCollection('users');

db.users.createIndex({ "username": 1 }, { unique: true });
db.users.createIndex({ "email": 1 }, { unique: true });
db.users.createIndex({ "user_id": 10000001 }, { unique: true });

db.users.insertOne({
  user_id: "10000001",
  username: "admin",
  password: "admin123",
  email: "admin@example.com",
  role: "admin"
});

db.createCollection('processes');

db.processes.createIndex({ "user_id": 10000001 });
