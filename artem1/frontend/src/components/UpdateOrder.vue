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
              <td>{{ item.number }}</td>
              <td>{{ item.telephone }}</td>
              <td>{{ item.name }}</td>
              <td>{{ item.articul }}</td>
              <td>{{ item.brand }}</td>
              <td>{{ item.term }}</td>
              <td>{{ item.term_wanted }}</td>
              <td>{{ item["amount_actual"] }}</td>
              <td>{{ item["amount_wanted"] }}</td>
              <td>{{ item.status }}</td>
              <td>{{ item.cost }}</td>
              <td>{{ item.pre_cost }}</td>
              <td>{{ item.total_cost }}</td>
              <td>{{ item.description }}</td>
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
             item: {
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
          this.item= this.$store.getters.order;

        }

        }
    }
</script>

<style scoped>

</style>
