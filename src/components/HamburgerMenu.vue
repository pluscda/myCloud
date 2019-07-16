<template>
    <div class="gain-menu" @click.stop="handle_close">
        <div class="wrapper">
            <div @click="changeView($event,'/', 'News')">News</div>
            <div @click="changeView($event,'/region', 'Regions')">Regions</div>
            <div @click="changeView($event,'/video', 'Video')">Video</div>
            <div @click="changeView($event,'/tv', 'TV')">TV</div>
            
        </div>
                          
    </div>
</template>

<script>
    import { mapMutations } from 'vuex';
    import bus from '@/assets/util/bus';
    export default {
        data() {
            return {
             
            };
        },
        computed: {
           
        },
        methods: {
            ...mapMutations([
                'setMenuShow'
            ]),
            handle_close() {
                this.setMenuShow();
            },
            changeView(evt,path, name){
                this.$router.push(path);
                bus.$emit('routechange', name);
            },
           
        },
        created() {
           
        },
        mounted() {
        }
    };
</script>

<style lang="scss" scoped>

    .gain-menu{
        text-align: center;
        position: fixed;
        z-index: 9999;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        cursor: pointer;
        display: flex;
        justify-content: flex-end;
        background-color: rgba(#000, 0.6);
    }

    .wrapper{
        position: absolute;
        width: 60vw;
        height: 300px;
        display: flex;
        right:20px;
        top:20px;
        background:rgb(240, 15, 0) ;
        border-radius: 5px;
        flex-direction: column;
        padding-top: 20px;
        > div {
           width:100%;
           height:40px;
           color:#fff;
           text-align:left;
           padding-left:14px;
           margin-bottom:30px;
           font-size:30px;
        }

    }
   
</style>