<template>
  <div :class="clientWidth < viewportBreakpoint ? 'small-header' : 'gain-header'" >
       
    <template v-if="clientWidth > viewportBreakpoint">
        <div class="logo"></div>
        <div class="menu-grid">
            <div @click="changeView($event,'/', 'News')">News</div>
            <div >Regions</div>
            <div >Video</div>
            <div >TV</div>
            <div class="search-div">
                <input ref="s1" maxlength="62" placeholder="Search"   @keydown.enter="calculateBy($event)">
            </div>
        </div>
    </template>
     
     <template v-else>
         <div class="top" :data-msg="title">
            <div class="logo"></div>
            <button class="hamburger-menu" @click="showMenu">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
        </div>
        <div class="bottom search-div">
                <input ref="s2" maxlength="62" placeholder="Search"  @keydown.enter="calculateBy($event)">
        </div>
    </template>
  </div>
</template>

<script>
 
  import { mapGetters, mapActions , mapMutations } from 'vuex';
  import bus from '@/assets/util/bus';
  import debounce from 'lodash.debounce';
  export default {
    data() {
        return {
            clientWidth:1839,
            title: 'News',
        }
    },
   
    computed: {
      ...mapGetters([
          'viewportBreakpoint'
      ]),
   
    },
    methods: {
     ...mapMutations([
       'setMenuShow'
               
    ]),
    ...mapActions([
        'updateSearchTerm',
    ]),
       lodashDebounce: debounce((evt,fun) => fun(evt),500),
       showMenu() {
          this.setMenuShow();
       },
       calculateBy(evt) {
          this.updateSearchTerm(evt.target.value);
       },
       changeView(evt,path, name){
           let el = document.querySelector('.selected-item');
           el  ? el.classList.remove('selected-item') : '';
           evt.target.classList.add('selected-item');
           this.$router.push(path);
           this.title = name;
       }
    },
    mounted() {
       this.clientWidth = document.body.clientWidth;
       window.addEventListener('resize', () => {
            this.clientWidth = document.body.clientWidth;
       });

       bus.$on('routechange', name => this.title = name);
      
    }
  }
</script>

<style lang="scss" scoped>

.small-header{
    height:120px;
    background:rgb(240, 15, 0) ;
    width:100%;
    position: relative;
    display:flex;
    flex-direction: column;
    
    .top {
        display:flex;
        justify-content: space-between;
        align-items: flex-start;
        height:70px;
        margin-bottom:10px;
        position: relative;
        &::after{
            content: attr(data-msg);
            position:absolute;
            display:block;
            top:40%;
            left:50%;
            transform: translate(-50%, -40%);
            text-align: center;
            font-size:24px;
            color:white;
        }
    }
    .bottom {
        width:100%;
        height: 40px;
        background: #2c0807;
        padding-left:10px;
        padding-right:10px;
        padding-top: 5px;
        position: relative;
        &::after {
            content:'';
            position:absolute;
            display:block;
            top:12px;
            left:20px;
            width:16px;
            height:16px;
            border-radius: 5px;
            background: url(../../assets/images/bypass-search.jpg) no-repeat center / contain;
        }
        input {
             padding-left:30px;
             display:inline-block;
             width: 100%;
             height:30px;
             color:white;
             border-radius: 5px;
             background: transparent;
             border-color: white;
        }
    }
   
    .logo {
       margin-left:18px;
       margin-top: 4px;
       width:50px;
       height:50px;
       z-index:2;
       border-radius: 50%;
       background: url(../../assets/images/logo.png) no-repeat center / contain;
    }

   .hamburger-menu {
        background: none;
        border: none;
        display: inline-block;
        margin-right:15px;
        margin-top:15px;
    }
    .hamburger-menu .icon-bar {
        background-color: white;
        display: block;
        height: 4px;
        margin: 0 auto 4px;
        width: 30px;
    }
}
</style>

<style lang="scss" scoped>
 .gain-header {
   background:rgb(240, 15, 0) ;
   width:100vw;
   display:flex;
   height: 140px;
   padding-left: 20px;
   padding-right:20px;
   margin-bottom:16px;
   .logo {
       min-width:120px;
       min-height:120px;
       width:120px;
       height:120px;
       border-radius: 50%;
       background: url(../../assets/images/logo.png) no-repeat center / contain;
       margin-top: 6px;
       margin-right:80px;
   }
   .menu-grid {
       flex:1;
       display:grid;
       margin-top: 30px;
       grid-template-areas: "news reg vid tv search";
       grid-template-columns: repeat(4, 200px) 1fr;
       height: 50px;
       background: #2d0707;
       .selected-item{
            background:#d8b81a;
            color:black;
       }
       > div {
           font-size: 18px;
           color:white;
           text-align: center;
           line-height: 50px;
           border-right:1px solid white;
           cursor: pointer;
           &:hover{
               font-size:20px;
           }
           
       }
       & > div:nth-child(1){
           grid-area: news;
       }
       & > div:nth-child(2){
           grid-area: reg;
       }
       & > div:nth-child(3){
           grid-area: vid;
       }
       & > div:nth-child(4){
           grid-area: tv;
       }
       & > div:nth-child(5){
           grid-area: search;
           border:none;
           padding-left:15px;
           padding-top:8px;
           display:flex;
           position: relative;
            &::after {
                content:'';
                position:absolute;
                display:block;
                top:15px;
                left:25px;
                width:16px;
                height:16px;
                border-radius: 5px;
                background: url(../../assets/images/bypass-search.jpg) no-repeat center / contain;
            }
           input {
             padding-left:30px;
             display:inline-block;
             width: calc(100% - 10px);
             height:30px;
             color:white;
             border-radius: 5px;
             background: transparent;
           }
       }
       
   }

 }

</style>