<template>
  <v-app>
    <v-main class="app">
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import { defineComponent } from 'vue';
import "@/styles/app.css";
import { useRouter } from 'vue-router';


export default defineComponent({
  name: 'App',

  setup() {

    if (!localStorage.getItem('user')) {
      const router = useRouter();
      router.push('/');
    }

  },

  
});


</script>
