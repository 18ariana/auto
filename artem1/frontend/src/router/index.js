import Vue from 'vue'
import Router from 'vue-router'
import Orders from "../components/Orders";
import HelloWorld from "../components/HelloWorld";
import AddOrder from "../components/AddOrder";
import UpdateOrder from "../components/UpdateOrder";
Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/orders',
      name: 'Orders',
      component: Orders
    },
        {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/add_order',
      name: 'AddOrder',
      component: AddOrder
    },
     {
      path: '/update_order/:currOrder',
      name: 'UpdateOrder',
    component: UpdateOrder,
       props: true
    },
]})
