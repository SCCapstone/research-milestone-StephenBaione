<template>
    <v-container>
        <v-card class="asset__card">
            <div class="asset__header">
                <v-card-title>{{ name }}</v-card-title>
                <v-card-subtitle>${{ marketPrice }}</v-card-subtitle>
                <div class="asset__inflation">
                    <v-icon v-if="inflationUsd >= 0" color="green" dense>mdi-arrow-top-right</v-icon>
                    <v-icon v-else color="red" dense>mdi-arrow-bottom-right</v-icon>
                    <p :class="{positiveInflation: inflationUsd >= 0, negativeInflation: inflationUsd < 0}">{{ inflationUsd }}</p>
                </div>
            </div>
            <div class="asset__logo text-center">
                <img :src="require('../assets/' + name.toLowerCase() + '-logo.png')" alt="name"/>
            </div>
            <div class="asset__expandable">
                <v-expansion-panels>
                    <v-expansion-panel>
                        <v-expansion-panel-header>
                            Market Data
                            <template v-slot:actions>
                                <v-icon large>
                                    mdi-plus
                                </v-icon>
                            </template>
                        </v-expansion-panel-header>
                        <v-expansion-panel-content>
                            <template>
                                <v-simple-table>
                                    <template v-slot:default>
                                    <tbody>
                                        <tr>
                                            <td>Market Price:</td>
                                            <td>${{ marketPriceUsd }}</td>
                                        </tr>
                                        <tr>
                                            <td>Market Cap:</td>
                                            <td>${{ marketCapUsd }}</td>
                                        </tr>
                                        <tr>
                                            <td>Average Transaction Fee:</td>
                                            <td>${{ averageTransactionFee }}</td>
                                        </tr>
                                        <tr>
                                            <td>Inflation USD:</td>
                                            <td>${{ inflationUsd }}</td>
                                        </tr>
                                    </tbody>
                                    </template>
                                </v-simple-table>
                            </template>
                        </v-expansion-panel-content>
                    </v-expansion-panel>
                </v-expansion-panels>
            </div>
        </v-card>
    </v-container>
</template>
<script>
export default {
    name: "AssetDisplay",
    props: {
        name: {
            type: String,
            required: true
        },
        marketPrice: {
            type: Number,
            required: true
        },
        averageTransactionFee: {
            type: Number,
            required: true
        },
        marketPriceUsd: {
            type: Number,
            required: true
        },
        marketCapUsd: {
            type: Number,
            required: true
        },
        inflationUsd: {
            type: Number,
            required: true
        }
    }
}
</script>
<style lang="scss">

.asset {
    &__card {
        max-width: 25vw;
    }

    &__logo {
        padding: 2em;

        img {
            max-height: 200px;
        }
    }

    &__header {
        position: relative;
        border-bottom: 1px solid black;
    }

    &__inflation {
        position: absolute;
        top: 0;
        right: 0;
        padding-right: 1em;
        padding-top: 16px;

        v-icon, p {
            display: inline-block;
            padding: 5px;
        }
    }
}

.positiveInflation {
    color: green;
}

.negativeInflation {
    color: red;
}
    
</style>

