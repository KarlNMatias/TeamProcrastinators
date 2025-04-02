<template>
  <div>
    <h2>Users</h2>
    <ul v-if="users.length">
      <li v-for="user in users" :key="user.id">
        {{ user.name }}
        <button @click="deleteUser(user.id)">Delete</button>
      </li>
    </ul>
    <p v-else>Loading...</p>
    <input v-model="newUser" placeholder="Enter name" />
    <button @click="addUser">Add User</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      users: [],
      newUser: '',
    };
  },
  async created() {
    this.fetchUsers();
  },
  methods: {
    async fetchUsers() {
      try {
        const response = await axios.get('https://jsonplaceholder.typicode.com/users');
        this.users = response.data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    async addUser() {
      if (!this.newUser) return;
      try {
        const response = await axios.post('https://jsonplaceholder.typicode.com/users', {
          name: this.newUser,
        });
        this.users.push(response.data);
        this.newUser = '';
      } catch (error) {
        console.error('Error adding user:', error);
      }
    },
    async deleteUser(id) {
      try {
        await axios.delete(`https://jsonplaceholder.typicode.com/users/${id}`);
        this.users = this.users.filter(user => user.id !== id);
      } catch (error) {
        console.error('Error deleting user:', error);
      }
    },
  },
};
</script>

