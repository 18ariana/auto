import axios from 'axios';
import Order from "./OrderPrototype";


export default {
  namespaced: true,
  state: {
    orders: [],
    currOrder: null
  },
  mutations: {
     orders(state, payload) {
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
    orders({ commit}) {
      axios
        .get('http://127.0.0.1:8000/orders/')
        .then((response) => {
          let data = response.data;
          commit('orders', data);
          console.log('orders', data);
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

