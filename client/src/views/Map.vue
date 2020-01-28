<template>
  <div>
    <EuropeMap/>
    <Footer/>
  </div>
</template>

<script>
import EuropeMap from '@/components/charts/Map.vue';
import Footer from '@/components/generic/Footer.vue';

export default {
  name: 'Map',
  components: {
    EuropeMap,
    Footer,
  },
};
</script>

<style scoped>
</style>
