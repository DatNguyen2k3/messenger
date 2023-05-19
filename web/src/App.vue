<template>
  <v-app>
    <v-main class="app">
      <v-botttom-navigation>
        <v-btn :to="{name: 'home'}" prepend-icon="mdi-home">Home</v-btn>
        <v-btn :to="{name: 'about'}" prepend-icon="mdi-information-outline">About</v-btn>
        <v-btn :to="{name: 'helloworld'}" prepend-icon="mdi-new-box">Hello World</v-btn>
        <v-btn :to="{name: 'login'}" prepend-icon="mdi-new-box">Login </v-btn>


      </v-botttom-navigation>
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

    const getUsers = async () => {
      await axios
        .get("/api/users")
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    };

    getUsers();
    console.log("Hello World");
  },

  
});


</script>
