<template>
    <button :disabled="disabled" @click="onclick">
        <slot></slot>
    </button>
</template>

<script>
export default {
    name: 'Button',
    props: {
        onclick: {
            type: Function
        },
        disabled: {
            type: Boolean
        }
    }
}
</script>

<style scoped>
button {
    margin-top: 5px;
    margin-bottom: 5px;
    background: transparent;
    border: none;
    font-size: 30px;
    color: white;
    transition: .3s;
}

button:active {
    transform: scale(.95);
}

button:hover {
    cursor: pointer;
}

button:disabled {
    opacity: .3;
}
</style>