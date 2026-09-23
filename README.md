# YongHao Ning 的学术主页

网站：<https://eureka1029.github.io/>

本项目使用 [luost26/academic-homepage](https://github.com/luost26/academic-homepage) 的原始 Jekyll 模板、组件、样式和脚本，已迁入个人资料。上游版本及本地调整见 [docs/template-source.md](docs/template-source.md)。

## 修改后自动生成页面

**修改提交并推送到 GitHub 的 `main` 分支后，GitHub Actions 会自动构建、检查并发布网站。** 仅在本地执行 `git commit` 不会触发远端发布。

普通 Git 操作：

```powershell
git add -A
git commit -m "content: update homepage"
git push origin main
```

也可以直接在 GitHub 网页上编辑文件并提交到 `main`。在 [Actions](https://github.com/Eureka1029/Eureka1029.github.io/actions) 查看构建结果。构建或链接检查失败时，新版本不会部署。

使用 Obsidian 时，打开本目录作为仓库。现有 Obsidian Git 设置为文件修改后约 1 分钟自动提交并同步；Obsidian 必须保持运行，Git 认证和网络也必须可用。单独点击“Commit”时仍需执行“Push”或“Commit-and-sync”。

如果出现 `127.0.0.1:7897` 连接失败，这是 Git 配置的本地代理没有运行，需要启动相应代理或修正 Git 代理配置，推送成功后才会触发发布。

GitHub Pages 的发布源应为 **Settings → Pages → Source → GitHub Actions**。仓库已经有通过 Actions 成功部署的记录。

## 内容编辑位置

| 内容 | 文件或目录 |
| --- | --- |
| 姓名、简介、头像、教育经历、社交链接 | `_data/profile.yml` |
| 导航 | `_data/navigation.yml` |
| 首页模块开关、页脚 | `_data/display.yml` |
| 博客文章 | `_posts/YYYY-MM-DD-title.md` |
| 论文 | `_publications/` |
| 首页新闻 | `_news/`，新闻文字使用 front matter 中的 `title` |
| 项目展示 | `_showcase/`，设置 `show: true` |
| 全站与文章样式 | `assets/css/global.css`、`assets/css/blog.css` |

`templates/` 提供文章、论文、新闻和项目的写作模板。Obsidian 模板中的日期占位符会在插入时替换；直接新建文件时填写真实日期。未来日期的文章会在之后一次构建时才被发布。

文章使用 `layout: blog_post`，旧的 `layout: post` 也兼容。添加文章后，博客列表、RSS 和文章页面会在下次构建时自动更新。论文设置 `selected: true` 后会自动出现在首页。

## 本地预览和检查

安装 Ruby 3.3 和 Bundler 后运行：

```sh
bundle install
bundle exec jekyll serve
```

打开 <http://localhost:4000/>。生产构建与 CI 使用相同命令：

```sh
bundle exec jekyll build --trace
ruby bin/check_site.rb _site
```

发布工作流在 `.github/workflows/deploy.yml`：推送到 `main` 后构建并部署；拉取请求运行构建和检查；也支持手动运行。
