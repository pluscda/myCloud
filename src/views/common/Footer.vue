<template>
  <div class="ampos-footer" v-if="clientWidth > viewportBreakpoint">
    <div class="footer-grid">
        <div>News</div>
        <div></div>
        <div>Regions</div>
         <div></div>
        <div>Video</div>
        <div></div>
        <div>TV</div>
    </div>
    <div></div>
    <div>Copyright &copy; AMPOS</div>
  </div>
 
</template>

<script>
  import { mapGetters, mapActions , mapMutations } from 'vuex';
  export default {
    data() {
      return {
          clientWidth:1839,
      }
    },
    computed: {
      ...mapGetters([
          'viewportBreakpoint'
      ]),
   
   },
    mounted() {
       this.clientWidth = document.body.clientWidth;
       window.addEventListener('resize', () => {
            this.clientWidth = document.body.clientWidth;
       });
    }
  }
</script>

<style lang="scss" scoped>
@media  (max-width: 768px)  { //ipad size
     
}
.ampos-footer{
 width:100vw;
 height:85px;
 background:rgb(240, 15, 0) ;
 display:flex;
 color:white;
 margin-top:71px;
    .footer-grid{
        display:grid;
        grid-template-columns:  min-content  1px min-content 1px min-content 1px min-content;
        grid-column-gap: 15px;
        margin-left:36px;
        > div:nth-child(odd){
            cursor: pointer;
        }
        > div:nth-child(even) {
            background: white;
            height:25px;
        }
    }
    & > div {
       // margin-bottom: 25px;
        font-size:18px;
        margin-top:25px;
        position: relative;
    }
    
    & > div:nth-child(2){
        flex:1;
    }

    & > div:nth-child(3){
        margin-right:20px;
    }
    
}

      
</style>