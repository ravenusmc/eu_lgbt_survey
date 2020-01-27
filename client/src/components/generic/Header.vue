<template>
  <div>
    <header>
      <div id="nav">
        <router-link class='router_text' to="/">EU LGBT SURVEY</router-link> |
        <router-link class='router_text' to="/map">MAP PAGE</router-link> |
        <router-link class='router_text' to="/about">ABOUT</router-link>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style scoped>

Header {
  background: #00AFC9;
  height: 80px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

#nav {
  margin-left: 3%;
  color: white;
}

.router_text {
  color: white;
  text-decoration: none;
  font-size: 20px;
}

.router_text:hover {
  color: yellow;
}

</style>
