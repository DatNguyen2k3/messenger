<template>
    <div style="width: 100%">
      <side-drawer>

      </side-drawer>    
      <v-container class="content-box justify-space-between">
        <conversation-list></conversation-list>
        <chat-box></chat-box>
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
  
  data() {
    return {
      isSearch: true,
    }
  },



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