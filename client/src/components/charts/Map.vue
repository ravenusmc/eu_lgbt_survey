<template>
  <div>
    <header>
      <div>
        <h1 class='mapTitle font center'>Map Page</h1>
      </div>
    </header>
    <MapInfo/>
    <MapForm/>
    <section id='map_section'>
      <vue-chart id='map_section'
      chart-type="GeoChart"
      :columns="columns"
      :rows='mapData'
      :options="options">
      </vue-chart>
    </section>
    <Background/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import MapInfo from '@/components/mapPage/Info.vue';
import MapForm from '@/components/forms/MapForm.vue';
import Background from '@/components/mapPage/Background.vue';

export default {
  name: 'EuropeMap',
  components: {
    MapForm,
    Background,
    MapInfo,
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

header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-image: url('../../assets/img/europeMap.jpg');
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
  height: 600px;
}

header div {
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  padding: 20px;
  border-radius: 12px;
}

.mapTitle {
  font-size: 40px;
  text-transform: uppercase;
}

#map_section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 25px;
  margin-bottom: 25px;
}
</style>
