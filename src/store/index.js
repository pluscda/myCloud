import Vue from 'vue';
import Vuex from 'vuex';
import * as common from './common-module';
import * as news from './news-module';

// console log vuex
import createLogger from 'vuex/dist/logger';
class Modules {
  constructor() {
      this.modules = {};
  }
  addModules(obj) {
      let self = this;
      Object.keys(obj).forEach(key => {
        console.log(key)
          self.modules[key] = obj[key];
      });
  }
  getModules() {
      return this.modules;
  }
}

let modules = new Modules();
modules.addModules(common);
modules.addModules(news);
Vue.use(Vuex)
const debug = process.env.NODE_ENV === 'development' ? true : false;
export default new Vuex.Store({
  modules: modules.getModules(),
  strict: debug,
  plugins: debug ? [createLogger()] : []
});
