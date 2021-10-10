<template>
  <v-app id="inspire">
    <v-container>
      <section class="search-result">
        <nft-search ref="nftSearch" @getAsset="newAsset($event)"></nft-search>
      </section>

      <section class="watchlist">
        <h1>Search Result:</h1>
        <nft-display v-if="nft" :nft="nft"></nft-display>
        <watch-list></watch-list>
      </section>

      <section class="assets">
        <h1>All of Our Assets:</h1>
        <asset-display-layout :assetDisplays="this.assetDisplays"></asset-display-layout>
      </section>
    </v-container>
  </v-app>
</template>

<script>
  import HelloWorld from '../components/HelloWorld'
  import WatchList from '../components/WatchList.vue';
  import AssetDisplay from '../components/AssetDisplay.vue';
  import AssetDisplayLayout from '../components/AssetDisplayLayout.vue';
  import NftSearch from '../components/NftSearch.vue';
  import NftDisplay from '../components/NftDisplay.vue';

  export default {
    name: 'Home',

    components: {
      HelloWorld,
      AssetDisplay,
      AssetDisplayLayout,
      WatchList,
      NftSearch,
      NftDisplay
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
        ],
        'nft': null
        }
      },
    methods: {
      newAsset (nft_data) {
        this.nft = nft_data["data"];
      }
    },
  }
</script>
