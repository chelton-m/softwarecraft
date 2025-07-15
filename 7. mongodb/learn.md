1. Project Setup
A. Backend (Node + Express + MongoDB)
npm init -y
npm install express mongoose cors dotenv body-parser
npm install --save-dev nodemon
Create server.js (see below)
Create .env or config.env:
MONGODB_URI=mongodb://localhost:27017/mern-tutorial
PORT=5000

B. Frontend (React)
npx create-react-app client
cd client && npm install axios
Replace client/src/App.js with the code below.

2. Backend: Basic Hello World + MongoDB
server.js

3. Frontend: Basic CRUD
client/src/App.js

4. Run Everything
Start MongoDB: brew services start mongodb/brew/mongodb-community
Start backend: npm run dev
Start frontend: cd client && npm start