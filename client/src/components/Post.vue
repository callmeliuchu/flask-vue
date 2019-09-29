<template>
      <b-card v-bind:class="[post_style]">
         <b-row>
           <b-col>
             {{ post_data.title }}
           </b-col>
         </b-row>
         <b-row>
           <b-col>
             {{ post_data.content  }}
           </b-col>
         </b-row>
         <b-row>
           <b-col>
             {{ post_data.date_created }}
           </b-col>
         </b-row>
      </b-card>
</template>


<script>
  export default {
    data(){
      return  {
        post_style : ''
      }
    },
    props:['post_data'],
    created(){
      console.log(JSON.stringify(this.post_data))
      this.post_style = `box_${this.post_data.type}`
    }
  }
</script>


<style>
  .box_1 {
    background: #00FF00	;
  }
  .box_2 {
    background: #00449e	;
  }
  .box_3 {
    background: #ffff00	;
  }
  .box_4 {
    background: #50e3c2	;
  }
  .box_5 {
    background: #81b10c	;
  }
  .box_6 {
    background: #ff725c	;
  }
  .box_7 {
    background: #61affe	;
  }
  .box_8 {
    background: #D3E7E9	;
  }
  .box_9 {
    background: #ffff00	;
  }
  .box_10 {
    background: #A5D6D9	;
  }
</style>
