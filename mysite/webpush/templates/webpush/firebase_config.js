// Initialize Firebase
var config = {
    apiKey: "{{ firebase_config.apiKey|default:'' }}",
    authDomain: "{{ firebase_config.authDomain|default:'' }}",
    databaseURL: "{{ firebase_config.databaseURL|default:'' }}",
    storageBucket: "{{ firebase_config.storageBucket|default:'' }}",
    messagingSenderId: "{{ firebase_config.messagingSenderId|default:'' }}",
    appId: "{{ firebase_config.appId|default:'' }}",
    projectId: "{{ firebase_config.projectId|default:'' }}"
};
firebase.initializeApp(config);
