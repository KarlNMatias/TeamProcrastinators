import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

const app = createApp(App); // Define `app` before using it
app.use(router);
app.mount('#app');

