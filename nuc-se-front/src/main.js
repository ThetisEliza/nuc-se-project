import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router/index.js'


import { aliases, mdi } from 'vuetify/iconsets/mdi'

import 'vuetify/styles'
import "vuetify/dist/vuetify.min.css";

import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import '@mdi/font/css/materialdesignicons.css'

const vuetify = createVuetify({
    components,
    directives,
    ssr: true,
    theme: {
      defaultTheme: 'light',
      //
    },
    icons: {
      defaultSet: 'mdi',
      aliases,
      sets: {
        mdi,
      },
    },
  })

createApp(App).use(router).use(vuetify).use(VueAxios, axios).mount('#app')
