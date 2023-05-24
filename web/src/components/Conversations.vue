<template>
    <div style="width: 100%">
      <side-drawer
        :user="user"
      >
      </side-drawer>  

      <v-container class="content-box justify-space-between">
        <conversation-list
          :conversations="conversations"
          :selectedConversation="selectedConversation"
          :user="user"
        >
        </conversation-list>
        
        <chat-box
          :selectedConversation="selectedConversation"
          :user="user"
        >

        </chat-box>
      </v-container>
    </div>
</template>

<script>

import { useRouter } from 'vue-router';
import SideDrawer from '@/components/chat/SideDrawer.vue';
import ConversationList from '@/components/chat/ConversationList.vue';
import ChatBox from '@/components/chat/ChatBox.vue';

export default {
  name: 'conversations',

  components: {
    SideDrawer,
    ConversationList,
    ChatBox,
  },
  
  created() {
    this.user = JSON.parse(localStorage.getItem('user'));
    this.getConversations();
  },

  data() {
    return {
      conversations: [],
      selectedConversation: null,
      user: null,
    }
  },

  methods: {
    getConversations() {
      axios.get(`/api/conversations?user_id=${this.user.id}`)
        .then(response => {
          this.conversations = response.data;
          if (this.conversations.length > 0) {
            this.selectedConversation = this.conversations[0];
          }
        })
        .catch(error => {
          console.log(error);
        });
    },


  }



}



</script>



<style scoped>  

.content-box {
  display: flex;
  width: 100%;
  height: 91.5vh;
  padding: 10px;
  max-width: 98%;
}


</style>