<template>
    <div :class="clientWidth < viewportBreakpoint ? 'small-content' : 'top-content'">
            <div class="gain-content" v-if="clientWidth > viewportBreakpoint">
                <div @click="showNewsDetail($event)" v-for="(item, i) in newsList" :key="i" class="news-detail" :data-url="'//unsplash.it/200/200?images=' + i">
                    <h3>News: {{ item.title.toUpperCase().split(' ').slice(0,3).join(' ')}}</h3>
                    <div class="img" :style="{backgroundImage:'url('+ '//unsplash.it/400/400?images=' + i + ')'}"> </div>    
                    <p :data-msg="'Updated: 20 July , 2016, 12:' + (i  > 9 ? i : '0' + i) "> Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptatum distinctio modi non atque, illum quos! Totam, ab amet omnis expedita eveniet, optio nulla sequi cumque eos at voluptatum delectus ullam. Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis aliquam at aspernatur rem! Nihil, odio vero rem perferendis in, eius animi eum ratione blanditiis quisquam autem repudiandae corporis sed accusamus.</p>
                </div>
            </div>

             <div class="gain-content" v-if="clientWidth < viewportBreakpoint">
                <div @click="showNewsDetail($event)" v-for="(item, i) in newsList" :key="i" :data-url="'//unsplash.it/400/400?images=' + i" class="news-detail">
                    <div class="left">
                         <div class="img" :style="{backgroundImage:'url('+ '//unsplash.it/200/200?images=' + i + ')'}"> </div> 
                    </div>
                    <div class="right">
                        <h3>News: {{ item.title.toUpperCase().split(' ').slice(0,3).join(' ')}}</h3>   
                        <p>{{item.body}}</p>
                        <h4>{{'Updated: 20 July , 2016, 12:' + (i > 9 ? i : '0' + i)}}</h4>
                    </div>
                </div>
            </div>
            <div ref="loadMore" class="load-more" @click="loadMore">Load More</div>

            <div class="result" v-show="!newsList.length">No Record Found</div>
           
    </div>
</template>

<script>
import { mapGetters, mapActions , mapMutations } from 'vuex';
import bus from '@/assets/util/bus'
import openNewTab from '@/mixins/openNewTab';
export default {
  mixins: [openNewTab],
  data() {
    return {
       page: {start:0, limit:15},
       newsList:[],
       clientWidth: 1800,
       totalNews:45,
       allLoaded:false,
    }
  },
   components: {
    
  },
  computed: {
      ...mapGetters([
          'viewportBreakpoint',
          'searchBy',
      ]),
  },
  methods: {
      ...mapMutations([

          
      ]),
      ...mapActions([
        'getNewsList'
      ]),

      showNewsDetail(evt) {
          const url = evt.target.dataset.url ;
          this.openNewTab(url);
      },
      async loadMore() {
        if(this.allLoaded) return;
        this.page.start += 15;
        if (this.page.start >= this.totalNews) {
            this.$refs.loadMore.classList.add('disable');
            this.allLoaded = true;
        }
        try{
            let map = await this.getNewsList(this.page);
            if(!map) return;
            this.newsList = [...this.newsList, ...map];
        }catch(e) {
            console.log(e);
        }
        
      },
  },
 
  async mounted() {
      try{
        let map = await this.getNewsList(this.page);
        this.newsList = map; 
        this.clientWidth = document.body.clientWidth;
        this.page.start = 15;
      }catch(e) {
          console.log(e);
      }
       window.addEventListener('resize', () => {
            this.clientWidth = document.body.clientWidth;
       });
  },
  beforeDestroy() {
        
  },
  watch: {
      searchBy(newVal, oldVal) {
          if(newVal) {
            this.$refs.loadMore.classList.add('hidden');
            let str = newVal.toUpperCase();
            window.setTimeout(async () => {
                 let map = await this.getNewsList({start:0, limit:this.totalNews});
                 this.newsList = map.filter( s => s.title.toUpperCase().split(' ').slice(0,3).join(' ').includes(str));
                 if(!this.newsList.length) {
                    document.querySelector('.result').classList.add('empty-search');
                 }else {
                    document.querySelector('.result').classList.remove('empty-search');
                 }
            },0);
           
          }else {
            this.page.start = 0;
            this.allLoaded = false;
            this.newsList = [];
            this.loadMore();
            document.querySelector('.result').classList.remove('empty-search');
            this.$refs.loadMore.classList.remove('disable');
            this.$refs.loadMore.classList.remove('hidden');
          }
      }
  },
  name: 'News',
}
</script>


<style lang="scss" scoped>
 .empty-search {
    position:absolute;
    top:0;
    left:0;
    bottom:0;
    right:0;
    text-align: center;
    background: black;
    color:white;
    font-size:32px;
    line-height: 150px;
    opacity: 1;
    animation: showup 0.3s ease-in ;
 }

 @keyframes showup {
     0%{
      opacity:0;
     }
     100%{
        opacity:1;
     }
     
 }
  .hidden {
      display:none;
  }
  .news-detail {
      cursor: pointer;
      & > * {
          pointer-events: none;
      }
  }
  .small-content{
     min-height:calc(100vh - 120px);
     position: relative;
      .load-more{
            margin:10px 5px;
            width:98%;
            padding-top:15px;
            padding-bottom:15px;
            text-align: center;
            font-size:18px;
            border-radius: 5px;
            background: #2d0707;
            color:white;
            cursor: pointer;
    }
    .disable{
      background-color:#ccc;
      cursor:not-allowed;
    }
     .gain-content {
         display:flex;
         flex-direction: column;
        
         & > div {
              display:flex;
              .left {
                  width: 200px;
                  padding-top:8px;
                  padding-left:10px;
                  margin-right:10px;
                   .img {
                    height:160px;
                    width:100%;
                    background: no-repeat center / cover;
                  }
              }
              .right {
                  flex:1;
                  margin-top:20px;
                  padding-right:10px;
                 margin-bottom: 10px;
                   h3 {
                    font-size:20px;
                    margin-bottom: 10px;
                  }
                  p {
                    font-size:16px;
                    margin-bottom: 10px;
                    position: relative;
                  }

              }
             
         }
     }
  }
</style>

<style lang="scss" scoped>
 @import "@/assets/scss/animate.scss";
 .top-content {
    min-height:calc(100vh - 205px); // 205 == header + footer height
    margin-left:20px;
    margin-top:20px;
    margin-right:20px;
    position: relative;
    
    .load-more{
        width:100%;
        height:50px;
        text-align: center;
        line-height: 50px;
        font-size:18px;
        border-radius: 5px;
        background: #2d0707;
        color:white;
        cursor: pointer;
    }
     .disable{
      background-color:#ccc;
      cursor:not-allowed;
    }
    .gain-content {
    display:grid;
    margin-bottom:40px;
    grid-template-columns: repeat(3, minmax(380px, 1fr));
    grid-row-gap: 45px;
    grid-column-gap: 40px;
    & > div {
        border: 1px solid black;
        height:475px;
        padding:20px 10px 15px 10px;
        display:flex;
        flex-direction: column;
        color:#000;
        text-align: left;
        h3 {
           font-size:20px;
           margin-bottom: 20px;
        }
        .img {
            height:160px;
            width:100%;
            background: no-repeat center / cover;
            margin-bottom: 10px;
        }
        p {
           font-size:16px;
           height:200px;
           margin-bottom: 10px;
           position: relative;
           &::after{
               content: attr(data-msg);
               position:absolute;
               bottom: -10px;
               font-size:16px;
               width:100%;
               height:20px;
               display:block;
               
           }
        }
       
    }
 }
 }
 
</style>

