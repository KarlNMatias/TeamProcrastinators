<template>
  <div class="about-page-container">
    <!-- Top Bar with Back Button -->
    <div class="top-bar">
      <router-link to="/" class="back-button">⬅️ Back</router-link>
    </div>

    <!-- Title -->
    <div class="about-title-container">
      <div class="about-title-sticky">
        <div class="pin-emoji">📌</div>
        <h1 class="about-title-text">Meet the Team</h1>
      </div>
    </div>

    <!-- Sticky Notes for Workers -->
    <div class="about-sticky-board">
      <!-- Bennett Bush -->
      <div class="worker-sticky yellow tilt-left">
        <strong>Bennett Bush</strong><br />
        Computer Science Major<br />
        Junior
      </div>

      <!-- Larchelle Tuifao -->
      <div class="worker-sticky pink tilt-right">
        <strong>Larchelle Tuifao</strong><br />
        Computer Science Major<br />
        Senior
      </div>

      <!-- Karl Nick Matias -->
      <div class="worker-sticky blue tilt-left">
        <strong>Karl Nick Matias</strong><br />
        Computer Science Major<br />
        Junior
      </div>
    </div>
  </div>
</template>

<script setup>
// Nothing needed yet
</script>

<style scoped>
.about-page-container {
  background-color: #f5f0e1;
  min-height: 100vh;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: 'Comic Sans MS', cursive, sans-serif;
  position: relative;
}

/* Top Bar for Back Button */
.top-bar {
  position: absolute;
  top: 20px;
  left: 20px;
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
  transition: background 0.3s, transform 0.3s;
}

.back-button:hover {
  background: #ffb6c1;
  transform: scale(1.05);
}

/* Title Sticky */
.about-title-container {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 5rem; /* Adjust for top bar */
  margin-bottom: 3rem;
  position: relative;
}

.about-title-sticky {
  position: relative;
  background: #fff89a;
  padding: 2rem 4rem;
  border: 2px solid #f0e68c;
  border-radius: 12px;
  box-shadow: 5px 5px 10px rgba(0,0,0,0.15);
  text-align: center;
  width: fit-content;
}

.pin-emoji {
  position: absolute;
  top: -24px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 2rem;
}

.about-title-text {
  font-size: 3rem;
  color: #4b3b2b;
  margin: 0;
  font-weight: bold;
}

/* Sticky Board */
.about-sticky-board {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
  align-items: center;
}

/* Worker Sticky Notes */
.worker-sticky {
  position: relative;
  width: 220px;
  height: 220px;
  padding: 1rem;
  background-color: #fff89a;
  border: 2px solid #f0e68c;
  border-radius: 12px;
  box-shadow: 4px 4px 10px rgba(0,0,0,0.15);
  text-align: center;
  font-weight: bold;
  color: #4b3b2b;
  display: flex;
  flex-direction: column;
  justify-content: center;
  font-size: 1.2rem;
  transition: transform 0.3s;
}

.worker-sticky:hover {
  transform: scale(1.05);
}

/* Tilts */
.tilt-left {
  transform: rotate(-3deg);
}

.tilt-right {
  transform: rotate(3deg);
}

/* Sticky note colors */
.yellow {
  background-color: #fff89a;
  border: 2px solid #f0e68c;
}

.pink {
  background-color: #ffd1dc;
  border: 2px solid #ffb6c1;
}

.blue {
  background-color: #add8e6;
  border: 2px solid #87ceeb;
}
</style>
