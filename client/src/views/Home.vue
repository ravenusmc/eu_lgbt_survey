<template>
  <div class="home">
    <Intro />
    <section id='formSection'>
      <SectionOne v-on:changeTitle="updateTitle($event)"/>
      <Questions/>
    </section>
    <Study :state='state' :orientation='orientation'/>
    <hr>
    <Footer/>
  </div>
</template>

<script>
// @ is an alias to /src
import Intro from '@/components/Intro.vue';
import SectionOne from '@/components/SectionOne.vue';
import Questions from '@/components/Questions.vue';
import Study from '@/components/Study.vue';
import Footer from '@/components/generic/Footer.vue';


export default {
  name: 'home',
  components: {
    SectionOne,
    Questions,
    Intro,
    Study,
    Footer,
  },
  data() {
    return {
      state: 'Austria',
      orientation: 'Lesbian',
    };
  },
  methods: {
    updateTitle(data) {
      // console.log(data.payload.state);
      this.state = data.payload.state;
      this.orientation = data.payload.orientation;
      console.log(this.state);
    },
  },
};
</script>

<style>

.center {
  text-align: center;
}

.font {
  font-family: 'Baskervville', serif;
}

button {
  background-color: #F48C34;
  border-radius: 6px;
  padding: 12px;
  border-color: #333;
}

button:hover {
  background-color: #00AFC9;
  border-color: #333;
}

#formSection {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

/* Media Queries */
@media only all and (max-width: 900px){

  #formSection {
    grid-template-columns: 1fr;
  }

}

</style>
