<template>

  <v-toolbar class="chat-bar" style="justify-content: space-between;">
    <div style="width: 100%; display: flex; justify-content: space-between; align-items: center;">

      <v-btn @click="setSearch">
        <v-icon>mdi-magnify</v-icon>
        <span class="hidden md:inline-block">Search User</span>
      </v-btn>
  
      <v-text class="chat-bar-title">Messenger</v-text>
  
      <div>
        <v-avatar color="info" size="x-large">
          <v-img
            aspect-ratio="1/1"
            cover
            src="http://localhost:8000/static/avatar_imgs/user23.jpg"
          ></v-img>
        </v-avatar>
      </div>
    </div>


  </v-toolbar>

  <v-navigation-drawer
    v-model="isSearch"
    location="left"
    temporary
    style="width: 30%;"
    class="search-box"
  >
    <v-form @submit.prevent class="search-form">
      <v-text-field label="Search User" ></v-text-field>
    </v-form>
    <user-list class="users"></user-list>
  </v-navigation-drawer>

</template>

<script>
import UserList from '@/components/chat/UserList.vue';

export default {

  name: 'side-drawer',

  components: {
    UserList,
  },

  data() {
    return {
      isSearch: false,
      search: '',
      loading: false,
      searchResult: [],
      notification: [],
      user: {
        name: '',
        pic: ''
      }
    };
  },
  methods: {
    setSearch() {
      this.isSearch = !this.isSearch;
    },
  }

};
</script>

<style scoped>

.chat-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 5px 10px 5px 10px;
  border-width: 5px;
  background-color: white;
}

.chat-bar-title {
  font-size: 2rem;
  font-family: 'Work Sans', sans-serif;
}

.search-box {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

.search-form {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 90%;
  margin-top: 5%;
  margin-left: 5%;
  margin-right: 5%;
  height: 15%;
}

.users {
  margin-left: 5%;
  margin-right: 5%;
  margin-bottom: 5%;
  height: 75%;
  width: 90%;
}

</style>
