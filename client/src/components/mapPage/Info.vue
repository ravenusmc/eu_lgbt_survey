<template>
  <div>
    <section class='infoSection'>
      <div class='pictureDiv'>
      </div>
      <div>
        <h1 class='title center font'>How this Page Works</h1>
        <div class='paragraphDiv'>
          <p class='font'>
            The purpose of this page is to show how each country stacks up compared
            to other countries in Europe. A user selects a question to be examined
            from the form below. They then select an answer such as 'very widespread'
            and finally the sex-gay, lesbian, bi or transgender. Once that is done,
            the user hits submit and the data appears!
          </p>
          <br>
          <p class='font'>
            Once the data comes back, the countries are color coded a shade of green.
            The darker the green is the higher the percentage. Thus, is the question
            was along the lines of looking at assualts in a country and the answer
            was vry widespread your seeing the amount of people that thought that
            assaults were widespread in their country.
          </p>
          <br>
          <p class='font'>
            I also wanted to add some of my own views here. It's quite apparent to
            me that countries in Western Europe are much more tolerant of LGBT people
            than countries in Southern/Eastern Europe. In many cases, states that were
            part of the Soviet Union almost always have a low appeal of LGBT rights.
            In Southern Europe, such as Italy, I'd argue that it has to do with the
            Catholic church and possibly other socio/economic factors such as Southern
            Europe not being as rich as North/West Europe.
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'MapInfo',
};
</script>

<style scoped>

.pictureDiv {
  background-image: url('../../assets/img/loveWall.jpg');
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
  height: 600px;
  border-radius: 10px;
}

.infoSection {
  margin-top: 15px;
  margin-bottom: 15px;
}

.title {
  margin-top: 25px;
  font-size: 30px;
  text-transform: uppercase;
}

.paragraphDiv {
  margin-left: 3%;
  margin-right: 3%;
}
</style>
