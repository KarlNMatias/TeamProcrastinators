<template>
  <div class="page-container">
    <!-- Top Bar -->
    <div class="top-bar">
      <router-link to="/" class="back-button">⬅️ Back</router-link>
    </div>

    <!-- Center Post Your Business button -->
    <div class="center-post">
      <div class="post-business-button" @click="showForm = !showForm">
        🏢 Post Your Business!
      </div>
    </div>

    <!-- Form flyer -->
    <div v-if="showForm" class="form-flyer">
      <form @submit.prevent="addBusiness">
        <input v-model="newBusiness.name" placeholder="Business Name" required />
        <input v-model="newBusiness.type" placeholder="Type (e.g. Café, Bookstore)" required />
        <input v-model="newBusiness.location" placeholder="Location" required />
        <input v-model="newBusiness.contact" placeholder="Contact Info" required />
        <button type="submit">Add Business</button>
      </form>
    </div>

    <!-- Business flyers -->
    <ul>
      <li 
        v-for="(business, index) in filteredBusinesses" 
        :key="index" 
        @click="deleteBusiness(index)"
        class="business-flyer"
      >
        <!-- Staple dots -->
        <div class="staple top-left"></div>
        <div class="staple top-right"></div>

        <div class="flyer-content">
          <strong>{{ business.name }}</strong><br />
          Type: {{ business.type }}<br />
          Location: {{ business.location }}<br />
          Contact: {{ business.contact }}
        </div>
      </li>
    </ul>

    <!-- Shredder -->
    <div class="shredder" @click="toggleTrash">
      🗑️ ({{ deletedBusinesses.length }})
    </div>

    <!-- Trash Modal -->
    <div v-if="showTrash" class="trash-modal">
      <h2>Shredded Businesses</h2>
      <ul>
        <li v-for="(biz, idx) in deletedBusinesses" :key="idx" class="deleted-sheet">
          <strong>{{ biz.name }}</strong><br />
          Type: {{ biz.type }}<br />
          Location: {{ biz.location }}<br />
          Contact: {{ biz.contact }}
          <div class="restore-button" @click="restoreBusiness(idx)">Restore</div>
        </li>
      </ul>
      <button @click="toggleTrash">Close</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const newBusiness = ref({ name: '', type: '', location: '', contact: '' })
const businesses = ref([])
const deletedBusinesses = ref([])
const showForm = ref(false)
const showTrash = ref(false)

// Computed list: Only businesses not deleted
const filteredBusinesses = computed(() => {
  const deletedSet = new Set(deletedBusinesses.value.map(b => b.name + b.location))
  return businesses.value.filter(biz => !deletedSet.has(biz.name + biz.location))
})

// Load businesses and deleted ones
const loadLocalData = () => {
  businesses.value = JSON.parse(localStorage.getItem('businesses')) || []
  deletedBusinesses.value = JSON.parse(localStorage.getItem('deletedBusinesses')) || []
}

// Save to localStorage
const saveLocalData = () => {
  localStorage.setItem('businesses', JSON.stringify(businesses.value))
  localStorage.setItem('deletedBusinesses', JSON.stringify(deletedBusinesses.value))
}

// Add new business
const addBusiness = () => {
  const newEntry = { ...newBusiness.value }
  businesses.value.push(newEntry)
  saveLocalData()
  newBusiness.value = { name: '', type: '', location: '', contact: '' }
  showForm.value = false
}

// Delete business
const deleteBusiness = (index) => {
  const removed = filteredBusinesses.value[index]
  if (removed) {
    deletedBusinesses.value.push(removed)
    saveLocalData()
  }
}

// Restore business from trash
const restoreBusiness = (idx) => {
  const restored = deletedBusinesses.value.splice(idx, 1)[0]
  businesses.value.push(restored)
  saveLocalData()
}

// Trash modal toggle
const toggleTrash = () => {
  showTrash.value = !showTrash.value
}

