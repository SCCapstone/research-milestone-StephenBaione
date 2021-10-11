<template>
    <v-card>
        <div class="card-title">
            <v-card-title>
                Search for NFTs
            </v-card-title>
        </div>
        <div class="input">
            <v-alert v-if="showAlert" type="error" prominent>Please enter a Contract Address and Token ID
                <template v-slot:actions>
                    <v-icon>mdi-exclamation-thick</v-icon>
                </template>
            </v-alert>
            <v-text-field label="Contract Address"
                v-model="contractAddress">
            </v-text-field>
            <v-text-field label="Token ID"
                v-model="tokenId">
            </v-text-field>
            <v-btn @click="getAsset()"
            color="#6f36bc">
                Search
            </v-btn>
        </div>
    </v-card>
</template>
<script>
    import { ServiceRequest } from '../service/ServiceRequest';
    import VueRouter from 'vue-router';

    export default {
        name: "NftSearch",
        data() {
            return {
                contractAddress: '',
                tokenId: '',
                showAlert: false
            }
        },
        methods: {
            getAsset: function() {
                this.showAlert = false;
                if (this.contractAddress === '' || this.tokenId === '') {
                    this.showAlert = true;
                    return null;
                }
                var serviceRequest = new ServiceRequest();
                serviceRequest.getNFT(this.contractAddress, this.tokenId)
                .then(result => { this.$emit('getAsset', result) });
            }
        },
    }
</script>
<style lang="scss">
    .input {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 2em;

            .v-text-field {
                width: 50%;
            }

            .v-btn__content {
                color: white;
            }
        }

    .card-title {
        border-bottom: 0.5px solid black;
        color: white;
        background-color: #6f36bc;
    }

</style>
