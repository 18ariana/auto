<template>
 <div>
    <section>
      <v-simple-table>
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-center">№ Заказа</th>
              <th class="text-center">Мобильный номер</th>
              <th class="text-center">ФИ заказчика</th>
              <th class="text-center">Артикул</th>
              <th class="text-center">Бренд</th>
              <th class="text-center">Дата заказа</th>
              <th class="text-center">Выбранная дата доставки</th>
              <th class="text-center">Позиций</th>
              <th class="text-center">Было заказано</th>
              <th class="text-center">Статус</th>
              <th class="text-center">Цена за штуку</th>
              <th class="text-center">Сумма</th>
              <th class="text-center">Предоплата</th>
              <th class="text-center">Описание</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>{{ currOrder["number"] }}</td>
              <td>{{ currOrder.telephone }}</td>
              <td>{{ currOrder.name }}</td>
              <td>{{ currOrder.articul }}</td>
              <td>{{ currOrder.brand }}</td>
              <td>{{ currOrder.term }}</td>
              <td>{{ currOrder.term_wanted }}</td>
              <td>{{currOrder["amount_actual"] }}</td>
              <td>{{ currOrder["amount_wanted"] }}</td>
              <td>{{currOrder.status }}</td>
              <td>{{ currOrder.cost }}</td>
              <td>{{ currOrder.pre_cost }}</td>
              <td>{{ currOrder.total_cost }}</td>
              <td>{{ currOrder.description }}</td>
          </tr>
          </tbody>
        </template>
      </v-simple-table>
    </section>
  </div>

</template>

<script>

    export default {
        name: "UpdateOrder",
      props : ['currOrder'],
      data () {
          return{
             currentOrder: {
            telephone: '',
            name: '',
            number: '',
            brand: '',
            articul: '',
            term: '',
            term_wanted: '',
            amount_wanted: '',
            amount_actual: '',
            cost: '',
            pre_cost: '',
            status: '',
            description: ''
          },
          }
      },
    computed: {
        order(){
          console.log(this.$store.getters.currentOrder);
          return this.$store.getters.currentOrder
        }

        },

    }
</script>

<style scoped>

</style>
