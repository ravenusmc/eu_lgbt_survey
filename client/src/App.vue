<template>
  <div id="app">
    <Header/>
    <router-view/>
  </div>
</template>

<script>
import Header from '@/components/generic/Header.vue';

export default {
  components: {
    Header,
  },
};
</script>

<style>
body {
  margin-left: 5%;
  margin-right: 5%;
}
</style>
