# HelloFont · Figma 插件合集页

字由（HelloFont）发布于 Figma 社区的插件汇总页，收录 11 个插件，支持**中文 / English / 日本語**三语切换。

- 线上预览：https://had2mhahdshad.github.io/hellofont-figma-plugins/
- 线上部署：GitHub Pages（`main` 分支 `/docs` 目录，推送后约 1–2 分钟生效）

---

## 快速开始

```bash
git clone https://github.com/had2mhahdshad/hellofont-figma-plugins.git
cd hellofont-figma-plugins

# 本地预览（任选一种）
cd docs && python3 -m http.server 8080
# 然后打开 http://localhost:8080
```

**没有依赖、没有构建步骤。** 直接改 `docs/index.html` 保存，刷新浏览器即可看到效果。

---

## 项目结构

```
.
├── README.md                 # 本文件
├── scripts/
│   └── build-single.py       # 可选：把 index.html 打包成自包含单文件
└── docs/                     # ← GitHub Pages 发布目录（只发布这里）
    ├── index.html            # ★ 全部代码都在这一个文件里
    ├── .nojekyll             # 关闭 Jekyll，勿删
    └── assets/
        ├── covers/           # 11 张插件封面（16:9，800×450）
        └── demo/             # 演示 GIF / 视频占位
```

> `docs/index.html` 是**单文件应用**：内联 CSS + JS + 数据，改这一个文件就够了。

---

## 代码结构（`docs/index.html`，共约 650 行）

| 行号 | 区块 | 说明 |
|---|---|---|
| 21–217 | `<style>` | 全部 CSS。含设计变量、组件样式、响应式断点 |
| 221–231 | 导航栏 | |
| 233–263 | Hero 首屏 | 含演示视频占位框 |
| 265–276 | 插件列表区 | 标题 + 筛选栏 + 卡片网格容器 |
| 277–286 | 底部 CTA | |
| 287–316 | 页脚 | |
| 318+ | `<script>` | 数据 + 渲染逻辑 |
| 322 | `CONFIG` | 品牌名、邮箱、外链等全局配置 |
| **332** | **`I18N`** | **三语文案字典（`zh` / `en` / `ja`）** |
| **417** | **`FILTERS`** | 筛选分类（All / Latin / CJK / Cyrillic / SE Asia / Other） |
| **431** | **`PLUGINS`** | **11 个插件数据（名称、描述、链接、封面…）** |
| 562–575 | 语言逻辑 | `LANGS` / `LANG_LABEL` / `detectLang()` |
| 606 | `cardHTML()` | 卡片 HTML 模板 |

---

## 常见微调怎么做

### 改文案（中/英/日）

编辑 `I18N`（第 332 行起）。三个语言块**字段必须一一对应**：

```js
const I18N = {
  zh:{ heroSub:"…", navPlugins:"全部插件", … },
  en:{ heroSub:"…", navPlugins:"Plugins",  … },
  ja:{ heroSub:"…", navPlugins:"プラグイン", … }
};
```

- 文案里可以写 HTML：`heroTitle` 用了 `<br/>` 和 `<span class="grad-text">…</span>`（渐变文字）
- **不要删字段、不要改字段名**，否则页面会显示 `undefined`
- 新增语言：在 `I18N` 加一个语言块 + 把语言代码加进 `LANGS`（第 562 行）+ `LANG_LABEL`（第 565 行）

### 加 / 改插件

编辑 `PLUGINS`（第 431 行起），复制一个现有对象改字段即可：

```js
{
  name:"插件名", type:"plugin", family:"lat", isNew:false,
  variant:{zh:"…", en:"…", ja:"…"},        // 卡片副标题（单行）
  description:{zh:"…", en:"…", ja:"…"},    // 卡片描述（显示 2 行，超出截断）
  figmaUrl:"https://www.figma.com/community/plugin/…",
  installs:184, likes:19, pricing:"paid",
  priceLabel:{zh:"…", en:"…", ja:"…"},     // 当前页面未展示
  tags:{zh:[…], en:[…], ja:[…]},           // 当前页面未展示
  accent:"linear-gradient(135deg,#5b4bff,#9a5bff)",  // 封面加载前的占位渐变
  mono:"A", flag:"EN",                      // flag = 封面右上角语言徽章
  cover:"assets/covers/cover_xxx.jpg"
}
```

