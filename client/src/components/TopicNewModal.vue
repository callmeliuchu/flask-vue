<template>
  <div>
    <b-button    id="show-btn"  pill variant="outline-secondary" @click="showModal">新建话题</b-button>

    <b-modal ref="my-modal"  hide-footer title="Using Component Methods">
      <div>
            <b-form-select
            v-model="selected"
            :options="ops"
            class="mb-3"
            value-field="item"
            text-field="name"
            disabled-field="notEnabled"
             ></b-form-select>
      </div>
      <b-button  class="float-right"  id="show-btn"  pill variant="outline-secondary" @click="hideModal">取消</b-button>
      <b-button  class="float-right"  id="show-btn"  pill variant="outline-secondary" @click="toggleModal">新建</b-button>
    </b-modal>
  </div>
</template>

<script>
  export default {
    props:['ops','selected'],
    data(){
      return {
      }
    },
    methods: {
      showModal() {
        this.$refs['my-modal'].show()
      },
      hideModal() {
        this.$refs['my-modal'].hide()
      },
      toggleModal() {
        // alert(this.selected)
        let topic_data = {}
        for(let d of this.ops){
          if(d['item'] == this.selected){
            topic_data['id'] = d['item'];
            topic_data['name'] = d['name'];
          }
        }
        this.$router.push({name:'TopicNew',params:{topic_data:topic_data}})
        this.$refs['my-modal'].toggle('#toggle-btn')
      }
    }
  }
</script>
