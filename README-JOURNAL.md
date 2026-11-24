# Junk journal v2

Copy `templates/` and `static/` into the same folders in your existing project. Keep your working `main.py`, `.env`, `vercel.json`, and `requirements.txt` unchanged.

## Editing doodles
All doodles are local SVGs in `static/images/doodles/`. Open them in VS Code to change `stroke`, `fill`, and the vector paths, or open in Inkscape/Figma to edit visually. No API is used. You can replace these with your own SVG or transparent PNG drawings.

## Adding photos
Suggested layout:
- `static/images/profile/`
- `static/images/research/`
- `static/images/community/`
- `static/images/hobbies/crochet/`
- `static/images/hobbies/journaling/`
- `static/images/hobbies/languages/`
- `static/images/doodles/`
- `static/documents/` (PUBLIC: files here can be accessed without login)

**Privacy:** Vercel's static files are public. Do not put private admissions materials in `static/` until access control for assets is implemented.

## Alignment
The tape and `made with care` annotation are now children of `.polaroid-wrap` and rotate with it. Adjust `.polaroid-wrap .paper-tape` and `.polaroid-wrap .scribble` in `static/style.css` to fine-tune.

## Notes
This update preserves the existing content, navigation, and working login backend. No third-party doodle API or JavaScript library required. Test on mobile and desktop before deploying.
