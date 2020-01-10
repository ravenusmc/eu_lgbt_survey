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
