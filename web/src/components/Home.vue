<template lang="">
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
            {{ selectedFile.name | truncate(20)}}
        </v-text>

        <!-- Create a File Input that will be hidden but triggered with JavaScript -->
        <input 
            ref="uploader" 
            class="d-none" 
            type="file" 
            @change="onFileChanged"
        >
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'Home',
    data(){
        return {
            isSelecting: false,
            selectedFile: null
        }
    },
    methods: {
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
            // Do whatever you need with the file, liek reading it with FileReader
        },
    }
})
</script>

<style lang="">

</style>