<template>
  <v-virtual-scroll
    :items="[
      '1',
      '2',
      '3',
      '4',
      '5',
      '6',
      '7',
      '8',
      '9',
      '10',
      '11',
      '12',
      '13',
      '14',
      '15',
      '16',
      '17',
      '18',
      '19',
      '20',
      '21',
      '22',
      '23',
      '24',
      '25',
      '26',
      '27',
      '28',
      '29',
      '30',
    ]"
    class="scrollable-list"
  >
    <template v-slot:default="{ item }">
      <div v-if="item % 2 == 0" class="receive-single-message">
        <v-avatar color="secondary">
          <v-img
            aspect-ratio="1/1"
            cover
            src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
          ></v-img>
        </v-avatar>
        <v-chip class="ma-2" size="large"> x-large chip </v-chip>
      </div>
      <div v-else class="send-single-message">
        <v-chip class="ma-2" size="large"> x-large chip </v-chip>
        <v-avatar color="secondary">
          <v-img
            aspect-ratio="1/1"
            cover
            src="http://localhost:8000/static/avatar_imgs/user23.jpg"
          ></v-img>
        </v-avatar>
      </div>
    </template>
  </v-virtual-scroll>
</template>

<script>
export default {
  name: "messages",

  data() {
    return {};
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
