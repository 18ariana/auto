<template>
  <v-app id="app">
      <v-card class="overflow-hidden">
        <v-app-bar
          color="indigo darken-2"
          dark
          shrink-on-scroll
          scroll-target="#scrolling-techniques"
        >

                <v-toolbar-title class="headline">
                  <v-icon>mdi-car-side</v-icon>  Всё для Вашего авто <v-icon>mdi-car-side</v-icon>
                </v-toolbar-title>

          <v-spacer></v-spacer>
          <v-btn icon @click="goAddOrder()">
        <v-icon>mdi-plus-one</v-icon>
      </v-btn>


        </v-app-bar>
      </v-card>
    <router-view/>
  </v-app>
</template>
<script>
export default {
  name: 'App',
  methods: {
    goAddOrder(){
      this.$router.push({name:"AddOrder"})
    }
  }
  }
</script>

