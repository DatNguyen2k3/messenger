<template>
    <v-container class="chat-box">
      <single-chat 
        v-if="selectedConversation"
        :selectedConversation="selectedConversation"
        :user="user"
        @message-sent="$emit('message-sent')"
        
      ></single-chat>
      
    </v-container>
</template>

<script>
import SingleChat from '@/components/chat/SingleChat.vue';


export default {
  name: 'chat-box',
  props: ['selectedConversation', 'user'],

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