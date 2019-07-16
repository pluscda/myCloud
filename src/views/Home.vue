<template>
  <p style="margin-left:40px;">{{calculateBy}}  {{ !calculateBy ? '' : '= '  + result }}</p>
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
       result: 0,
    }
  },
   components: {
    
  },
  computed: {
      ...mapGetters([
          'viewportBreakpoint',
          'calculateBy',
      ]),
  },
  methods: {
      ...mapMutations([

          
      ]),
      ...mapActions([
        
      ]),

     calculate(num1, num2, operator) {
        num1 = parseFloat(num1);

        if (isNaN(num1)) {
            this.result = 'First parameter invalid. Must be a interger.';
        }

        num2 = parseFloat(num2);
       
        if (isNaN(num2)) {
            this.result = 'Second parameter invalid. Must be a interger.';
        }

        operator = operator.trim(); 
       // alert( operator);

        if (!/^\+$|^\-$|^\*$|^\/$/.test(operator)) {
            this.result = 'parameter invalid. Valid are + | - | * | /';
        }

        let calculations = {
            '+' : (numb1, numb2) => numb1 + numb2,
            '-' : (numb1, numb2) => numb1 - numb2,
            '*' : (numb1, numb2) => numb1 * numb2,
            '/' : (numb1, numb2) => numb1 / numb2
        }

        return calculations[operator](num1,num2);
      }
  },
 
  mounted() {
     
  },
  beforeDestroy() {
        
  },
  watch: {
      calculateBy(newVal, oldVal) {
          if(newVal) {
              console.log(newVal)
              let arr = newVal.trim().split('');
              let i = 0;
              let op1 = '';
              let op2 = '';
              let opt = '';
              this.result = '';
              for(i = 0 ; i < arr.length; ++i) {
                  if(!opt && !isNaN(arr[i]) && !this.result) {
                     op1 += arr[i];
                  }else if( /^\+$|^\-$|^\*$|^\/$/.test(arr[i])  && !opt) {
                     opt = arr[i];
                     op2 = '';
                  }else if(!isNaN(arr[i])) {
                     op2 += arr[i];
                  }
                  if(op1 && opt && op2 && isNaN(arr[i+1] )) {
                      console.log(op2);
                      op1 =  this.calculate(op1,op2, opt);
                      opt = op2 = '';
                      
                  }
              }
              this.result = Math.ceil(op1);
              
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

