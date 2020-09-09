<template>
  <div>
    <section>
      <v-simple-table>
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-center">№ Заказа</th>
              <th class="text-center">Дата заказа</th>
              <th class="text-center">Позиций</th>
              <th class="text-center">Сумма</th>
              <th class="text-center">Статус</th>
              <th class="text-center">Выбранная дата доставки</th>
              <th class="text-center">Описание</th>
              <th class="text-center">Редактировать заказ</th>
              <th class="text-center">Удалить заказ </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in orders">
              <td>{{ item.number }}</td>
              <td>{{ item.term }}</td>
              <td>{{ item.amount_actual }}</td>
              <td>{{ item.total_cost }}</td>
              <td>{{ item.status }}</td>
              <td>{{ item.term_wanted }}</td>
              <td>{{ item.description }}</td>

              <td><v-btn text small color="success" :to="'update_order/'+`${item.id}`">Редактировать</v-btn></td>

              <td> <v-btn text small color="error" @click="removeOrder(item)">Удалить заказ</v-btn></td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </section>
  </div>
</template>

<script>

    import axios from "axios";

    export default {
        name: "Orders",
      data () {
          return {
            orders: [],
            currentOrder: {},
          };
      },
      async created() {
        await this.fetchOrders();
      },
      methods: {
          async fetchOrders() {
             const response = await fetch('http://127.0.0.1:8000/orders/')
            this.orders = await response.json()
          },
        async removeOrder(order) {
            let token = localStorage.getItem('auth_token');
            const { id } = order;
            const response = await fetch(`http://127.0.0.1:8000/order/${id}?api_token=`+token, {
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization' : "Token "+token
              },
              method: "DELETE",
              });
            if (response.status !== 204) {
              alert(JSON.stringify(await response.json(), null, 2));
            }
            await this.fetchOrders();
        }
      }
    }
</script>

<style scoped>
   table {
    width: 300px; /* Ширина таблицы */
    border: 1px solid green; /* Рамка вокруг таблицы */
    margin: auto; /* Выравниваем таблицу по центру окна  */
   }
   td {
    text-align: center; /* Выравниваем текст по центру ячейки */
   }

    h2 {padding: 25px;}
input {
border: 1px solid #f7f7f7;
padding: 0.75rem 1.25rem;
}
</style>

