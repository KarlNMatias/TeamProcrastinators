<template>
  <div class="page-container">
    <!-- Top Bar: Back Button -->
    <div class="top-bar">
      <router-link to="/" class="back-button">⬅️ Back</router-link>
    </div>

    <!-- Centered Post A Community Event sticky -->
    <div class="center-post">
      <div class="post-event-button" @click="showForm = !showForm">
        📝 Post A Community Event!
      </div>
    </div>

    <!-- Form sticky note -->
    <div v-if="showForm" class="form-sticky">
      <form @submit.prevent="addEvent">
        <input v-model="newEvent.name" placeholder="Event Name" required />
        <input v-model="newEvent.time" type="datetime-local" required />
        <input v-model="newEvent.where" placeholder="Location" required />
        <input v-model="newEvent.why" placeholder="Why (Purpose)" required />
        <button type="submit">Add Event</button>
      </form>
    </div>

    <!-- Event sticky notes -->
    <ul>
      <li 
        v-for="(event, index) in filteredEvents" 
        :key="index"
        @click="deleteEvent(index)"
        :class="['sticky-note', event.colorClass]"
      >
        <strong>{{ event.name }}</strong><br />
        When: {{ formatDate(event.time) }}<br />
        Where: {{ event.where }}<br />
        Why: {{ event.why }}
      </li>
    </ul>

    <!-- Trash bin bottom right -->
    <div class="trash-bin" @click="toggleTrash">
      🗑️ ({{ deletedEvents.length }})
    </div>

    <!-- Trash Modal -->
    <div v-if="showTrash" class="trash-modal">
      <h2>Deleted Events</h2>
      <ul>
        <li v-for="(deleted, idx) in deletedEvents" :key="idx" class="deleted-note">
          <strong>{{ deleted.name }}</strong><br />
          When: {{ formatDate(deleted.time) }}<br />
          Where: {{ deleted.where }}<br />
          Why: {{ deleted.why }}
          <div class="restore-button" @click="restoreEvent(idx)">Restore</div>
        </li>
      </ul>
      <button @click="toggleTrash">Close</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const newEvent = ref({ name: '', time: '', where: '', why: '' })
const events = ref([])
const deletedEvents = ref([])
const showForm = ref(false)
const showTrash = ref(false)

const colors = ['yellow-note', 'pink-note', 'blue-note', 'green-note', 'purple-note']

// Computed: Only show events that are not deleted
const filteredEvents = computed(() => {
  const deletedSet = new Set(deletedEvents.value.map(e => e.time + e.name))
  return events.value.filter(event => !deletedSet.has(event.time + event.name))
})

// Load saved events and deletedEvents from localStorage
const loadLocalData = () => {
  events.value = JSON.parse(localStorage.getItem('events')) || []
  deletedEvents.value = JSON.parse(localStorage.getItem('deletedEvents')) || []
}

// Save events and deletedEvents to localStorage
const saveLocalData = () => {
  localStorage.setItem('events', JSON.stringify(events.value))
  localStorage.setItem('deletedEvents', JSON.stringify(deletedEvents.value))
}

// Add a new event
const addEvent = () => {
  const newEntry = { ...newEvent.value, colorClass: randomColor() }
  events.value.push(newEntry)
  saveLocalData()
  newEvent.value = { name: '', time: '', where: '', why: '' }
  showForm.value = false
}

// Delete event and move to trash
const deleteEvent = (index) => {
  const removed = filteredEvents.value[index]
  if (removed) {
    deletedEvents.value.push(removed)
    events.value = events.value.filter(e => !(e.name === removed.name && e.time === removed.time))
    saveLocalData()
  }
}

// Restore event from trash
const restoreEvent = (idx) => {
  const restored = deletedEvents.value.splice(idx, 1)[0]
  events.value.push(restored)
  saveLocalData()
}

const toggleTrash = () => {
  showTrash.value = !showTrash.value
}

const randomColor = () => {
  return colors[Math.floor(Math.random() * colors.length)]
}

const formatDate = (datetime) => {
  const options = { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }
  return new Date(datetime).toLocaleString(undefined, options)
}

onMounted(loadLocalData)
</script>

