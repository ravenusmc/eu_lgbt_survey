<template>
  <div>
    <section>
      <div id='picDiv'>
      </div>
      <div id='paragraphDiv'>
        <h1 class='center title'>The Study</h1>
        <p>
          In the summer of 2019, I was on Kaggle, like I am a lot, and found this
          dataset. It interested me but at the time I wanted to work on another
          project. I then have to admit that I kind of forgot about the dataset. Later
          in the summer I came back to Kaggle and found the dataset again. I still
          was working on another project but decided to download the data so that
          I would have it.
        </p>
        <p>
          I finally have decided to work on this issue and I'm interested in what
          the data will show me in regards to LGBT rights in Europe. I have this
          project broken up by 6 questions that I found interesting from the survey.
          You are able to select a specific country or type of orientation and see how
          the data breaks out. The options returned, for each question are the following:
          'Very widespread', 'Fairly widespread', 'Fairly rare', 'Very rare', and
           'Don`t know'. Each question will have a graph and then a little bit about the
           response of the data.
        </p>
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

.title {
  font-family: 'Baskervville', serif;
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

#paragraphDiv {
  margin-right: 5%;
  font-size: 20px;
  font-family: 'Baskervville', serif;
}

</style>
