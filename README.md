# Arlington Guitar Lessons — landing page

Static site for https://arlingtonguitar.live, hosted free on GitHub Pages.

## Files

- `index.html` — the landing page
- `CNAME` — custom domain for GitHub Pages
- `flyer.py` / `guitar-lessons-flyer.pdf` — printable flyer with tear-off tabs

## Go live

```bash
cd ~/p/arlingtonguitar
gh repo create arlingtonguitar.live --public --source=. --push
```

Then in the repo: Settings → Pages → Deploy from branch → `main` / root.
Add DNS records at your registrar:

- `A` @ → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
- `CNAME` www → `<your-github-username>`.github.io

GitHub provisions HTTPS automatically once DNS resolves.
