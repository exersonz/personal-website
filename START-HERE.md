# Fast scrapbook update

This is a **visual/content prototype** built from your earlier Junk Journal V2. It does **not** include any real photos or claim the placeholders are real work.

## Apply
1. On your existing Git testing branch, back up your work.
2. Copy `templates/` and `static/journal.css` into your project, plus `static/images/doodles/` if missing. **Keep your currently working `main.py`, `vercel.json`, `requirements.txt`, and `.env` unchanged.**
3. Start locally, check Home, My Work, Community, Little Joys, Resume and login/logout.
4. Don't merge to main until the preview is tested.

## Fill photos quickly
The placeholders display a recommended filename and a clickable **media idea** note. Put a photo in `static/images/work/`, `static/images/community/`, or `static/images/joys/` as suggested. **The image automatically appears** when you add the file at the displayed path. Refresh your browser. No HTML editing needed. The placeholder remains visible until a matching file exists.

For photos use jpg/webp and crop 4:3. For logos use PNG or SVG with transparent backgrounds. Keep captions to one sentence. You can remove cards you don't want by deleting the `{{ card(...) }}` call in the relevant page.

## Privacy
Anything under `static/` is publicly addressable, even when the page requires login. Do not add sensitive PDFs, private documents, or identifiable workshop participant photos without permission. This update does not fix that issue.

## Customize
Change colors, paper backgrounds, rotations, and tape in `static/journal.css`. Editable cat SVGs live in `static/images/doodles/`. No image API is needed.
