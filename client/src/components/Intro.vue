<template>
  <div>
    <section>
      <div id='picDiv'>
      </div>
      <div>
        <h1 class='center'>The Study</h1>
        <p></p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Intro',
};
</script>

<style scoped>

.center {
  text-align: center;
  text-transform: uppercase;
}

section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 1em;
  margin-top: 5%;
  margin-bottom: 3%;
}

#picDiv {
  margin-left: 5%;
  margin-right: 5%;
  background-image: url('../assets/img/picOne.jpg');
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
  height: 600px;
}

</style>
