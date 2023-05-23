<template>
    <v-text class="title">
      Nguyen Van A
    </v-text>

    <v-container class="message-box">
      <messages style="height:85%"></messages>
      <v-form class="send-message-form" @submit.prevent >
        <v-text-field required placeholder="Enter your message" class='send-message-box' ></v-text-field>
      </v-form>
    </v-container>
</template>

<script>
import Messages from '@/components/chat/Messages.vue';

export default {
  name: 'single-chat',

  components: {
    Messages,
  },

  data() {
    return {

    }
  },    
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