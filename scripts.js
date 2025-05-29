<script>
  // 找到所有收藏按钮，绑定点击事件
  document.querySelectorAll('.favorite-btn').forEach(btn ={
    btn.addEventListener('click', e => {
      e.stopPropagation();   // 阻止点击冒泡，防止触发卡片的其它点击事件
      btn.classList.toggle('active');  // 切换 active 类，控制颜色变化
    })
  });
</script>

