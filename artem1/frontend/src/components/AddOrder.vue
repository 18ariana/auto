<template>
  <div>
          <h2 align="center">Добавить Заказ</h2>

       <v-card class="mx-auto" max-width="650">
         <v-card-text>
           <v-text-field label="Номер телефона" v-model="currentOrder.telephone"></v-text-field>
           <v-text-field label="Фамилия, имя заказчика" v-model="currentOrder.name"></v-text-field>
          <v-text-field label="Номер заказа" v-model="currentOrder.number"></v-text-field>
          <v-text-field label="Бренд" v-model.number="currentOrder.brand"></v-text-field>
          <v-text-field label="Артикуль" v-model="currentOrder.articul"></v-text-field>
          <v-text-field label="Дата заказа" v-model="currentOrder.term"></v-text-field>
          <v-text-field label="Ожидается на складе(дата)" v-model="currentOrder.term_wanted"></v-text-field>
          <v-text-field label="Было заказано" v-model="currentOrder.amount_wanted"></v-text-field>
          <v-text-field label="Количество(пришло)" v-model="currentOrder.amount_actual"></v-text-field>
           <v-text-field label="Предоплата(руб)" v-model="currentOrder.pre_cost"></v-text-field>
          <v-text-field label="Цена за штуку" v-model="currentOrder.cost"></v-text-field>
          <v-select v-model="currentOrder.status" :items="statuses" label="Статус"></v-select>
          <v-text-field label="Описание" v-model="currentOrder.description"></v-text-field>
        </v-card-text>
         <v-card-actions>
           <v-spacer><h2 align="center"><v-btn rounded color="indigo darken-2" dark @click="createOrder()">Добавить</v-btn></h2></v-spacer>
         </v-card-actions>
    </v-card>

  </div>
</template>

<script>
    export default {
        name: "AddOrder",
      data: function () {
        return {
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
          statusData: [],
          statuses: []
        }
      },
       mounted () {
    this.$axios
      .get('http://127.0.0.1:8000/status/')
      .then(response => { this.statusData = response; this.updateStatus() })},
    methods:{
          updateStatus(){
                  let data = this.statusData.data
             for (let status of data) {
        this.statuses.push({'text': `${status.status}`, 'value': `${status.id}`})
      }},
        async createOrder() {
            let token = localStorage.getItem('auth_token');
            const response = await fetch('http://127.0.0.1:8000/add_order', {
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization' : "Token "+token
              },
              method: "POST",
              body: JSON.stringify(this.currentOrder)
              });
            console.log(response.data)
            alert("Спасибо за заказ!")
            await this.$router.push({name: "Orders"});
            if (response.status !== 201) {
              alert(JSON.stringify(await response.json(), null, 2));
            }


    }
    }}
</script>

