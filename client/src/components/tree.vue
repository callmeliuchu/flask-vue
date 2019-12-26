<template>
    <div class="tree-menu">
        <ul v-for="item in data">
            <c-tree-item :data="item" :custom_method="custom_method"></c-tree-item>
        </ul>
    </div>
</template>

<script>


import cTreeItem from './tree-item'
export default {
    props: {
        data: {
            type: [Object, Array],
            required: true
        },
        custom_method:{
            type: [Function],
            required: false
        }
    },
    components: {
        cTreeItem
    }
}
</script>
