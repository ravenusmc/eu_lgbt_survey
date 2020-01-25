<template>
  <div>
    <vue-chart
    chart-type="GeoChart"
    :columns="columns"
    :rows="rows"
    :options="options"></vue-chart>
  </div>
</template>

<script>
export default {
  name: 'Map',
  data() {
    return {
      columns: [{
        'type': 'string',
        'label': 'Country',
      }, {
        'type': 'number',
        'label': 'Suicides',
      }],
      rows: [['Country', 'Popularity'],
        ['Germany', 200],
        ['United States', 300],
        ['Brazil', 400],
        ['Canada', 500],
        ['France', 600],
        ['RU', 700]],
      options: {
        title: 'Suicide by Countries',
        width: 900,
        height: 500,
      },
    };
  },
};
</script>

<style scoped>
</style>
