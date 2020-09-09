import Vue from 'vue'
import Vuex from 'vuex'

// import your store modules here
import common from "./common";
import Order from "./Order"
Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    Order,
    common
  }
})
