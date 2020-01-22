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
      :data='questionTwoData'
      :options='chartOptionsTwo'>
      </GraphCard>
      <GraphCard
      :typeOne='typeOne'
      :data='questionThreeData'
      :options='chartOptionsThree'>
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
      chartOptionsTwo: {
        title: 'Question 2',
        legend: { position: 'top' },
        height: 500,
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
      chartOptionsThree: {
        title: 'Question 3',
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
      'questionTwoData',
      'questionThreeData',
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
