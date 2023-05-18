<template>
  <v-container class="container">
    
    <v-card class="title-box" align="center" justify="center">
      <v-text class="title-text">
        Messenger
      </v-text>
    </v-card>

    <v-card
      class="mx-auto auth-box"
      elevation="1"
      max-width="100%"
    >
      <v-tabs isFitted v-model="tab" variant="soft-rounded">
        
        <v-tab value="sign_in" class="auth-button">Sign in</v-tab>
        <v-tab value="sign_up" class="auth-button">Sign up</v-tab>

      </v-tabs>

      <v-card>
        <v-window v-model="tab">
          <v-window-item value="sign_in">
            <v-form @submit.prevent ref="loginForm">
              <v-card-text>
                <div class="text-subtitle-2 font-weight-black mb-1"  >Username</div>

                <v-text-field
                  label="Enter username here"
                  single-line
                  variant="outlined"
                  v-model="signInForm.username"
                ></v-text-field>

                <v-btn
                  :disabled="loading"
                  :loading="loading"
                  block
                  type="submit"
                  class="text-none mb-4 "
                  size="x-large"
                  variant="flat"
                  style="background-color: #1A237E; color: white; border-radius: 12px; margin-top: 1em;"
                  @click="login"
                >
                  Login
                </v-btn>
              </v-card-text>
            </v-form>
          </v-window-item>

          <v-window-item value="sign_up">
            <v-form @submit.prevent>
              <v-card-text>
                <div class="text-subtitle-2 font-weight-black mb-1">Username</div>

                <v-text-field
                  label="Enter username here"
                  single-line
                  variant="outlined"
                  v-model="signUpForm.username"
                ></v-text-field>

                <div class="text-subtitle-2 font-weight-black mb-1">Email</div>

                <v-text-field
                  label="Enter email here"
                  single-line
                  variant="outlined"
                  v-model="signUpForm.email"
                ></v-text-field>

                                <div>
                    <!-- 1. Create the button that will be clicked to select a file -->
                  <v-btn 
                    color="primary" 
                    rounded 
                    dark 
                    :loading="isSelecting" 
                    @click="handleFileImport"
                  >
                    Upload File
                  </v-btn>

                  <v-text v-if="selectedFile">
                      {{ selectedFile.name }} 
                  </v-text>

                    <!-- Create a File Input that will be hidden but triggered with JavaScript -->
                  <input 
                      ref="uploader" 
                      class="d-none" 
                      type="file" 
                      @change="onFileChanged"
                  >
                </div>

                <v-btn
                  :disabled="loading"
                  :loading="loading"
                  block
                  type="submit"
                  class="text-none mb-4 "
                  size="x-large"
                  variant="flat"
                  style="background-color: #1A237E; color: white; border-radius: 12px; margin-top: 1em;"
                  @click="register"
                >
                  Register
                </v-btn>


              </v-card-text>  
            </v-form>        
          </v-window-item>

        </v-window>
      </v-card>



      
    </v-card>

  </v-container>

</template>

<script>
import logo from '../assets/logo.svg'

export default {
  name: 'login',

  data: () => ({
    tab: null,
    signUpForm: {
      username: '',
      email: '',
      avatar_img: '',
    },
    signInForm: {
      username: '',
    },

    isSelecting: false,
    selectedFile: null,



  }),

  
  methods: {
    login() {
      let username = this.signInForm.username
      console.log(username)
    },

    register() {
      let username = this.signUpForm.username
      let email = this.signUpForm.email
      console.log(username, email)
    },

    handleFileImport() {
      this.isSelecting = true;
      // After obtaining the focus when closing the FilePicker, return the button state to normal
      window.addEventListener('focus', () => {
          this.isSelecting = false
      }, { once: true });
      
      // Trigger click on the FileInput
      this.$refs.uploader.click();
    },

    onFileChanged(e) {
      this.selectedFile = e.target.files[0];
      signUpForm.avatar_img = this.selectedFile
      // Do whatever you need with the file, liek reading it with FileReader
    },
  },
}
</script>

<style>

.container {
  max-width: 40%;
  min-width: 300px;
}

.title-box {
  display: flex;
  justify-content: center;
  padding: 12px;
  background-color: white;
  width: 100%;
  margin: 40px 0 15px 0;
  border-radius: 12px;
  border-width: 1px;
}

.title-text {
  font-size: 2rem;
  font-family: 'Work Sans', sans-serif;
}

.auth-box {
  background-color: white;
  width: 100%;
  padding: 16px;
  border-radius: 12px;
  border-width: 1px;
}

.tabs {
  width: 100%;
  height: 100%;
  border-radius: 12px;
}

.choice-button {
  margin-bottom: 1em;
}

.auth-button {
  font-size: 1.5rem;
  font-family: 'Work Sans', sans-serif;
  width: 50%;
}

</style>
