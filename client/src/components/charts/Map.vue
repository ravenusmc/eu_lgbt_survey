<template>
  <div>
    <MapForm/>
    <h1 class='font center'>Map Area</h1>
    <section id='map_section'>
      <vue-chart
      chart-type="GeoChart"
      :columns="columns"
      :rows="rows"
      :options="options">
      </vue-chart>
    </section>
  </div>
</template>

<script>
import MapForm from '@/components/forms/MapForm.vue';

export default {
  name: 'EuropeMap',
  components: {
    MapForm,
  },
  data() {
    return {
      columns: [{
        type: 'string',
        label: 'Country',
      }, {
        type: 'number',
        label: 'Popularity',
      }],
      rows: [['Germany', 200],
        ['France', 600]],
      options: {
        region: '150', // Africa
        title: 'Suicide by Countries',
        width: 900,
        height: 500,
      },
    };
  },
};
</script>

<style scoped>
#map_section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
