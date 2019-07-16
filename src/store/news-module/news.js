import Vue from "vue";

/**
 * @author Alex
 * @description news applied in APP
 */


const state = {
    calculateBy: '',
   
};

// get filter data from state
const getters = {
    calculateBy: state => state.calculateBy,
};

// init actions 
const actions = {
   async getNewsList({commit,state}, {start,limit}) {
        //console.log('getNewsList start with ' + start);
        return await Vue.axios.get(`http://jsonplaceholder.typicode.com/posts?_start=${start}&_limit=${limit}`);
    },

   updateSearchTerm({commit,state}, search) {
        commit('updateNewsSearhTerm', search);
   },
};

const mutations = {
   updateNewsSearhTerm(state, search) {
        state.calculateBy = search;
   }
    
};

export default {
    state,
    actions,
    getters,
    mutations
};