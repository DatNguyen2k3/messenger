<template>
  <v-container class="box3">
    <v-col class="conversation-boxes">
      <v-row
        class="single-conversation"
        v-for="user in result_users"
        :key="user.id"
        @click="selectUser(user)"
      >
        <v-text>
          {{ user.username }}
        </v-text>
        <v-text class="latest-message">
          <b>email: </b>
          {{ user.email }}
        </v-text>
      </v-row>
    </v-col>
  </v-container>
</template>

<script>
export default {
  name: "user-list",
  props: ["result_users"],

  updated() {
    console.log(this.result_users);
  },

  data() {
    return {};
  },

  methods: {
    selectUser(user) {
      this.$emit("click-user", user);
    },
  },
};
</script>

<style scoped>
.box1 {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.75rem;
  background-color: white;
  width: 31%;
  border-radius: 12px;
  border-width: 1px;
}

.box2 {
  padding-bottom: 3px;
  padding-left: 3px;
  font-size: 28px;
  font-family: "Work Sans", sans-serif;
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
}

.box3 {
  display: flex;
  flex-direction: column;
  padding: 3px;
  background-color: #f8f8f8;
  width: 100%;
  height: 100%;
  border-radius: 12px;
  overflow-y: hidden;
}

.single-conversation {
  cursor: pointer;
  background-color: #e8e8e8;
  color: black;
  display: flex;
  flex-direction: column;
  padding-left: 0.75rem; /* Equivalent to px={3} */
  padding-right: 0.75rem; /* Equivalent to px={3} */
  padding-top: 0.5rem; /* Equivalent to py={2} */
  padding-bottom: 0.5rem; /* Equivalent to py={2} */
  border-radius: 12px;
  margin-bottom: 0.5rem;
  margin-left: 0.1rem;
  margin-right: 0.1rem;
  margin-top: 0.1rem;
}

.latest-message {
  font-size: 12px;
}

.conversation-boxes {
  overflow-y: scroll;
}
</style>
