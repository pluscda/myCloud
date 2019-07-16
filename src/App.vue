<template>
  <div id="app" ref="refBody" class="gain-app">
    <router-view name="commonHeader"></router-view>
       <div id="gain-content" class="content">
            <router-view class="main"></router-view>   <!--default router view-->
            
       </div>
      <HamburgerMenuCompoment v-if="isMobileMenuShow"></HamburgerMenuCompoment>
  </div>
</template>
<script>
  import { mapGetters, mapActions , mapMutations } from 'vuex';
  import HamburgerMenuCompoment from '@/components/HamburgerMenu'
  export default {
        data() {
            return {
              
            };
        },
        components: {
          HamburgerMenuCompoment,
        },
        computed: {
           ...mapGetters([
           ]),
           isMobileMenuShow() {
                return this.$store.state.global.mobileTopMenuShow ;
           },
     
        },
        methods: {
           ...mapMutations([

               
           ]),
           ...mapActions([
             'getNewsList',
             'updateSearchTerm',
           ]),
           
        },
        async mounted() {
            
        },
        beforeDestroy() {
             
        },
        created() {
           
        },
        watch: {
            $route(newVal, oldVal) {
                this.updateSearchTerm('');
                const container = document.querySelector('#gain-content');
                container.scrollTop = 0;
            },
        }
        
  }
</script>


<style>
html {
  box-sizing: border-box;
  font-size: 62.5%; /* 10 /16 * 100%  nearly 10px*/ 
}
*, *::before, *::after {
  box-sizing: inherit;
  margin:0px;
  padding:0px;
  outline: 0px;
}

body{
    overflow: hidden;
}
</style>
<style lang="scss" scoped>

@import '@/assets/scss/mixins.scss';
#app {
  font-family: Arial, Verdana,Geneva,Microsoft YaHei, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  position: relative;
  overflow-x: hidden;
  
}

#gain-content {
    max-height:calc(100vh - 140px );
    overflow-x: hidden;
    position: relative;
    @include scrollbar-style();
     -webkit-overflow-scrolling: touch;
    
   
}
</style>
