<template>
  <p style="margin-left:40px;">{{calculateBy}}  {{ !calculateBy ? '' : '= '  + result }}</p>
</template>

<script>
import { mapGetters, mapActions , mapMutations } from 'vuex';
import bus from '@/assets/util/bus'
import openNewTab from '@/mixins/openNewTab';
import { normalize } from 'path';
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
      reorganizeArray(array){
        var reorganized = [];
        var k = -1;
        while(++k < array.length){
            if(array[k] !== false) reorganized.push(array[k]);
        }
        return reorganized;
      },
      doTheMath(op, array){
        let t1 = op-1;
        let t2 = op+1;

        switch(array[op]){

            case '*':
                array[t1] = parseFloat(array[t1]) * parseFloat(array[t2]);
                break;

            case '/':
                array[t1] = parseFloat(array[t1]) / parseFloat(array[t2]);
                break;
            case '+':
                array[t1] = parseFloat(array[t1]) + parseFloat(array[t2]);
                break;
            case '-':
                        array[t1] = parseFloat(array[t1]) - parseFloat(array[t2]);
                        break;
            }

            array[op] = false;
            array[t2] = false;

            return this.reorganizeArray(array);

    },
    calculate(string){

        // break the string into numbers and operators
        var cArray = (string.match(/([0-9]+)|\+|-|\*|\//g));
        let i = -1;

        if(!cArray || cArray.length == 1) return string;
        
        // multiplications
        while(i++ < cArray.length - 1){

            if(cArray[i] == '*'){
                cArray = this.doTheMath(i, cArray);
                i = i-1;
            }

        }

        // divisions
        i = -1;
        while(i++ < cArray.length - 1){

            if(cArray[i] == '/'){
                cArray = this.doTheMath(i, cArray);
                i--;
            }

        }

        // sum/substract
        i = -1;
        while(i++ < cArray.length - 1){

            if(cArray[i] == '+'){
                cArray = this.doTheMath(i, cArray);
                i--;
            }

            if(cArray[i] == '-'){
                cArray = this.doTheMath(i, cArray);
                i--;
            }

        }

        return cArray[0];

    },
    calculateFull(str){
        // clean the string from spaces
        str = str.replace(/ /g,'');

        // declare the final result variable
        var result = str;

        // brake the strings there are between parentheses
        var subCalculations = str.match(/\(([^()]+)\)/gmi); 
        var subCalc;

        if(!subCalculations)
            return this.calculate(str);

        for(let k = 0; k < subCalculations.length; k++){
            subCalc = subCalculations[k].replace(/\(|\)/g, '');
            console.log('Replacing (' + subCalc + ') by ' + this.calculate(subCalc));
            result = result.replace('('+subCalc+')', this.calculate(subCalc));
        }

        // verify if the string still have parentheses and recursively resolves them
        if(result.indexOf('(') >= 0)
            return this.calculateFull(result);

        console.log("String after subcalculations are done: " + result);
        return this.calculate(result);
        
    },
  },

    mounted() {
        
    },
    beforeDestroy() {
            
    },
    watch: {
        calculateBy(newVal, oldVal) {
            if(newVal) {
                this.result = this.calculateFull(newVal);
            }else{
                this.result = '';
            }
        }
    },
    name: 'calc'
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

