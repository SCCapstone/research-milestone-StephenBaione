<template>
    <v-container v-if="nft" class="nft">
        <v-card class="nft__card">
            <div class="card-content-wrapper">
                <div class="nft__header">
                    <div>
                        <v-card-title color="white" class="title">{{ nft.name }}</v-card-title>
                    </div>
                    <div>
                        <v-card-subtitle color="white" class="title">{{ nft.collection.name }}</v-card-subtitle>
                    </div>
                </div>
                <div class="nft__top-level">
                    <div class="nft__logo text-center">
                        <img :src="nft.image_url"/>
                    </div>
                    <div class="nft__description">
                        <h2>Collection Details</h2>
                        <img :src="nft.collection.large_image_url" alt="">
                        <p>Collection: {{ nft.collection.name }} ({{nft.asset_contract.symbol}})</p>
                        <p>
                            <v-icon color="white" large>mdi-discord</v-icon>
                            <a :href="nft.collection.discord_url">Discord Server</a>
                        </p>
                        <p>
                            <v-icon color="white" large>mdi-web</v-icon>
                            <a :href="nft.collection.external_url">Site</a>
                        </p>
                        <p>
                            <v-icon color="white" large>mdi-twitter</v-icon>
                            Twitter Username: {{ nft.collection.twitter_username }}
                        </p>
                        <div class="nft__link text-center">
                            <v-icon color="white" large>mdi-brush</v-icon>
                            <a :href="nft.external_link"> Go to {{nft.name}} 
                                <v-icon dense color="blue">mdi-arrow-right</v-icon>
                            </a>
                        </div>
                    </div>
                </div>
                <div class="token-description">
                    <p>{{ nft.description }}</p>
                </div>
                <div class="divider">
                    <v-divider></v-divider>
                </div>
                <div class="collection-stats">
                    <h1>Token Info</h1>
                    <nft-token-info 
                        :token_id="nft.token_id"
                        :contract_address="nft.asset_contract.address"
                        :owner="nft.owner"
                        :last_sale="nft.last_sale"
                        :fees_usd="nft[nft.asset_contract.address].address.fees_usd"
                        :balance_usd="nft[nft.asset_contract.address].address.balance_usd"
                        :spent_usd="nft[nft.asset_contract.address].address.spent_usd"
                        :num_sales="nft.num_sales"
                        :transactions="nft[nft.asset_contract.address].calls"
                    ></nft-token-info>
                </div>
                <div class="collection-stats">
                    <h1>Collection Stats</h1>
                    <nft-collection-stats :collectionStats="collectionStats"></nft-collection-stats>
                </div>
            </div>
        </v-card>
    </v-container>
</template>
<script>
import NftCollectionStats from './NftCollectionStats.vue';
import NftTokenInfo from './NftTokenInfo.vue';

export default {
    name: 'NftDisplay',
    components: {
        NftCollectionStats,
        NftTokenInfo
    },
    props: {
        nft: {
            type: Object,
            default: null
        }
    },
    computed: {
        collectionStats() {
            return this.nft.collection.stats;
        }
    }
    
}
</script>
<style lang="scss">
.row {
    margin: 0 !important;
}

.nft {

    .divider {
        padding: 32px;
    }

    .body-top {
        border-bottom: 1px black solid;
    }

    &__header {
        padding: 1em;
        border-bottom: 1px solid black;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        position: relative;
        background-color: #6f36bc;
    }

    &__top-level {
        display: flex;
        align-items: flex-start;
        background-color: #36174D;
        color: white;
        padding-right: 3em;
        padding-left: 3em;
    }

    &__logo {
        padding: 2em;

        img {
            max-width: 400px;
        }
    }

    &__description {
        font-size: 1.25em;
        padding: 32px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;

        p {

            v-icon, a {
                padding: 5px;
            }
        }

        h2 {
            padding-bottom: 10px;
        }
    }

    .token-description {
        width: 100%;
        padding: 3em;
        background-color: #36174D;
        color: white;
        font-size: 1.5em;
    }

    .collection-stats {
        padding: 3em;
    }

    .title {
        color: white;
    }
    
}
    
</style>