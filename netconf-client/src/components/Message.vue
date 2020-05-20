<template>
    <div class="message" v-if="Boolean(message)">
        <div>
            {{message}}
        </div>
        <img @click="close" src="../assets/close.svg" />
    </div>
</template>

<script>
export default {
    data: function() {
        return {
            message: null,
        }
    },
    methods: {
        close: function() {
            this.message = null
        },
        fire: function(message) {
            this.message = message
        }
    }
}
</script>

<style scope>
.message {
    position: fixed;
    top: 0px;
    right: 0px;
    margin: 20px;
    width: 300px;
    background: purple;
    color: white;
    padding: 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.message img {
    filter: brightness(0) invert(1);
}

.message img:hover {
    cursor: pointer;
}
</style>