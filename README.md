# HelloFont · Figma 插件合集

字由（HelloFont）发布于 Figma 社区的插件汇总页，收录全部 11 个插件，按安装量排序。

## 在线访问

启用 GitHub Pages 后访问：

```
https://<你的用户名>.github.io/<仓库名>/
```

## 项目结构

```
docs/                     # GitHub Pages 发布目录
├── index.html            # 主页面（单文件，内联 CSS + JS）
├── .nojekyll             # 关闭 Jekyll 处理
└── assets/
    ├── covers/           # 11 张插件封面图（16:9）
    └── demo/             # 演示 GIF
```

## 功能

- 中英文双语切换（自动检测浏览器语言，localStorage 记忆）
- 按语言/字符集筛选：All / Latin / CJK / Cyrillic / SE Asia / Other
- 11 个插件卡片，按安装量降序排列
- 每张卡片底部提供「Open in Figma」直达链接

## 部署到 GitHub Pages

1. 在仓库 **Settings → Pages** 中，将 **Source** 设为 `Deploy from a branch`
2. Branch 选择 `main`，目录选择 `/docs`
3. 保存后等待 1-2 分钟，即可通过上述链接访问

## 本地预览

```bash
cd docs && python3 -m http.server 8080
# 打开 http://localhost:8080
```

## 相关链接

- Figma 主页：https://www.figma.com/@hellofont
- 字由官网：https://www.hellofont.cn
