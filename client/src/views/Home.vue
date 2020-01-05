<template>
  <div class="home">
    <SectionOne/>
  </div>
</template>

<script>
// @ is an alias to /src
import SectionOne from '@/components/SectionOne.vue';

export default {
  name: 'home',
  components: {
    SectionOne,
  },
};
</script>
