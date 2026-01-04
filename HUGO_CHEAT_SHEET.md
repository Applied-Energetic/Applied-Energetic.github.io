# Hugo 常用命令速查表

这里列出了管理 Hugo 博客时最常用的命令。

## 1. 启动开发服务器 (本地预览)

在本地启动 Web 服务器，实时预览修改效果。

```bash
# 启动服务器 (默认不包含草稿)
hugo server

# 启动服务器 (包含草稿内容 -D / --buildDrafts)
hugo server -D
```

默认地址: http://localhost:1313/

## 2. 创建新内容

快速创建新的博客文章或页面。

```bash
# 创建一篇新文章 (路径相对于 content 目录)
hugo new post/my-new-post.md

# 创建一个新页面
hugo new about.md
```

## 3. 构建站点 (发布)

生成静态文件到 `public` 目录，用于部署到 GitHub Pages 或其他服务器。

```bash
# 构建站点
hugo

# 构建站点 (包含草稿)
hugo -D

# 指定输出目录 (例如输出到 docs 目录)
hugo -d docs
```

## 4. 其他常用命令

```bash
# 查看 Hugo 版本
hugo version

# 检查配置 (查看当前生效的配置)
hugo config
```

## 5. 常见参数说明

- `-D`: 包含草稿 (`draft: true` 的文章)。
- `-F`: 包含未来日期的文章。
- `-E`: 包含已过期的文章。
- `--gc`: 构建后运行垃圾回收 (清理未使用的缓存)。
- `--cleanDestinationDir`: 构建前清理目标目录 (慎用)。

## 自定义

### 图标
https://tabler.io/icons
