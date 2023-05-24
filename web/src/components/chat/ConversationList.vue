<template>
  <v-container class="box1">
    
    <v-container class="box2">
      <div>Conversations</div>
    </v-container>
    
    <v-container class="box3" >
      <v-col class="conversation-boxes" v-if="conversations">

        <v-row 
          class="single-conversation" 
          v-for="conversation in conversations" 
          :key="conversation.id"
          @click="selectedConversation = conversation; $emit('conversation-clicked', conversation)"
          :style="getConversationStyle(conversation)"
        >
          
          <v-text>
            {{ conversation.name }}
          </v-text>
          <v-text class="latest-message">
            <b>{{ conversation.latest_message.from_user.username }}: </b>
            {{ conversation.latest_message.content }}
          </v-text>
        </v-row>

      </v-col>
      <v-text v-else>
        No conversation
      </v-text>
    </v-container>
  
  </v-container>

</template>

<script>
export default {
  name: 'conversation-list',

  props: ['conversations', 'selectedConversation'],
  setup() {

  },


  data() {
    return {

    }
  }, 
  


  methods: {
    getConversationStyle(conversation) {
      return {
        backgroundColor: this.selectedConversation == conversation ? '#47A992' : '#E8E8E8',
        color: this.selectedConversation == conversation ? 'white' : 'black',
      }
    },
  }
}

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
  font-family: 'Work Sans', sans-serif;
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
}

.box3 {
  display: flex;
  flex-direction: column;
  padding: 3px;
  background-color: #F8F8F8;
  width: 100%;
  height: 100%;
  border-radius: 12px;
  overflow-y: hidden;
}

.single-conversation {
  cursor: pointer;
  background-color: #E8E8E8;
  color: black;
  display: flex;
  flex-direction: column;
  padding-left: 0.75rem;  /* Equivalent to px={3} */
  padding-right: 0.75rem; /* Equivalent to px={3} */
  padding-top: 0.5rem;    /* Equivalent to py={2} */
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