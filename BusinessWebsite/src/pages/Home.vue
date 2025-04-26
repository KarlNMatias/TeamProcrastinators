<template>
  <div class="home-container">
    <!-- About Sticky Note (Top Right) -->
    <router-link to="/about" class="about-sticky-note">
      <div class="about-text">About</div>
    </router-link>

    <!-- Title Sticky with Pins -->
    <div class="title-container">
      <div class="title-sticky">
        <h1 class="title-text">Post-It</h1>
        <div class="pins">
          <div class="pin">
            <div class="pin-head"></div>
            <div class="pin-stem"></div>
          </div>
          <div class="pin">
            <div class="pin-head"></div>
            <div class="pin-stem"></div>
          </div>
          <div class="pin">
            <div class="pin-head"></div>
            <div class="pin-stem"></div>
          </div>
          <div class="pin">
            <div class="pin-head"></div>
            <div class="pin-stem"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bulletin Board with Sticky Notes -->
    <div class="school-board">
      <nav class="nav">
        <router-link to="/page1" class="sticky-note yellow tilt-left">
          <div class="note-title">Community Events</div>
        </router-link>
        <router-link to="/page2" class="sticky-note pink tilt-right">
          <div class="note-title">Local Business</div>
        </router-link>
        <router-link to="/page3" class="sticky-note blue tilt-left">
          <div class="note-title">Funding</div>
        </router-link>
      </nav>
    </div>
  </div>
</template>

<script setup>
import './Home.css'
</script>
