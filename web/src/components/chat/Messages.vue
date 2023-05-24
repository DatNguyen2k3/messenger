<template>
  <v-virtual-scroll
    class="scrollable-list"
    :items="messages"
  > 
    <template v-slot:default="{ item }">
      <div v-if="item.from_user.id != user.id" class="receive-single-message">
        <v-avatar color="secondary">
          <v-img
            aspect-ratio="1/1"
            cover
            :src="item.from_user.avatar_img_url"
          ></v-img>
        </v-avatar>
        <v-chip class="ma-2" size="large"> {{ item.content }} </v-chip>
      </div>
      <div v-else class="send-single-message">
        <v-chip class="ma-2" size="large"> {{ item.content }} </v-chip>
        <v-avatar color="secondary">
          <v-img
            aspect-ratio="1/1"
            cover
            :src="item.from_user.avatar_img_url"
          ></v-img>
        </v-avatar>
      </div>
    </template>
  </v-virtual-scroll>
</template>

<script>


export default {
  name: "messages",
  props: ["selectedConversation", "user", "messages"],

  data() {

  },



  methods: {

  },
};
</script>

<style scoped>
.scrollable-list {
  height: 100%;
  width: 100%;
  overflow-y: auto;
  overflow-x: hidden;
}

.receive-single-message {
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  width: 100%;
}

.send-single-message {
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  width: 100%;
}

</style>
