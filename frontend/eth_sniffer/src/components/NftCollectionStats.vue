<template>
    <div class="nft__stats" v-if="collectionStats">
        <v-row justify="center">
            <v-expansion-panels>
                <v-expansion-panel>
                    <v-expansion-panel-header>Overall Data</v-expansion-panel-header>
                    <v-expansion-panel-content>
                        <div class="collection__table">
                            <template>
                                <v-simple-table>
                                    <tbody>
                                        <tr>
                                            <td>Market Cap:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.market_cap }} ETH</td>
                                        </tr>
                                        <tr>
                                            <td>Average Price:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.average_price }} ETH</td>
                                        </tr>
                                        <tr>
                                            <td>Floor Price:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.floor_price }} ETH</td>
                                        </tr>
                                        <tr>
                                            <td>Volume:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.total_volume }} ETH</td>
                                        </tr>
                                        <tr>
                                            <td>Total Sales:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.total_sales }} ETH</td>
                                        </tr>
                                        <tr>
                                            <td>Total Supply:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.total_supply }} ETH</td>
                                        </tr>
                                    </tbody>
                                </v-simple-table>
                            </template>
                        </div>
                    </v-expansion-panel-content>
                </v-expansion-panel>
                <v-expansion-panel>
                    <v-expansion-panel-header>Past Day</v-expansion-panel-header>
                    <v-expansion-panel-content>
                        <div class="collection__table">
                            <v-simple-table>
                                <template>
                                    <tbody>
                                        <tr>
                                            <td>1 Day Average Price:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.one_day_average_price }} ETH</td>
                                        </tr>
                                        <tr>
                                            <td>1 Day Change:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.one_day_change }} ETH</td>
                                        </tr>
                                        <tr>
                                            <td>1 Day Sales:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.one_day_sales }} ETH</td>
                                        </tr>
                                        <tr>
                                            <td>1 Day Volume:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.one_day_volume }} ETH</td>
                                        </tr>
                                    </tbody>
                                </template>
                            </v-simple-table>
                        </div>
                    </v-expansion-panel-content>
                </v-expansion-panel>
                <v-expansion-panel accordian>
                    <v-expansion-panel-header>Past Week</v-expansion-panel-header>
                    <v-expansion-panel-content>
                        <div class="collection__table">
                            <template>
                                <v-simple-table>
                                    <tbody>
                                        <tr>
                                            <td>7 Day Average Price:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.seven_day_average_price }} ETH</td>
                                        </tr>
                                        <tr>
                                            <td>7 Day Change:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.seven_day_change }} ETH</td>
                                        </tr>
                                        <tr>
                                            <td>7 Day Sales:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.seven_day_sales }} ETH</td>
                                        </tr>
                                        <tr>
                                            <td>7 Day Volume:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.seven_day_volume }} ETH</td>
                                        </tr>
                                    </tbody>
                                </v-simple-table>
                            </template>
                        </div>
                    </v-expansion-panel-content>
                </v-expansion-panel>
                <v-expansion-panel>
                    <v-expansion-panel-header>Past Month</v-expansion-panel-header>
                    <v-expansion-panel-content>
                        <div class="collection__table">
                            <template>
                                <v-simple-table>
                                    <thead>
                                        <tr>
                                            <th>30 Day Performance:</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>30 Day Average Price:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.thirty_day_average_price }} ETH</td>
                                        </tr>
                                        <tr>
                                            <td>30 Day Change:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.thirty_day_change }} ETH</td>
                                        </tr>
                                        <tr>
                                            <td>30 Day Sales:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.thirty_day_sales }} ETH</td>
                                        </tr>
                                        <tr>
                                            <td>30 Day Volume:</td>
                                            <td><v-icon color="purple">mdi-ethereum</v-icon> {{ collectionStats.thirty_day_volume }} ETH</td>
                                        </tr>
                                    </tbody>
                                </v-simple-table>
                            </template>
                        </div>
                    </v-expansion-panel-content>
                </v-expansion-panel>
            </v-expansion-panels>
        </v-row>
    </div>
</template>
<script>
export default {
    name: "NftCollectionStats",
    props: {
        'collectionStats': {
            type: Object
        }
    }
    
}
</script>
<style lang="scss">
    
</style>