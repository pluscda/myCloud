import Vue from "vue";

/**
 * @author Alex
 * @description global applied in APP
 */

const state = {
    viewpointSizeBreakPoint: 1246,
    mobileTopMenuShow:false,
   
};

// get filter data from state
const getters = {
    viewportBreakpoint: state => state.viewpointSizeBreakPoint,
   
};

// init actions 
const actions = {
  
};

const mutations = {
   setMenuShow(state){
      state.mobileTopMenuShow = !state.mobileTopMenuShow;
   }
    
};

export default {
    state,
    actions,
    getters,
    mutations
};