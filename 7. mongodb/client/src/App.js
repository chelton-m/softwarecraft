import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const API_BASE_URL = 'http://localhost:5001/api';

function App() {
  const [users, setUsers] = useState([]);
  const [formData, setFormData] = useState({ name: '', email: '' });
  const [editingId, setEditingId] = useState(null);
  const [loading, setLoading] = useState(false);

  // Fetch all users
  const fetchUsers = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`${API_BASE_URL}/users`);
      setUsers(response.data);
    } catch (error) {
      console.error('Error fetching users:', error);
    } finally {
      setLoading(false);
    }
  };

  // Create new user
  const createUser = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      const response = await axios.post(`${API_BASE_URL}/users`, formData);
      setUsers([...users, response.data]);
      setFormData({ name: '', email: '' });
    } catch (error) {
      console.error('Error creating user:', error);
    } finally {
      setLoading(false);
    }
  };

  // Update user
  const updateUser = async (id) => {
    try {
      setLoading(true);
      const response = await axios.put(`${API_BASE_URL}/users/${id}`, formData);
      setUsers(users.map(user => user._id === id ? response.data : user));
      setFormData({ name: '', email: '' });
      setEditingId(null);
    } catch (error) {
      console.error('Error updating user:', error);
    } finally {
      setLoading(false);
    }
  };

  // Delete user
  const deleteUser = async (id) => {
    try {
      setLoading(true);
      await axios.delete(`${API_BASE_URL}/users/${id}`);
      setUsers(users.filter(user => user._id !== id));
    } catch (error) {
      console.error('Error deleting user:', error);
    } finally {
      setLoading(false);
    }
  };

  // Start editing user
  const startEdit = (user) => {
    setFormData({ name: user.name, email: user.email });
    setEditingId(user._id);
  };

  // Cancel editing
  const cancelEdit = () => {
    setFormData({ name: '', email: '' });
    setEditingId(null);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>MERN + MongoDB Tutorial</h1>
        <p>Learn MongoDB through hands-on CRUD operations</p>
      </header>

      <main className="App-main">
        {/* Form Section */}
        <section className="form-section">
          <h2>{editingId ? 'Edit User' : 'Add New User'}</h2>
          <form onSubmit={editingId ? (e) => { e.preventDefault(); updateUser(editingId); } : createUser}>
            <div className="form-group">
              <input
                type="text"
                placeholder="Name"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                required
              />
            </div>
            <div className="form-group">
              <input
                type="email"
                placeholder="Email"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                required
              />
            </div>
            <div className="form-actions">
              <button type="submit" disabled={loading}>
                {loading ? 'Saving...' : (editingId ? 'Update' : 'Add User')}
              </button>
              {editingId && (
                <button type="button" onClick={cancelEdit} className="cancel-btn">
                  Cancel
                </button>
              )}
            </div>
          </form>
        </section>

        {/* Users List Section */}
        <section className="users-section">
          <h2>Users ({users.length})</h2>
          {loading && <p className="loading">Loading...</p>}
          <div className="users-grid">
            {users.map(user => (
              <div key={user._id} className="user-card">
                <div className="user-info">
                  <h3>{user.name}</h3>
                  <p>{user.email}</p>
                  <small>Created: {new Date(user.createdAt).toLocaleDateString()}</small>
                </div>
                <div className="user-actions">
                  <button 
                    onClick={() => startEdit(user)}
                    className="edit-btn"
                    disabled={loading}
                  >
                    Edit
                  </button>
                  <button 
                    onClick={() => deleteUser(user._id)}
                    className="delete-btn"
                    disabled={loading}
                  >
                    Delete
                  </button>
                </div>
              </div>
            ))}
          </div>
          {users.length === 0 && !loading && (
            <p className="no-users">No users found. Add your first user above!</p>
          )}
        </section>
      </main>

      <footer className="App-footer">
        <p>MongoDB Concepts Demonstrated:</p>
        <ul>
          <li>✅ Database Connection</li>
          <li>✅ Schema Definition</li>
          <li>✅ CRUD Operations (Create, Read, Update, Delete)</li>
          <li>✅ Error Handling</li>
          <li>✅ Real-time Data Updates</li>
        </ul>
      </footer>
    </div>
  );
}

export default App;
