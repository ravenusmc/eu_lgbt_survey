<template>
  <div>
    <header>
      <div id="nav">
        <router-link to="/">Home</router-link> |
        <router-link to="/about">About</router-link>
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
}

</style>
