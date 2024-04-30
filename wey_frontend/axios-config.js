// axios-config.js

import axios from 'axios';

// Configurez le port par défaut pour toutes les requêtes Axios
axios.defaults.baseURL = 'http://localhost:8000'; // Spécifiez le nouveau port ici

// Exportez Axios configuré
export default axios;
