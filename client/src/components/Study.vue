<template>
  <div>
    <div id='studyTitleArea'>
      <h1 class='font center'>Results For: State: {{ state }}, Orientation: {{ orientation }}</h1>
    </div>
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
      <GraphCard
      :typeOne='typeOne'
      :data='questionFourData'
      :options='chartOptionsFour'>
      </GraphCard>
      <GraphCard
      :typeOne='typeOne'
      :data='questionFiveData'
      :options='chartOptionsFive'>
      </GraphCard>
      <div id='picDiv'>
      </div>
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
  props: ['state', 'orientation'],
  data() {
    return {
      typeOne: 'BarChart',
      chartOptionsOne: {
        title: 'In your opinion, how widespread is offensive language about lesbian, gay, bisexual and/or transgender people by politicians in the country where you live?',
        legend: { position: 'top' },
        height: 500,
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
      chartOptionsTwo: {
        title: 'In your opinion, how widespread is same-sex partners holding hands in public in the country where you live?',
        legend: { position: 'top' },
        height: 500,
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
      chartOptionsThree: {
        title: 'In your opinion, how widespread are expressions of hatred and aversion towards lesbian, gay, bisexual and/or transgender in public in the country where you live?',
        legend: { position: 'top' },
        height: 500,
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
      chartOptionsFour: {
        title: 'In your opinion, how widespread are assaults and harassment against lesbian, gay, bisexual and/or transgender people in the country where you live?',
        legend: { position: 'top' },
        height: 500,
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
      chartOptionsFive: {
        title: 'In your opinion, how widespread is same-sex partners holding hands in public in the country where you live?',
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
      'questionFourData',
      'questionFiveData',
    ]),
  },
};
</script>

<style>
#studyTitleArea {
  margin-top: 25px;
  margin-bottom: 25px;
  text-transform: uppercase;
  font-size: 30px;
}

section {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

#picDiv {
  background-image: url('../assets/img/bar_chart.jpg');
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
  height: 500px;
  border-radius: 10px;
}

/* Media Queries */
@media only all and (max-width: 900px){

  section {
    grid-template-columns: 1fr;
  }

  GraphCard {
    margin-left: 3%;
    margin-right: 3%;
  }

}
</style>
