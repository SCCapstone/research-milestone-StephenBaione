<template>
    <div class="nft__info">
        <v-row>
            <v-expansion-panels>
                <v-expansion-panel>
                    <v-expansion-panel-header>
                        NFT
                        <template v-slot:actions>
                            <v-icon>mdi-drawing-box</v-icon>
                        </template>
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                        <div class="token__table">
                            <template>
                                <v-simple-table>
                                    <tbody>
                                        <tr>
                                            <td>Contract Address:</td>
                                            <td>{{ contract_address }}</td>
                                        </tr>
                                        <tr>
                                            <td>Token ID:</td>
                                            <td>{{ token_id }}</td>
                                        </tr>
                                        <tr>
                                            <td>Owner:</td>
                                            <td>
                                                <div class="token__owner">
                                                    <v-img :src="owner.profile_img_url" alt="profile image" max-height="50px" max-width="50px"></v-img>
                                                    <p>{{ owner.address }}</p>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>Spent (USD):</td>
                                            <td>${{ spent_usd }}</td>
                                        </tr>
                                        <tr>
                                            <td>Balance (USD):</td>
                                            <td>${{ balance_usd }}</td>
                                        </tr>
                                        <tr>
                                            <td>Fees USD:</td>
                                            <td>${{ fees_usd }}</td>
                                        </tr>
                                    </tbody>
                                </v-simple-table>
                            </template>
                        </div>
                    </v-expansion-panel-content>
                </v-expansion-panel>
                <v-expansion-panel>
                    <v-expansion-panel-header>
                        Sales Data
                        <template v-slot:actions>
                            <v-icon>mdi-gold</v-icon>
                        </template>
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                        <div class="token__table">
                            <template>
                                <v-simple-table>
                                    <tbody>
                                        <tr>
                                            <td>Number of Sales:</td>
                                            <td>{{ num_sales }}</td>
                                        </tr>
                                        <tr>
                                            <td>Spent (USD):</td>
                                            <td>${{ spent_usd }}</td>
                                        </tr>
                                        <tr>
                                            <td>Balance (USD):</td>
                                            <td>${{ balance_usd }}</td>
                                        </tr>
                                        <tr>
                                            <td>Fees USD:</td>
                                            <td>${{ fees_usd }}</td>
                                        </tr>
                                    </tbody>
                                </v-simple-table>
                            </template>
                        </div>
                    </v-expansion-panel-content>
                </v-expansion-panel>
                <v-expansion-panel>
                    <v-expansion-panel-header>
                        Transactions
                        <template v-slot:actions>
                            <v-icon>mdi-diamond</v-icon>
                        </template>
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                        <div class="token__table transactions">
                            <template>
                                <v-simple-table>
                                    <thead>
                                        <th>Block ID</th>
                                        <th>Sender</th>
                                        <th>Recipient</th>
                                        <th>Transaction Hash</th>
                                        <th>Transferred</th>
                                        <th>Value (USD)</th>
                                    </thead>
                                    <tbody>
                                        <tr v-for="(transaction, index) of transactions"
                                        :key="index">
                                            <td>{{ transaction.block_id }}</td>
                                            <td>{{ transaction.sender }}</td>
                                            <td>{{ transaction.recipient }}</td>
                                            <td>{{ transaction.transaction_hash }}</td>
                                            <td>{{ transaction.transferred }}</td>
                                            <td>${{ transaction.value_usd }}</td>
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
    name: "NftTokenInfo",
    props: {
        token_id: {
            type: String,
            default: ""
        },
        contract_address: {
            type: String,
            default: ""
        },
        owner: {
            type: Object,
            default: null
        },
        fees_usd: {
            type: Number,
            default: null
        },
        balance_usd: {
            type: Number,
            default: null
        },
        spent_usd: {
            type: Number,
            default: null
        },
        num_sales: {
            type: Number,
            default: null
        },
        transactions: {
            type: Array,
            default: null
        }
    }
}
</script>
<style lang="scss">
    .transactions {
        th, td {
            border: 1px solid black;
        }
    }

    .token__owner {
        display: flex;
        align-items: center;
        justify-content: flex-start;

        p {
            margin: 0;
            padding-left: 10px;
        }

        v-img {
            padding-right: 10px;
        }
    }

    v-expansion-panel-header {
        background-color: #36174D;
    }
</style>