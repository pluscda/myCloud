import Vue from "vue";

/**
 * @author Alex
 * @description global applied in APP
 */


// mutations-type config
// const Types = {
//     GET_COUNTRIES_SUCCESS: 'common/GET_COUNTRIES_SUCCESS',
//     SET_MENU: 'common/SET_MENU',
//     RELOAD_PAGE: 'common/RELOAD_PAGE',
//     RELOAD_PAGE_SLOW: 'common/RELOAD_PAGE_SLOW',
//     GET_USER_LANGUAGE: 'common/GET_USER_LANGUAGE',
//     GET_TIME_ZONES: 'common/GET_TIME_ZONES',
//     SET_CURRENT_LANG: 'common/SET_CURRENT_LANG'
// };

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