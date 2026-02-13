---
layout: default
title: 搜索
---

<div class="search-container">
  <div class="search-box">
    <input type="text" id="search-input" placeholder="搜索标题..." autocomplete="off">
    <button id="search-button">🔍 搜索</button>
  </div>
  
  <div id="search-results">
    <p class="search-hint">输入关键词搜索标题</p>
  </div>
</div>

<style>
.search-container {
  max-width: 900px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.search-box {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 2rem;
}

#search-input {
  flex: 1;
  padding: 0.75rem 1rem;
  font-size: 1rem;
  border: 2px solid #159957;
  border-radius: 4px;
  outline: none;
}

#search-input:focus {
  border-color: #155799;
  box-shadow: 0 0 0 3px rgba(21, 153, 87, 0.1);
}

#search-button {
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  background: linear-gradient(120deg, #155799, #159957);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s;
}

#search-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

#search-results {
  min-height: 200px;
}

.search-hint {
  text-align: center;
  color: #666;
  font-size: 1.1rem;
  padding: 3rem 0;
}

.search-result-item {
  padding: 1.5rem;
  margin-bottom: 1rem;
  background: #f6f8fa;
  border-left: 4px solid #159957;
  border-radius: 4px;
  transition: all 0.3s;
}

.search-result-item:hover {
  background: #e1e4e8;
  transform: translateX(4px);
}

.search-result-title {
  font-size: 1.3rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.search-result-title a {
  color: #155799;
  text-decoration: none;
}

.search-result-title a:hover {
  color: #159957;
  text-decoration: underline;
}

.search-result-excerpt {
  color: #586069;
  line-height: 1.6;
  margin-bottom: 0.5rem;
}

.search-result-url {
  font-size: 0.9rem;
  color: #159957;
}

.no-results {
  text-align: center;
  padding: 3rem;
  color: #666;
}

.loading {
  text-align: center;
  padding: 2rem;
  color: #159957;
}

mark {
  background-color: #fff3cd;
  padding: 0 0.2em;
  border-radius: 2px;
}
</style>

<script src="https://unpkg.com/lunr/lunr.js"></script>
<script>
(function() {
  let searchIndex;
  let searchData;
  
  // 加载搜索数据
  fetch('{{ "/search.json" | relative_url }}')
    .then(response => response.json())
    .then(data => {
      searchData = data;
      
      // 构建搜索索引（只搜索标题）
      searchIndex = lunr(function() {
        this.ref('url');
        this.field('title'); // 只索引标题字段
        
        // 添加中文分词支持
        this.pipeline.remove(lunr.stemmer);
        this.searchPipeline.remove(lunr.stemmer);
        
        data.forEach(doc => {
          this.add(doc);
        });
      });
      
      console.log('搜索索引已加载，共 ' + data.length + ' 个页面');
    })
    .catch(error => {
      console.error('加载搜索索引失败:', error);
      document.getElementById('search-results').innerHTML = 
        '<p class="no-results">搜索功能加载失败，请刷新页面重试</p>';
    });
  
  // 执行搜索
  function performSearch(query) {
    if (!searchIndex || !searchData) {
      document.getElementById('search-results').innerHTML = 
        '<p class="loading">搜索索引加载中...</p>';
      return;
    }
    
    if (!query || query.trim() === '') {
      document.getElementById('search-results').innerHTML = 
        '<p class="search-hint">请输入搜索关键词</p>';
      return;
    }
    
    document.getElementById('search-results').innerHTML = 
      '<p class="loading">搜索中...</p>';
    
    try {
      // 执行搜索
      const results = searchIndex.search(query);
      
      if (results.length === 0) {
        document.getElementById('search-results').innerHTML = 
          '<p class="no-results">没有找到相关内容，请尝试其他关键词</p>';
        return;
      }
      
      // 显示结果
      let html = '<p style="margin-bottom: 1rem; color: #666;">找到 ' + results.length + ' 个相关结果</p>';
      
      results.slice(0, 20).forEach(result => {
        const doc = searchData.find(d => d.url === result.ref);
        if (doc) {
          // 高亮标题中的关键词
          let title = doc.title || '无标题';
          const regex = new RegExp('(' + query.split(/\s+/).join('|') + ')', 'gi');
          title = title.replace(regex, '<mark>$1</mark>');
          
          // 显示摘要（不高亮）
          let excerpt = doc.excerpt || doc.content.substring(0, 200);
          
          html += `
            <div class="search-result-item">
              <div class="search-result-title">
                <a href="${doc.url}">${title}</a>
              </div>
              <div class="search-result-excerpt">${excerpt}...</div>
              <div class="search-result-url">${doc.url}</div>
            </div>
          `;
        }
      });
      
      document.getElementById('search-results').innerHTML = html;
    } catch (error) {
      console.error('搜索出错:', error);
      document.getElementById('search-results').innerHTML = 
        '<p class="no-results">搜索出错，请重试</p>';
    }
  }
  
  // 绑定搜索事件
  document.getElementById('search-button').addEventListener('click', function() {
    const query = document.getElementById('search-input').value;
    performSearch(query);
  });
  
  document.getElementById('search-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      const query = this.value;
      performSearch(query);
    }
  });
  
  // 从 URL 参数获取搜索词
  const urlParams = new URLSearchParams(window.location.search);
  const queryParam = urlParams.get('q');
  if (queryParam) {
    document.getElementById('search-input').value = queryParam;
    // 等待索引加载后执行搜索
    setTimeout(() => performSearch(queryParam), 500);
  }
})();
</script>
