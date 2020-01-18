<template>
  <div class="home">
    <Intro />
    <SectionOne/>
    <Study/>
  </div>
</template>

<script>
// @ is an alias to /src
import Intro from '@/components/Intro.vue';
import SectionOne from '@/components/SectionOne.vue';
import Study from '@/components/Study.vue';


export default {
  name: 'home',
  components: {
    SectionOne,
    Intro,
    Study,
  },
};
</script>

<style>

.font {
  font-family: 'Baskervville', serif;
}

button {
  background-color: #F48C34;
  border-radius: 6px;
  padding: 12px;
  border-color: #F48C34;
}

button:hover {
  background-color: #00AFC9;
  border-color:  #00AFC9;
}

</style>
