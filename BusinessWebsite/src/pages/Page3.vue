<template>
  <div class="page-container">
    <!-- Top Bar -->
    <div class="top-bar">
      <router-link to="/" class="back-button">⬅️ Back</router-link>
    </div>

    <!-- Post Opportunity Button -->
    <div class="center-post">
      <div class="post-opportunity-button" @click="showForm = !showForm">
        📄 Post a Funding Opportunity!
      </div>
    </div>

    <!-- Form to Post New -->
    <div v-if="showForm" class="form-sheet">
      <form @submit.prevent="addOpportunity">
        <input v-model="newOpportunity.name" placeholder="Opportunity Name" required />
        <input v-model="newOpportunity.deadline" type="date" required />
        <input v-model="newOpportunity.source" placeholder="Funding Source" required />
        <input v-model="newOpportunity.description" placeholder="Short Description" required />
        <button type="submit">Add Opportunity</button>
      </form>
    </div>

    <!-- Flyers -->
    <ul>
      <li 
        v-for="(opportunity, index) in filteredOpportunities" 
        :key="index" 
        @click="deleteSticky(index)"
        class="opportunity-sheet"
      >
        <div class="paperclip"></div>
        <div class="sheet-content">
          <strong>{{ opportunity.name }}</strong><br />
          Deadline: {{ opportunity.deadline }}<br />
          Source: {{ opportunity.source }}<br />
          Description: {{ opportunity.description }}
        </div>
      </li>
    </ul>

    <!-- Trash bin -->
    <div class="trash-bin" @click="toggleTrash">
      🗑️ ({{ deletedOpportunities.length }})
    </div>

    <!-- Trash Modal -->
    <div v-if="showTrash" class="trash-modal">
      <h2>Deleted Opportunities</h2>
      <ul>
        <li v-for="(item, idx) in deletedOpportunities" :key="idx" class="deleted-sheet">
          <strong>{{ item.name }}</strong><br />
          Deadline: {{ item.deadline }}<br />
          Source: {{ item.source }}<br />
          Description: {{ item.description }}
          <div class="restore-button" @click="restoreOpportunity(idx)">Restore</div>
        </li>
      </ul>
      <button @click="toggleTrash">Close</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const newOpportunity = ref({ name: '', deadline: '', source: '', description: '' })
const opportunities = ref([])
const deletedOpportunities = ref([])
const showForm = ref(false)
const showTrash = ref(false)

// Computed - Only show not-deleted ones
const filteredOpportunities = computed(() => {
  const deletedSet = new Set(deletedOpportunities.value.map(op => op.name + op.source))
  return opportunities.value.filter(op => !deletedSet.has(op.name + op.source))
})

// Load saved data
const loadLocalData = () => {
  opportunities.value = JSON.parse(localStorage.getItem('opportunities')) || []
  deletedOpportunities.value = JSON.parse(localStorage.getItem('deletedOpportunities')) || []
}

// Save to localStorage
const saveLocalData = () => {
  localStorage.setItem('opportunities', JSON.stringify(opportunities.value))
  localStorage.setItem('deletedOpportunities', JSON.stringify(deletedOpportunities.value))
}

// Add opportunity
const addOpportunity = () => {
  const newEntry = { ...newOpportunity.value }
  opportunities.value.push(newEntry)
  saveLocalData()
  newOpportunity.value = { name: '', deadline: '', source: '', description: '' }
  showForm.value = false
}

// Delete opportunity
const deleteSticky = (index) => {
  const removed = filteredOpportunities.value[index]
  if (removed) {
    deletedOpportunities.value.push(removed)
    saveLocalData()
  }
}

// Restore opportunity from trash
const restoreOpportunity = (idx) => {
  const restored = deletedOpportunities.value.splice(idx, 1)[0]
  opportunities.value.push(restored)
  saveLocalData()
}

// Toggle trash modal
const toggleTrash = () => {
  showTrash.value = !showTrash.value
}

onMounted(loadLocalData)
</script>

<style scoped>
.page-container {
  background-color: #fff3e0;
  min-height: 100vh;
  padding: 2rem;
  font-family: 'Arial', sans-serif;
  position: relative;
}

.top-bar {
  display: flex;
  justify-content: flex-start;
  margin-bottom: 2rem;
}

.back-button {
  background: #ffe0b2;
  border: 2px solid #ffcc80;
  padding: 0.7rem 1.5rem;
  border-radius: 12px;
  text-decoration: none;
  color: #ef6c00;
  font-weight: bold;
  box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
  transition: background 0.3s;
}

.back-button:hover {
  background: #ffcc80;
}

.center-post {
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
}

.post-opportunity-button {
  background: #ffe0b2;
  border: 2px solid #ffcc80;
  padding: 1.5rem 3rem;
  border-radius: 12px;
  font-size: 1.8rem;
  font-weight: bold;
  color: #e65100;
  box-shadow: 3px 3px 7px rgba(0,0,0,0.2);
  cursor: pointer;
  transition: background 0.3s;
}

.post-opportunity-button:hover {
  background: #ffcc80;
}

.form-sheet {
  background: #ffffff;
  border: 2px solid #ffe0b2;
  border-radius: 8px;
  box-shadow: 3px 3px 7px rgba(0,0,0,0.2);
  padding: 1rem;
  max-width: 400px;
  margin: 1rem auto 2rem;
}

ul {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2rem;
  list-style: none;
  padding: 0;
}

.opportunity-sheet {
  position: relative;
  background-color: #ffffff;
  border: 2px solid #ffe0b2;
  box-shadow: 4px 4px 8px rgba(0,0,0,0.2);
  padding: 1.5rem;
  width: 260px;
  height: 240px;
  border-radius: 8px;
  text-align: center;
  transition: transform 0.2s, background 0.3s;
  cursor: pointer;
}

.opportunity-sheet:hover {
  transform: scale(1.03);
  background-color: #fff8e1;
}

.paperclip {
  position: absolute;
  top: 10px;
  left: 10px;
  width: 12px;
  height: 20px;
  border: 2px solid #555;
  border-top: none;
  border-left: none;
  transform: rotate(-20deg);
}

/* Trash Bin */
.trash-bin {
  position: fixed;
  bottom: 20px;
  right: 20px;
  font-size: 2.5rem;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.trash-bin:hover {
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
  border: 2px solid #ef6c00;
  box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
  overflow-y: auto;
  padding: 1rem;
  border-radius: 12px;
  z-index: 1000;
}

.deleted-sheet {
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
  background: #ef6c00;
  color: white;
  padding: 0.4rem 0.6rem;
  border-radius: 6px;
  text-align: center;
  font-size: 0.85rem;
  cursor: pointer;
  transition: background 0.3s;
}

.restore-button:hover {
  background: #e65100;
}
</style>
