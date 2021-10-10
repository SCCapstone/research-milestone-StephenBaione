<template>
    <v-container v-if="nft" class="nft">
        <v-card width="500">
            <div class="nft__header">
                <v-card-title class="title justify-center">{{ nft.name }}</v-card-title>
                <div class="nft__watchlist">
                    <p>Add to Watchlist</p>
                    <v-icon color="blue" @click="addToWatchlist">mdi-plus</v-icon>
                </div>
            </div>
            <div class="nft__logo text-center">
                <img :src="nft.image_url"/>
            </div>
            <div class="nft__description text-center">
                <v-card-text>{{ nft.description }}</v-card-text>
            </div>
            <div class="nft__link text-center">
                <a :href="nft.external_link"> Go to {{nft.name}} 
                    <v-icon dense color="blue">mdi-arrow-right</v-icon>
                </a>
            </div>
        </v-card>
    </v-container>
</template>
<script>

export default {
    name: 'NftDisplay',
    props: {
        nft: {
            type: Object,
            required: true
        }
    },
    methods: {
        addToWatchlist() {
            this.active = true;
            return true;
        },
        removeFromWatchList() {
            this.active = false;
            return true;
        }
    },
    
}
</script>
<style lang="scss">
.nft {
    &__header {
        padding: 1em;
        border-bottom: 1px solid black;
        position: relative;

        .nft__watchlist, .title {
            display: inline-block;
        }

        .nft__watchlist {
            position: absolute;
            right: 0;
            padding-right: 1em;
            padding-top: 16px;

            p, v-icon {
                display: inline-block;
            }
        }
    }

    &__logo {
        padding: 2em;

        img {
            max-width: 400px;
        }
    }

    &__description {
        font-size: 4em;
    }

    &__link {
        padding: 2em;
    }
}
    
</style>