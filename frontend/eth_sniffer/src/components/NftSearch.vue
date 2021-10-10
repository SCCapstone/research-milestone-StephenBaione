<template>
    <v-card>
        <div class="input">
            <v-text-field label="Contract Address"
            v-model="contractAddress">
            </v-text-field>
            <v-text-field label="Token ID"
            v-model="tokenId">
            </v-text-field>
            <v-btn @click="getAsset()">
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
                tokenId: ''
            }
        },
        methods: {
            getAsset: function() {
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
        }

</style>
