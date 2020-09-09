import axios from 'axios';
import Order from "./OrderPrototype";


export default {
  namespaced: true,
  state: {
    orders: [],
    currOrder: null
  },
  mutations: {
     set_orders(state, payload) {
      state.orders.push(payload)
    },
    currentOrder(state, payload){
       state.currOrder = payload
    },

  },
  actions: {
    currOrder({ commit }, payload) {
      commit('currOrder', payload)
  },
    orders({ commit, dispatch}) {
       commit('clearError');
      commit('setLoading', true);
      axios
        .get('http://127.0.0.1:8000/orders/')
        .then((response) => {
          let data = response.data;
          dispatch('set_orders', data);

          commit('set_orders', data);
          commit('setLoading', false)
        })
    }
  },
    getters: {
       currentOrder(state){
         console.log('Order is ',state.orders.find(order => order.id === state.currOrder) );
         return state.orders.find(order => order.id === state.currOrder)
       },
      orders(state){
         console.log('Orders are', state.orders);
         return state.orders
      }
    }
  }

