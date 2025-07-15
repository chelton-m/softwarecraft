# 🚀 MongoDB Tutorial Setup Guide

## Step 1: Install MongoDB

### Option A: Local MongoDB Installation
```bash
# macOS (using Homebrew)
brew tap mongodb/brew
brew install mongodb-community

# Start MongoDB service
brew services start mongodb/brew/mongodb-community
```

### Option B: MongoDB Atlas (Cloud)
1. Go to [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Create free account
3. Create new cluster
4. Get connection string
5. Update `config.env` with your connection string

## Step 2: Install Dependencies

```bash
# Install backend dependencies
npm install

# Install frontend dependencies
cd client && npm install
```

## Step 3: Start the Application

### Terminal 1 - Start Backend Server
```bash
npm run dev
```
You should see:
- "Server running on port 5000"
- "Connected to MongoDB!"

### Terminal 2 - Start Frontend
```bash
npm run client
```
This will open React app at http://localhost:3000

## Step 4: Test the Application

1. **Add a User:**
   - Fill in name and email
   - Click "Add User"
   - User appears in the list below

2. **Edit a User:**
   - Click "Edit" on any user
   - Modify name/email
   - Click "Update"

3. **Delete a User:**
   - Click "Delete" on any user
   - User disappears from list

## 🎯 MongoDB Concepts You're Learning

### 1. **Database Connection**
```javascript
mongoose.connect('mongodb://localhost:27017/mern-tutorial')
```
- Connects to MongoDB database
- Creates database if it doesn't exist

### 2. **Schema Definition**
```javascript
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  createdAt: { type: Date, default: Date.now }
});
```
- Defines data structure
- Sets validation rules
- Specifies data types

### 3. **CRUD Operations**

#### Create (POST /api/users)
```javascript
const user = new User(req.body);
const savedUser = await user.save();
```

#### Read (GET /api/users)
```javascript
const users = await User.find(); // Get all
const user = await User.findById(id); // Get by ID
```

#### Update (PUT /api/users/:id)
```javascript
const user = await User.findByIdAndUpdate(id, data, { new: true });
```

#### Delete (DELETE /api/users/:id)
```javascript
const user = await User.findByIdAndDelete(id);
```

## 🔍 Understanding MongoDB

### Collections vs Documents
- **Collection:** Like a table in SQL (e.g., 'users')
- **Document:** Like a row in SQL (e.g., individual user data)

### MongoDB vs SQL
| MongoDB | SQL |
|---------|-----|
| Database | Database |
| Collection | Table |
| Document | Row |
| Field | Column |

### Query Examples
```javascript
// Find all users
User.find()

// Find user by email
User.findOne({ email: 'john@example.com' })

// Find users created today
User.find({ createdAt: { $gte: new Date().setHours(0,0,0,0) } })

// Count total users
User.countDocuments()
```

## 🛠️ Next Steps

1. **Add Authentication**
   - User registration/login
   - JWT tokens
   - Password hashing

2. **Advanced Queries**
   - Aggregation pipelines
   - Complex filtering
   - Sorting and pagination

3. **Data Validation**
   - Schema validation
   - Custom validators
   - Error handling

4. **Performance**
   - Indexes
   - Query optimization
   - Connection pooling

## 🐛 Troubleshooting

### MongoDB Connection Issues
- Ensure MongoDB is running
- Check connection string in `config.env`
- Verify port 27017 is available

### CORS Issues
- Backend has CORS enabled
- Frontend runs on port 3000
- Backend runs on port 5000

### Common Errors
- `MongoDB connection error`: Check if MongoDB is running
- `ValidationError`: Check required fields in form
- `Duplicate key error`: Email must be unique 