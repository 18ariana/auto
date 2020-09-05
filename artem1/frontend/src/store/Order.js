import axios from 'axios';
import Order from "./OrderPrototype";
import Api from "@/services/api";

export default {
  namespaced: true,
  state: {
    orders: [],
    currOrder: null
  },
  mutations: {
     SET_ORDERS(state, orders) {
      state.orders = orders;
    },
    EDIT_ORDER(state, order) {
      let v = state.orders.find(v => v.id === order.id);
      v = order;
    },
  },
  actions: {
     async loadAll({commit, dispatch}){
      let response1 = await fetch('http://127.0.0.1:8000/orders/');
      let or = await response1.json();

      commit('SET_ORDERS', or);
    },
    async edit({commit}, order) {
      let response = await Api().put(`/order/update/$order.id}`, order);
      let newOrder = await response.json();
      commit('EDIT_ORDER', newOrder);
      return newOrder;
    },
    getters: {
       order(state){
         return state.orders.find(order => order.id === state.currOrder)
       },
      currentOrder(state){
         return state.currOrder
      }
    }
  }}

