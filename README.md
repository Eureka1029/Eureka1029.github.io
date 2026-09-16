# YongHao Ning 的 al-folio 主页

线上地址：<https://eureka1029.github.io/>

本仓库使用 [al-folio](https://github.com/alshedivat/al-folio) 与 Jekyll 构建，并由 GitHub Actions 自动发布到 GitHub Pages。

## 日常写作

1. 用 Obsidian 打开本仓库。
2. 在 `_posts` 中创建 `YYYY-MM-DD-title.md`，也可以使用 `templates/blog-post.md` 模板。
3. 保存后继续编辑；停止修改约 1 分钟后，Obsidian Git 会自动提交、拉取并推送。
4. 推送到 `main` 后，GitHub Actions 会自动构建并发布网站。

自动同步配置位于 `.obsidian/plugins/obsidian-git/data.json`。如果右上角出现 Git 错误提示，先打开 Obsidian 的 Source Control 面板检查冲突或登录状态；不要在多台设备上同时编辑同一篇文章。

## 常用文件

- `_config.yml`：站点名称、网址、功能开关
- `_pages/about.md`：首页与个人介绍
- `_posts/`：博客文章
- `_projects/`：项目卡片
- `_data/socials.yml`：社交链接
- `assets/img/`：图片资源

## 本地预览

安装 Docker Desktop 后，在仓库目录运行：

```powershell
docker compose pull
docker compose up
```

浏览器访问 <http://localhost:8080>。按 `Ctrl+C` 停止预览。

## 手动同步

如果没有使用 Obsidian，可运行：

```powershell
git add -A
git commit -m "content: update site"
git push origin main
```

发布进度位于仓库的 **Actions** 页面；成功后通常还需要几十秒让 Pages 缓存刷新。

