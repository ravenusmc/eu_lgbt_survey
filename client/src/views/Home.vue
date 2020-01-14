<template>
  <div class="home">
    <Intro />
    <SectionOne/>
  </div>
</template>

<script>
// @ is an alias to /src
import Intro from '@/components/Intro.vue';
import SectionOne from '@/components/SectionOne.vue';


export default {
  name: 'home',
  components: {
    SectionOne,
    Intro,
  },
};
</script>

<style>

.font {
  font-family: 'Baskervville', serif;
}

button {
  background-color: #349CF4;
  border-radius: 6px;
  padding: 12px;
  border-color: #349CF4;
}

button:hover {
  background-color: #F48C34;
  border-color:  #F48C34;
}
</style>
