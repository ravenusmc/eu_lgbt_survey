<template>
  <div>
    <h1 class='font center'>Map Area</h1>
    <MapForm/>
    <section id='map_section'>
      <vue-chart id='map_section'
      chart-type="GeoChart"
      :columns="columns"
      :rows='mapData'
      :options="options">
      </vue-chart>
    </section>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
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
        label: 'Percentage',
      }],
      rows: [['Germany', 200],
        ['France', 600]],
      options: {
        region: '150', // Europe Code
        title: 'Suicide by Countries',
        width: 900,
        height: 500,
      },
    };
  },
  computed: {
    ...mapGetters([
      'mapData',
    ]),
  },
};
</script>

<style scoped>
#map_section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 25px;
  margin-bottom: 25px;
}
</style>
