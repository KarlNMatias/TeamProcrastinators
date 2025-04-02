<template>
  <div>
    <h2>Users</h2>
    <ul v-if="users.length">
      <li v-for="user in users" :key="user.id">{{ user.name }}</li>
    </ul>
    <p v-else>Loading...</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      users: [],
    };
  },
  async created() {
    try {
      const response = await axios.get('https://jsonplaceholder.typicode.com/users');
      this.users = response.data;
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  },
};
</script>

