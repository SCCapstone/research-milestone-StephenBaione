<template>
  <v-app id="inspire">
    <v-app-bar
      app
      shrink-on-scroll
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Application</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>

    <section class="watchlist">
      <h1>My Watchlist:</h1>
      <watch-list></watch-list>
    </section>

    <section class="assets">
      <h1>All of Our Assets:</h1>
      <asset-display-layout :assetDisplays="this.assetDisplays"></asset-display-layout>
    </section>
  </v-app>
</template>

<script>
  import HelloWorld from '../components/HelloWorld'
  import WatchList from '../components/WatchList.vue';
  import AssetDisplay from '../components/AssetDisplay.vue';
  import AssetDisplayLayout from '../components/AssetDisplayLayout.vue';

  export default {
    name: 'Home',

    components: {
      HelloWorld,
      AssetDisplay,
      AssetDisplayLayout,
      WatchList
    },
    data() {
      return {
        'assetDisplays': [
          { "name": 'Ethereum', "marketPrice": 47.65, 'averageTransactionFee': 3, 'marketPriceUsd': 3, 'marketCapUsd': 3, 'inflationUsd': 0.2258},
          { "name": 'Bitcoin', "marketPrice": 47.65, 'averageTransactionFee': 3, 'marketPriceUsd': 3, 'marketCapUsd': 3, 'inflationUsd': -0.2258},
          { "name": 'Tether', "marketPrice": 47.65, 'averageTransactionFee': 3, 'marketPriceUsd': 3, 'marketCapUsd': 3, 'inflationUsd': 0.2258},
          { "name": 'Binance', "marketPrice": 47.65, 'averageTransactionFee': 3, 'marketPriceUsd': 3, 'marketCapUsd': 3, 'inflationUsd': -0.2258},
          { "name": 'Dogecoin', "marketPrice": 47.65, 'averageTransactionFee': 3, 'marketPriceUsd': 3, 'marketCapUsd': 3, 'inflationUsd': 0.2258},
          { "name": 'USD-Coin', "marketPrice": 47.65, 'averageTransactionFee': 3, 'marketPriceUsd': 3, 'marketCapUsd': 3, 'inflationUsd': -0.2258}
        ]
      }
    },
  }
</script>
