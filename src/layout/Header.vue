<script>
import { defineComponent, ref } from 'vue';
import { SettingOutlined } from '@ant-design/icons-vue';
export default defineComponent({
  setup() {
    const current = ref(['mail']);
    return {
      current,
    };
  },
  components: {
    SettingOutlined,
  },
});
</script>


<template>
  <div class="absolute top-5 right-12"> 
    <a-menu v-model:selectedKeys="current" mode="horizontal">
        <a-menu-item key="swift">
          <a href="/swift" rel="noopener noreferrer">
            Swift
          </a>
        </a-menu-item>
        <a-menu-item key="vue">
          <a href="/vue" rel="noopener noreferrer">
            Vue
          </a>
        </a-menu-item>
        <a-menu-item key="aws">
          <a href="/aws" rel="noopener noreferrer">
            AWS
          </a>
        </a-menu-item>
        <a-menu-item key="python">
          <a href="/python" rel="noopener noreferrer">
            Python
          </a>
        </a-menu-item>
    </a-menu>
   </div>
</template>
