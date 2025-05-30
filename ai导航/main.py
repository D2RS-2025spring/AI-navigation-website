# 引入必要的库
import streamlit as st
from pathlib import Path
import os
from urllib.parse import urlparse

# 页面基础配置（网页标题、布局）
st.set_page_config(page_title="AI 工具导航", layout="wide")
st.title("🎨 精美 AI 工具导航平台")

# 获取当前脚本所在目录（用于加载本地图标）
BASE_DIR = Path(__file__).parent

# 定义工具分类及其对应工具（包含：名称、链接、图标路径/URL）
tools = {
    "🖼️ 图像生成类 AI": [
        {"name": "豆包", "url": "https://www.doubao.com/", "icon": "image/doubao.jpg"},
        {"name": "Coze", "url": "https://www.coze.com/", "icon": "image/kouzi.jpg"},
        {"name": "讯飞星火", "url": "https://xinghuo.xfyun.cn/", "icon": "https://xinghuo.xfyun.cn/favicon.ico"},
        {"name": "Midjourney", "url": "https://www.midjourney.com/", "icon": "image/mid.jpg"},
        {"name": "Bing Image Creator", "url": "https://www.bing.com/images/create", "icon": "https://www.bing.com/favicon.ico"},
        {"name": "Canva AI", "url": "https://www.canva.cn/features/ai-image-generator/", "icon": "image/canva.jpg"},
    ],
    "💻 代码生成类 AI": [
        {"name": "GitHub Copilot", "url": "https://github.com/features/copilot", "icon": "https://github.githubassets.com/favicons/favicon.png"},
        {"name": "MarsCode", "url": "https://marscode.com/", "icon": "https://marscode.com/favicon.ico"},
        {"name": "CodeWhisperer", "url": "https://aws.amazon.com/codewhisperer/", "icon": "https://a0.awsstatic.com/libra-css/images/site/fav/favicon.ico"},
        {"name": "ChatGPT", "url": "https://chat.openai.com/", "icon": "image/gpt.jpg"},
        {"name": "Tabnine", "url": "https://www.tabnine.com/", "icon": "https://www.tabnine.com/favicon.ico"},
        {"name": "Kite", "url": "https://www.kite.com/", "icon": "image/kit.jpg"},
    ],
    "✍️ 写作辅助类 AI": [
        {"name": "文心一言", "url": "https://yiyan.baidu.com/", "icon": "image/文心一言.jpg"},
        {"name": "豆包", "url": "https://www.doubao.com/", "icon": "image/doubao.jpg"},
        {"name": "橙篇 AI", "url": "https://www.chengpian.com/", "icon": "image/橙篇.jpg"},
        {"name": "通义千问", "url": "https://tongyi.aliyun.com/", "icon": "image/通义.jpg"},
        {"name": "Notion AI", "url": "https://www.notion.so/product/ai", "icon": "https://www.notion.so/images/favicon.ico"},
        {"name": "Writesonic", "url": "https://writesonic.com/", "icon": "image/ws.jpg"},
    ]
}

# 辅助函数：判断给定路径是否为网络链接
def is_url(path: str) -> bool:
    try:
        result = urlparse(path)
        return result.scheme in ("http", "https")
    except:
        return False

# 渲染单个工具卡片（带图标 + 名称 + 链接）
def render_tool_card(tool):
    # 卡片样式容器
    st.markdown(f"""
        <div style="text-align: center; border: 1px solid #eee; border-radius: 12px; padding: 20px; background-color: #f9f9f9; margin-bottom: 15px;">
    """, unsafe_allow_html=True)

    icon_path = tool['icon']

    # 根据是网络图标还是本地图标来选择渲染方式
    if is_url(icon_path):
        # 网络图标：直接用 HTML 加载
        st.markdown(f'<img src="{icon_path}" width="48" style="margin-bottom: 8px;" />', unsafe_allow_html=True)
    else:
        # 本地图标：拼接绝对路径后用 st.image 显示
        local_icon = BASE_DIR / icon_path
        if local_icon.exists():
            st.image(str(local_icon), width=48)
        else:
            st.markdown("⚠ 图标未找到", unsafe_allow_html=True)

    # 名称 + 超链接
    st.markdown(f"""
        <div><a href="{tool['url']}" target="_blank" style="font-size: 16px; text-decoration: none; font-weight: bold; color: #007ACC;">{tool['name']}</a></div>
    </div>
    """, unsafe_allow_html=True)

# 遍历分类，分列显示每个工具
for category, tools_list in tools.items():
    st.markdown(f"### {category}")     # 分类标题
    cols = st.columns(3)               # 每行 3 列工具卡片
    for idx, tool in enumerate(tools_list):
        with cols[idx % 3]:
            render_tool_card(tool)     # 显示卡片
    st.markdown("---")                 # 分类之间添加分割线
