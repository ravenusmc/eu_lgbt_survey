<template>
  <div>
    <section>
      <GraphCard
      :typeOne='typeOne'
      :data='questionOneData'
      :options='chartOptionsOne'>
      </GraphCard>
      <GraphCard
      :typeOne='typeOne'
      :data='questionOneData'
      :options='chartOptionsOne'>
      </GraphCard>
    </section>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import GraphCard from '@/components/charts/GraphCard.vue';

export default {
  name: 'Study',
  components: {
    GraphCard,
  },
  data() {
    return {
      typeOne: 'BarChart',
      chartOptionsOne: {
        title: 'Question 1',
        legend: { position: 'top' },
        height: 500,
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
    };
  },
  computed: {
    ...mapGetters([
      'questionOneData',
    ]),
  },
};
</script>

<style>
section {
  display: grid;
  grid-template-columns: 1fr 1fr;
}
</style>
