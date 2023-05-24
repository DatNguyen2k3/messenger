<template>
    <v-text class="title">
      
      {{selectedConversation.name}}
    </v-text>

    <v-container class="message-box">
      <messages 
        v-if="selectedConversation"
        style="height:85%"
        :selectedConversation="selectedConversation"
        :user="user"
        :messages="messages"
      ></messages>
      <v-form class="send-message-form" @submit.prevent @submit="sendMessage">
        <v-text-field required placeholder="Enter your message" class='send-message-box' v-model="currentMessage"></v-text-field>
      </v-form>
    </v-container>
</template>

<script>
import Messages from '@/components/chat/Messages.vue';

export default {
  name: 'single-chat',
  props: ['selectedConversation', 'user'],

  components: {
    Messages,
  },

  data() {
    return {
      messages: [],
      currentMessage: '',
    }
  }, 

  created() {
    this.getMessages();
  },
  
  methods: {
    getMessages() {
      axios.get(`/api/messages?conversation_id=${this.selectedConversation.id}`)
        .then(response => {
          this.messages = response.data;
          this.messages.reverse();
        })
        .catch(error => {
          console.log(error);
        });
    },

    sendMessage() {
      axios.post('/api/messages', {
        from_user: this.user.id,
        content: this.currentMessage,
        to_conversation: this.selectedConversation.id,
      })
        .then(response => {
          this.messages.push(response.data);
          this.currentMessage = '';
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
}

</script>

<style scoped>

.title {
  font-size: 30px;
  padding-bottom: 0.75rem; 
  padding-left: 0.5rem;   
  padding-right: 0.5rem;
  width: 100%;
  font-family: 'Work Sans', sans-serif;
  display: flex;
  align-items: center;  
}

.message-box {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 0.75rem;
  background-color: #E8E8E8;
  width: 100%;
  height: 100%;
  border-radius: 12px;
  overflow: hidden;
}

.send-message-form {
  margin-top: 3rem;
  height: 10%;
}



</style>