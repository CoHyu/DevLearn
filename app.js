const { createApp, ref, computed } = Vue;

createApp({
  setup() {
    const username = ref('');
    const password = ref('');
    const loggedIn = ref(false);
    const message = ref('');
    const error = ref('');

    const canSubmit = computed(() => username.value.trim() !== '' && password.value.trim() !== '');

    function login() {
      error.value = '';
      // 简单模拟认证：用户名 'user' 密码 'pass'
      if (username.value === 'user' && password.value === 'pass') {
        loggedIn.value = true;
        message.value = `欢迎，${username.value}！你已成功登录。这里有一段随意发挥的话：\n在代码的世界里，每一次小小的改动都可能带来无限可能。继续探索，别停下。`;
      } else {
        error.value = '用户名或密码错误。提示：尝试 user / pass';
      }
    }

    function logout() {
      username.value = '';
      password.value = '';
      loggedIn.value = false;
      message.value = '';
      error.value = '';
    }

    return { username, password, loggedIn, message, error, canSubmit, login, logout };
  },
  template: `
    <div class="container">
      <div class="card" v-if="!loggedIn">
        <h2>登录</h2>
        <div class="field">
          <label>用户名</label>
          <input v-model="username" placeholder="输入用户名" />
        </div>
        <div class="field">
          <label>密码</label>
          <input v-model="password" type="password" placeholder="输入密码" />
        </div>
        <div class="actions">
          <button :disabled="!canSubmit" @click="login">登录</button>
        </div>
        <p class="note">测试账号：user / pass</p>
        <p class="error" v-if="error">{{ error }}</p>
      </div>

      <div class="card welcome" v-else>
        <h2>欢迎页面</h2>
        <p class="message" v-html="message.replace(/\n/g, '<br>')"></p>
        <button class="secondary" @click="logout">退出登录</button>
      </div>
    </div>
  `
}).mount('#app');
