<template>
    <v-container>
        <div v-if="assetDisplays" class="layout">
            <div class="layout__child"
                v-for="assetDisplay of assetDisplays"
                :key="assetDisplay.name"
            >
                <asset-display 
                    :name="assetDisplay.name"
                    :marketPrice="assetDisplay.marketPrice"
                    :averageTransactionFee="assetDisplay.averageTransactionFee"
                    :marketPriceUsd="assetDisplay.marketPriceUsd"
                    :marketCapUsd="assetDisplay.marketCapUsd"
                    :inflationUsd="assetDisplay.inflationUsd"
                >
                </asset-display>
            </div>
        </div>
    </v-container>
</template>
<script>
    import AssetDisplay from './AssetDisplay.vue';

    export default {

        name: "AssetDisplayLayout",
        components: {
            AssetDisplay
        },
        props: {
            assetDisplays: {
                type: Array,
                required: true
            }
        }
    }
</script>
<style lang="scss">
    .layout {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;

        &__child {
            flex: 1;
            flex-basis: 30%;
        }

        &__child:hover {
            cursor: pointer;
            box-shadow: 5px 5px 5px 5px gray;
            border-radius: 5px;
        }
    }
</style>