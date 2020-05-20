<template>
  <div id="app">
    <aside>
      <div class="button-container">
        <Button
          :onclick="connect"
          :disabled="Boolean(config)"
        >
          Connect
        </Button>
        <div class="seperator"></div>
        <Button
          :onclick="getConfig"
          :disabled="!Boolean(config)"
        >
          Get Config
        </Button>
        <Button
          :onclick="editConfig"
          :disabled="!Boolean(config) || !changed"
        >
          Edit Config
        </Button>
        <div class="seperator"></div>
        <Button
          :onclick="closeSession"
          :disabled="!Boolean(config)"
        >
          Close Session
        </Button>
      </div>
    </aside>
    <article>
      <Message ref="message" />
      <prism-editor
        @change="handleOnChange"
        ref="editor"
        v-if="config"
        v-model="config"
        language="xml"
        class="my-editor"
      />
      <div
        v-if="!config"
        class="error"
      >
        <div>
          Session is temporarily closed
        </div>
      </div>
    </article>
    
  </div>
</template>

<script>
import "prismjs";
import "prismjs/themes/prism-tomorrow.css";
import "vue-prism-editor/dist/VuePrismEditor.css";

import Button from "./components/Button";
import Message from './components/Message';
import Axios from 'axios'
import PrismEditor from "vue-prism-editor";
import X2JS from 'x2js';

export default {
  name: "App",
  data() {
    return {
      config : null,
      changed: false
    };
  },
  methods: {
    handleOnChange: function() {
      this.changed = true
    },  
    connect: function() {
      Axios.get(`http://localhost:5000/connect`)
        .then(response => {
          this.config = response.data
        })
        .catch(() => this.$refs.message.fire('Error'))
    },
    editConfig: function() {
      const x2js = new X2JS()
      const json = x2js.xml2js(this.config)
      Axios.post(`http://localhost:5000/config`, {
        data: x2js.js2xml(json['rpc-reply']['data'])
      }, {
        'Content-Type': 'application/json',
      })
        .then(response => {
          this.config = response.data
          this.changed = false
        })
        .catch(() => this.$refs.message.fire('Error'))
    },
    getConfig: function() {
      Axios.get(`http://localhost:5000/config`)
        .then(response => {
          this.config = response.data
        })
        .catch(() => this.$refs.message.fire('Error'))
    },
    closeSession: function() {
      Axios.get(`http://localhost:5000/close`)
        .then(() => {
          this.config = null
        })
        .catch(() => this.$refs.message.fire('Error'))
    },
  },
  mounted() {
    this.getConfig()
  },
  components: {
    Button,
    Message,
    PrismEditor
  }
};
</script>

<style>

html, body {
  height: 100%;
  margin: 0px;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app {
  display: flex;
  height: 100%;
  width: 100%;
  overflow: hidden;
}

aside {
  width: 40%;
  height: 100%;
  background: purple;
  display: flex;
}

article {
  width: 60%;
  height: 100%;
  box-sizing: border-box;
}

.button-container {
  display: flex;
  flex-direction: column;
  margin: auto;
  margin-right: 30px;
}

.error {
  display: flex;
  height: 100%;
}

.error > div {
  margin: auto;
  font-size: 30px;
  color: purple
}

.seperator {
  margin-top: 10px;
  margin-bottom: 10px;
  height: 1px !important;
  background: white;
  height: 40%;
}

</style>