onMounted(loadLocalData)
</script>

<style scoped>
.page-container {
  background-color: #f1f8e9;
  min-height: 100vh;
  padding: 2rem;
  font-family: 'Arial', sans-serif;
  position: relative;
}

/* Top bar */
.top-bar {
  display: flex;
  justify-content: flex-start;
  margin-bottom: 2rem;
}

.back-button {
  background: #c8e6c9;
  border: 2px solid #a5d6a7;
  padding: 0.7rem 1.5rem;
  border-radius: 12px;
  text-decoration: none;
  color: #2e7d32;
  font-weight: bold;
  box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
  transition: background 0.3s;
}

.back-button:hover {
  background: #a5d6a7;
}

/* Post button */
.center-post {
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
}

.post-business-button {
  background: #dcedc8;
  border: 2px solid #c5e1a5;
  padding: 1.5rem 3rem;
  border-radius: 12px;
  font-size: 1.8rem;
  font-weight: bold;
  color: #33691e;
  box-shadow: 3px 3px 7px rgba(0,0,0,0.2);
  cursor: pointer;
  transition: background 0.3s;
}

.post-business-button:hover {
  background: #c5e1a5;
}

/* Form flyer */
.form-flyer {
  background: #ffffff;
  border: 2px solid #c8e6c9;
  border-radius: 8px;
  box-shadow: 3px 3px 7px rgba(0,0,0,0.2);
  padding: 1rem;
  max-width: 400px;
  margin: 1rem auto 2rem;
}

form {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

input, button {
  padding: 0.5rem;
  font-size: 1rem;
  border-radius: 6px;
}

button {
  background-color: #558b2f;
  color: white;
  border: none;
  cursor: pointer;
  transition: background 0.3s;
}

button:hover {
  background-color: #33691e;
}

/* Flyers */
ul {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2rem;
  list-style: none;
  padding: 0;
}

.business-flyer {
  position: relative;
  background-color: #ffffff;
  border: 2px solid #c8e6c9;
  box-shadow: 4px 4px 8px rgba(0,0,0,0.2);
  padding: 1.5rem;
  width: 260px;
  height: 220px;
  border-radius: 8px;
  text-align: center;
  transition: transform 0.2s, background 0.3s;
  cursor: pointer;
}

.business-flyer:hover {
  transform: scale(1.03);
  background-color: #f0f8f0;
}

/* Staple dots */
.staple {
  position: absolute;
  width: 10px;
  height: 10px;
  background: #555;
  border-radius: 50%;
}

.top-left {
  top: 10px;
  left: 10px;
}

.top-right {
  top: 10px;
  right: 10px;
}

.flyer-content {
  margin-top: 1.5rem;
}

/* Shredder */
.shredder {
  position: fixed;
  bottom: 20px;
  right: 20px;
  font-size: 2.5rem;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.shredder:hover {
  animation: wiggle 0.5s ease infinite;
}

@keyframes wiggle {
  0%, 100% { transform: rotate(0deg); }
  25% { transform: rotate(3deg); }
  50% { transform: rotate(-3deg); }
  75% { transform: rotate(3deg); }
}

/* Trash Modal */
.trash-modal {
  position: fixed;
  bottom: 80px;
  right: 20px;
  width: 300px;
  max-height: 400px;
  background: white;
  border: 2px solid #558b2f;
  box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
  overflow-y: auto;
  padding: 1rem;
  border-radius: 12px;
  z-index: 1000;
}

.deleted-sheet {
  background-color: #f0f8f0;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  text-align: left;
  position: relative;
}

/* Restore button */
.restore-button {
  margin-top: 0.5rem;
  background: #558b2f;
  color: white;
  padding: 0.4rem 0.6rem;
  border-radius: 6px;
  text-align: center;
  font-size: 0.85rem;
  cursor: pointer;
  transition: background 0.3s;
}

.restore-button:hover {
  background: #33691e;
}
</style>
