# Yonghao Ning 的博客

网站地址为 <https://eureka1029.github.io/>。站点使用 Hugo 和 [PaperMod](https://github.com/adityatelange/hugo-PaperMod/)，主题随仓库提供。固定版本见 [主题来源](docs/template-source.md)。

## 本地预览

安装 Hugo 0.169.0 后，在仓库目录运行以下命令。

```sh
hugo server --buildDrafts
```

打开 <http://localhost:1313/>。发布前可运行生产构建和页面链接检查。

```sh
hugo --environment production --gc --minify
python bin/check_site.py public
```

## 编辑内容

| 内容 | 文件或目录 |
| --- | --- |
| 首页简介、联系方式和导航 | `hugo.yaml` |
| 教育经历和动态 | `content/about.md` |
| 博客文章 | `content/blog/` |
| 论文 | `content/publications/` |
| 项目 | `content/showcase/` |
| 静态图片 | `static/assets/img/` |

在 Obsidian 里可以继续使用 `templates/` 下的写作模板。也可以用 `hugo new content blog/my-post.md` 创建草稿，写完后把 `draft` 改为 `false`。文章网址为 `/blog/年份/文件名/`，设置 `slug` 可以自定义最后一段。

## 发布

推送到 GitHub 的 `main` 分支后，[GitHub Actions](https://github.com/Eureka1029/Eureka1029.github.io/actions) 会构建、检查并发布到 GitHub Pages。拉取请求会运行同样的构建和检查。Pages 的发布源设置为 **GitHub Actions**。
