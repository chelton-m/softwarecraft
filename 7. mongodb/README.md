# MERN + MongoDB Tutorial

A complete MERN stack application to learn MongoDB fundamentals.

## 🚀 Quick Start

### Prerequisites
- Node.js (v14+)
- MongoDB installed locally or MongoDB Atlas account
- npm or yarn

### Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Set up MongoDB:**
   - **Local MongoDB:** Start MongoDB service
   - **MongoDB Atlas:** Update `config.env` with your connection string

3. **Start the server:**
   ```bash
   npm run dev
   ```

4. **Create React client:**
   ```bash
   npx create-react-app client
   cd client && npm install axios
   ```

5. **Start the client:**
   ```bash
   npm run client
   ```

## 📚 MongoDB Concepts Covered

### 1. **Connection**
```javascript
mongoose.connect('mongodb://localhost:27017/mern-tutorial')
```

### 2. **Schema Definition**
```javascript
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  createdAt: { type: Date, default: Date.now }
});
```

### 3. **CRUD Operations**
- **Create:** `User.create()` or `new User().save()`
- **Read:** `User.find()`, `User.findById()`
- **Update:** `User.findByIdAndUpdate()`
- **Delete:** `User.findByIdAndDelete()`

## 🔧 API Endpoints

- `GET /` - Hello World
- `GET /api/users` - Get all users
- `POST /api/users` - Create user
- `GET /api/users/:id` - Get user by ID
- `PUT /api/users/:id` - Update user
- `DELETE /api/users/:id` - Delete user

## 🎯 Learning Path

1. **Basic Setup** - Project structure and dependencies
2. **MongoDB Connection** - Connecting to database
3. **Schema Design** - Defining data structure
4. **CRUD Operations** - Create, Read, Update, Delete
5. **Error Handling** - Managing database errors
6. **Frontend Integration** - React with MongoDB data

## 📖 MongoDB Fundamentals

### Collections vs Documents
- **Collection:** Like a table in SQL (e.g., 'users')
- **Document:** Like a row in SQL (e.g., individual user data)

### Schema Types
- `String` - Text data
- `Number` - Numeric data
- `Date` - Date/time data
- `Boolean` - True/false
- `Array` - List of values
- `ObjectId` - Unique identifier

### Query Methods
- `find()` - Get multiple documents
- `findOne()` - Get single document
- `findById()` - Get by ID
- `countDocuments()` - Count documents

## 🛠️ Next Steps

1. Add authentication
2. Implement data validation
3. Add search functionality
4. Create complex queries
5. Add indexes for performance 