<template>
  <div class="home">
    <Intro />
    <section id='formSection'>
      <SectionOne/>
      <Questions/>
    </section>
    <Study/>
    <hr>
    <Map/>
    <Footer/>
  </div>
</template>

<script>
// @ is an alias to /src
import Intro from '@/components/Intro.vue';
import SectionOne from '@/components/SectionOne.vue';
import Questions from '@/components/Questions.vue';
import Study from '@/components/Study.vue';
import Map from '@/components/charts/Map.vue';
import Footer from '@/components/generic/Footer.vue';


export default {
  name: 'home',
  components: {
    SectionOne,
    Questions,
    Intro,
    Study,
    Map,
    Footer,
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
