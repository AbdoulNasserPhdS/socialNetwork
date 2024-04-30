// import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import './index.css'


import axios from 'axios'


// In you main.js
// ... considering that your app creation is here
import Toaster from "@meforma/vue-toaster";
//on mets l'url de django
axios.defaults.baseURL =import.meta.env.VITE_API_URL

const app = createApp(App)

app.use(createPinia())
app.use(router,axios)
app.use(Toaster)
app.mount('#app')







// import App from './App.vue'
// import router from './router'
// import axios from 'axios'

// import './assets/main.css'

// axios.defaults.baseURL = import.meta.env.VITE_API_URL

// const app = createApp(App)