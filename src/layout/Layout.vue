<script>
import Header from "@/layout/Header.vue"
import Footer from "@/layout/Footer.vue"

export default {
    components: {
        Header,
        Footer
    }
}
</script>

<template>
    <header class="bg-blue-50 shadow">
      <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8 h-36">
        <h1 class="text-3xl font-bold leading-tight text-gray-900"><Header></Header></h1>
      </div>
    </header>
    <main class="bg-white shadow">
      <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        <router-view />
      </div>
    </main>
    <footer class="bg-gray-80 shadow">
      <div class="max-w-7xl h-56 mx-auto py-6 px-4 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold leading-tight text-gray-900"><Footer></Footer></h1>
      </div>
    </footer>
</template>