<style scoped>
.page-container {
  background-color: #f5f0e1;
  min-height: 100vh;
  padding: 2rem;
  font-family: 'Comic Sans MS', cursive, sans-serif;
  position: relative;
}

/* Top Bar */
.top-bar {
  display: flex;
  justify-content: flex-start;
  margin-bottom: 2rem;
}

.back-button {
  background: #ffd1dc;
  border: 2px solid #ffb6c1;
  padding: 0.7rem 1.5rem;
  border-radius: 12px;
  text-decoration: none;
  color: #4b3b2b;
  font-weight: bold;
  box-shadow: 3px 3px 7px rgba(0,0,0,0.2);
  transform: rotate(-3deg);
  transition: background 0.3s, transform 0.3s;
}

.back-button:hover {
  background: #ffb6c1;
  transform: rotate(0deg) scale(1.03);
}

/* Center Post Button */
.center-post {
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
}

.post-event-button {
  background: #fff89a;
  border: 2px solid #f0e68c;
  padding: 1.5rem 3rem;
  border-radius: 12px;
  font-size: 1.8rem;
  font-weight: bold;
  color: #4b3b2b;
  box-shadow: 3px 3px 7px rgba(0,0,0,0.2);
  cursor: pointer;
  transform: rotate(-2deg);
  transition: background 0.3s, transform 0.3s;
}

.post-event-button:hover {
  background: #fff56d;
  transform: rotate(0deg) scale(1.03);
}

/* Form sticky */
.form-sticky {
  background: #fff89a;
  border: 2px solid #f0e68c;
  border-radius: 12px;
  box-shadow: 3px 3px 7px rgba(0,0,0,0.2);
  padding: 1rem;
  max-width: 400px;
  margin: 1rem auto 2rem;
  transform: rotate(1deg);
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
  background-color: #4b3b2b;
  color: white;
  border: none;
  cursor: pointer;
  transition: background 0.3s;
}

button:hover {
  background-color: #2e2216;
}

/* Sticky Notes */
ul {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
  list-style: none;
  padding: 0;
}

.sticky-note {
  box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
  padding: 1rem;
  width: 220px;
  border-radius: 12px;
  transform: rotate(-2deg);
  cursor: pointer;
  font-size: 0.95rem;
  transition: transform 0.2s;
}

.sticky-note:hover {
  transform: rotate(0deg) scale(1.03);
}

.yellow-note { background-color: #fff89a; border: 2px solid #f0e68c; }
.pink-note   { background-color: #ffd1dc; border: 2px solid #ffb6c1; }
.blue-note   { background-color: #add8e6; border: 2px solid #87ceeb; }
.green-note  { background-color: #c1f0c1; border: 2px solid #a8d5a8; }
.purple-note { background-color: #e1d5f5; border: 2px solid #b9a3e3; }

li:nth-child(odd) {
  transform: rotate(2deg);
}

/* Trash bin */
.trash-bin {
  position: fixed;
  bottom: 20px;
  right: 20px;
  font-size: 2.5rem;
  cursor: pointer;
  transition: transform 0.2s;
}

.trash-bin:hover {
  animation: wiggle 0.5s ease infinite;
}

@keyframes wiggle {
  0%, 100% { transform: rotate(0deg); }
  25% { transform: rotate(5deg); }
  50% { transform: rotate(-5deg); }
  75% { transform: rotate(5deg); }
}

/* Trash Modal */
.trash-modal {
  position: fixed;
  bottom: 80px;
  right: 20px;
  width: 300px;
  max-height: 400px;
  background: white;
  border: 2px solid #4b3b2b;
  box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
  overflow-y: auto;
  padding: 1rem;
  border-radius: 12px;
  z-index: 1000;
}

.deleted-note {
  background-color: #fff8e1;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  text-align: left;
  position: relative;
}

/* Restore button */
.restore-button {
  margin-top: 0.5rem;
  background: #4b3b2b;
  color: white;
  padding: 0.4rem 0.6rem;
  border-radius: 6px;
  text-align: center;
  font-size: 0.85rem;
  cursor: pointer;
  transition: background 0.3s;
}

.restore-button:hover {
  background: #2e2216;
}
</style>
