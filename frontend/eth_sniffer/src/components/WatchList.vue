<template>
    <div>
        <v-simple-table
        item-key="name"
        class="elevation-1"
        >
            <tr class="header__row">
                <td 
                    v-for="watchListHeader of watchListHeaders"
                    :key="watchListHeader">
                    {{ watchListHeader }}
                </td>
            </tr>
            <div class="watchlist__items" v-if="assets">
                <tr 
                    v-for="asset of assets"
                    :key="asset.name"
                >
                    <td class="watchlist__asset">
                        
                    </td>
                </tr>
            </div>
        </v-simple-table>
    </div>
</template>
<script>
    export default {
        props: {
            assets: Array,
            required: false
        },
        data() {
            return {
                watchListHeaders: ['Asset', 'Price', 'Change', 'Market Cap', 'Watch']
            }
        },
        computed: {
            assetNames: function() {
                assets.forEach(asset => {
                    return asset.name
                });
            }
        }
    }
</script>
<style lang="scss">
    
</style>