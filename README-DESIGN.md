# Scrapbook homepage update

This is a first visual pass, not a completed portfolio. The original research, volunteering, hobbies, resume, and login pages are retained. The navigation is shortened to Home / My Work / Community / Little Joys / Resume, with Leadership still accessible at its existing URL but not in the main menu.

## Files changed
- `templates/index.html`: short introduction, three scrapbook-style links, no missing-image or placeholder embeds.
- `templates/base.html`: simpler navigation and dynamic footer year.
- `static/style.css`: appended scrapbook visual styles, mobile and keyboard focus improvements.
- `main.py`: adds `current_year` to the template context; otherwise keeps the previously corrected login implementation.

## Before deploying
- Do not add `.env` or secrets to GitHub.
- Test locally with `FLASK_LOCAL_HTTP=1` in local `.env` only.
- Images and PDFs are absent from the uploaded ZIP. Add approved assets later; public `/static/` files are not private.
- The existing research and hobby pages still have placeholder embeds and links. Do not treat them as finished.
- Review all drafted personal text for accuracy and voice before publication.
