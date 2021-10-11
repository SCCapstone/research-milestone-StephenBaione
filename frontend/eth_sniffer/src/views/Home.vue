<template>
  <v-app id="inspire">
    <v-container>
      <section class="search-result">
        <nft-search ref="nftSearch" @getAsset="newAsset($event)"></nft-search>
      </section>

      <section class="watchlist" v-if="nft">
        <nft-display :nft="nft"></nft-display>
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
  import NftTokenInfo from '../components/NftTokenInfo.vue';

  export default {
    name: 'Home',

    components: {
      HelloWorld,
      AssetDisplay,
      AssetDisplayLayout,
      WatchList,
      NftSearch,
      NftDisplay,
      NftTokenInfo
    },
    data() {
      return {
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
