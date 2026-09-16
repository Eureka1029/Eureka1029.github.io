# YongHao Ning's al-folio website

Live site: <https://eureka1029.github.io/>

This repository uses [al-folio](https://github.com/alshedivat/al-folio), Jekyll, GitHub Actions, and GitHub Pages.

## Writing

1. Open this repository as an Obsidian vault.
2. Create a `YYYY-MM-DD-title.md` file in `_posts`, or use `templates/blog-post.md`.
3. Save your changes. After about one minute without further edits, Obsidian Git automatically commits, pulls, and pushes.
4. A push to `main` triggers GitHub Actions and publishes the updated website.

The automatic synchronization settings are stored in `.obsidian/plugins/obsidian-git/data.json`. If Obsidian reports a Git error, check the Source Control panel for authentication problems or conflicts. Avoid editing the same article on multiple devices at the same time.

## Main files

- `_config.yml`: site metadata and feature settings
- `_pages/about.md`: homepage and education
- `_posts/`: articles
- `_projects/`: projects
- `_data/socials.yml`: social links
- `assets/img/`: images

## Local preview

After installing Docker Desktop, run:

```powershell
docker compose pull
docker compose up
```

Open <http://localhost:8080>. Press `Ctrl+C` to stop the preview.

## Manual synchronization

If you are not using Obsidian, run:

```powershell
git add -A
git commit -m "content: update site"
git push origin main
```

Deployment progress is available on the repository's **Actions** page. GitHub Pages may take several additional seconds to refresh after a successful deployment.
