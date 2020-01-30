<template>
  <div>
    <section>
      <div id='poetryDiv'>
        <p>
          Thank God for boys,<br>
          Thank God for girls,<br>
          Thank God for humans<br>
          In this world<br>
        </p>
        <p>
          Boys can like pink<br>
          Girls can wear blue<br>
          Your reaction<br>
          Is up to you<br>
        </p>
        <p>
          When someone's proud,<br>
          Let them be them,.<br>
          Let boys be girls,<br>
          Let girls be men.<br>
        </p>
        <p>
          Don't hate because they're different<br>
          As that's still up to you<br>
          In fact, you should be proud of them,<br>
          for they came out to you.<br>
        </p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Background',
};
</script>

<style scoped>
section {
  margin-left: 5%;
  margin-right: 5%;
  margin-bottom: 25px;
  background-image: url('../../assets/img/kissing.jpg');
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
  height: 600px;
  border-radius: 10px;
}

#poetryDiv {
  text-align: center;
  font-family: 'Indie Flower', cursive;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 25px;
  width: 50%;
  height: 88%;
  top: 4%;
  left: 10%;
  color: white;
  background-color: rgba(0, 0, 0, 0.5);
  margin-left: 50px;
}
</style>
