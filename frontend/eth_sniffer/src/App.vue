<template>
  <v-app>
    <v-app-bar
      app
      color="#36174D"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Snifter Logo"
          class="shrink mr-2"
          contain
          src="./assets/logo.svg"
          transition="scale-transition"
          width="40"
          color="white"
        />


        <h1>Snifter</h1>
      </div>

      <v-spacer></v-spacer>

      <h1>NFT Search</h1>
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
