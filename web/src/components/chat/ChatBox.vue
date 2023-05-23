<template>
    <v-container class="chat-box">
      <single-chat ></single-chat>
      
    </v-container>
</template>

<script>
import SingleChat from '@/components/chat/SingleChat.vue';


export default {
  name: 'chat-box',

  components: {
    SingleChat,
  },

  data() {
    return {

    }
  },    
}
</script>

<style scoped>

.chat-box {
  display: flex;
  align-items: center;
  flex-direction: column;
  padding: 0.75rem;
  background-color: white;
  width: 68%;
  border-radius: 12px;
  border-width: 1px;
}

</style>