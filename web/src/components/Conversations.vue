<template>
  <div style="width: 100%">
    <side-drawer :user="user" @click-user="moveToConversation($event)">
    </side-drawer>

    <v-container class="content-box justify-space-between">
      <conversation-list
        :conversations="conversations"
        :selectedConversation="selectedConversation"
        :user="user"
        @conversation-clicked="selectedConversation = $event"
      >
      </conversation-list>

      <chat-box
        :selectedConversation="selectedConversation"
        :user="user"
        @message-sent="getConversations"
      >
      </chat-box>
    </v-container>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import SideDrawer from "@/components/chat/SideDrawer.vue";
import ConversationList from "@/components/chat/ConversationList.vue";
import ChatBox from "@/components/chat/ChatBox.vue";

export default {
  name: "conversations",

  components: {
    SideDrawer,
    ConversationList,
    ChatBox,
  },

  created() {
    this.user = JSON.parse(localStorage.getItem("user"));
    this.getConversations();
  },

  data() {
    return {
      conversations: [],
      selectedConversation: null,
      user: null,
    };
  },

  methods: {
    getConversations() {
      axios
        .get(`/api/conversations?user_id=${this.user.id}`)
        .then((response) => {
          this.conversations = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    async moveToConversation(user) {
      // console.log(user)
      let conversations = await this.getConversation([this.user.id, user.id]);
      // console.log(conversations)
      if (conversations.length > 0) {
        // console.log("exist")
        this.selectedConversation = conversations[0];
      } else {
        await axios
          .post("/api/conversations", {
            created_by: this.user.id,
            modified_by: this.user.id,
            type: "Normal",
            members: [this.user.id, user.id],
          })
          .then((response) => {
            this.getConversations();
            this.selectedConversation = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },

    async getConversation(users) {
      let conversation = null;
      console.log(users);
      await axios
        .get(
          `/api/conversations?user_id=${this.user.id}&members=${users[0]}&members=${users[1]}`
        )
        .then((response) => {
          conversation = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      return conversation;
    },
  },
};
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
