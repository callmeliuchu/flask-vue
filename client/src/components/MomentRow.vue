<template>
  <tbody>
    <tr  v-for="moment in moments">
      <td v-for="column in columns">{{ moment[column] }}</td>
    </tr>
  </tbody>
</template>


<script>
 export default {
   props:['moments','columns']
 }

</script>