- 卡片**按 `installs` 自动降序排列**，不用手动排序
- `family` 决定筛选归属：`lat` / `cjk` / `cyr` / `sea` / `other`
- 换新封面：把图片放进 `assets/covers/`，改 `cover` 路径即可（建议 800×450，16:9）

### 改样式

全在 `<style>` 里。几个关键类：

| 类 | 作用 |
|---|---|
| `.hero h1` | 首屏主标题（**宽度刻意突破了内容区，见下方注意**） |
| `.filters` | 筛选按钮行 |
| `.grid` / `.card` | 卡片网格与卡片 |
| `.card-body .desc` | 卡片描述（`-webkit-line-clamp:2` 限制 2 行） |
| `.card-open` | 卡片右下角「Open in Figma」按钮 |
| `.cta-band` | 底部 CTA 横幅 |

设计变量（颜色、圆角、最大宽度）在 `:root` 里，改配色优先动这里。

### 替换演示视频占位

Hero 里的占位框（第 233 行附近）注释已经写明：把视频命名为 `assets/demo/hero-video.mp4`，或替换 `<video>` 节点即可。占位提示文案是 `I18N.demoPhT` / `demoPhS`。

---

## ⚠️ 改之前请知道的 5 个坑

这些是之前踩过并修好的，**改动时别破坏**：

1. **整卡可点靠 CSS 实现，别删**
   ```css
   .card-body .card-open::after{content:"";position:absolute;inset:0;z-index:1}
   ```
   这行让卡片任意位置都能点击跳转（第 149 行）。删掉就只有小按钮能点。

2. **`.hero h1` 故意比内容区宽**
   用了 `width:min(1180px,calc(100vw - 80px))` + `left:50%` + `translateX(-50%)` 突破 `.wrap` 的 1120px 限制。
   **原因**：英文首行需要 1167px，不突破会在桌面端折成 3 行。别"顺手"改成 `max-width:1120px`。

3. **`.filters` 必须是 `flex-wrap:wrap`**
   原来是 `nowrap`，导致 6 个按钮在手机上挤成一行、整页横向溢出 434px。

4. **三语布局有专门的响应式断点**
   `@media(max-width:1100px)` 调 H1 字号、`(max-width:720px/380px)` 收紧导航、`(max-width:640px)` 移动端 CTA 纵向排列。改移动端样式时确认不会让日文/英文溢出。

5. **卡片点击热区依赖 `.card{position:relative}`**
   如果改了 `.card` 的 position，点击热区会失效。

---

## 部署

推送到 `main` 分支即自动部署：

```bash
git add .
git commit -m "说明改动"
git push origin main
```

GitHub Pages 会在 1–2 分钟内重新构建。可在仓库 **Settings → Pages** 查看构建状态。

> 只发布 `docs/` 目录，仓库根目录的文件（README、scripts）不会上线。

---

## 可选：生成自包含单文件版

如果要把页面作为**单个 HTML 文件**交付（图片内嵌 base64，可直接双击打开、无需 assets 目录）：

```bash
python3 scripts/build-single.py
# 输出：docs/index_single.html
```

注意：这是**生成物**，不要直接编辑它，也不要提交进仓库（改了 `index.html` 后重新生成即可）。

---

## 验证改动是否安全

改完后建议在以下尺寸 × 三语快速过一遍，确认没有横向溢出和布局错乱：

桌面 `1440 / 1280 / 1024`，移动 `430 / 390 / 375`

重点看：Hero 标题行数（桌面应为 2 行）、按钮文字是否完整、同行卡片是否等高、页面能否左右滑动（不该能）。
