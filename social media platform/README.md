# Social Media Platform (Mini App)

Create a mini social media app.

Features to implement:
- User profiles
- Posts & comments
- Like/follow system

Frontend: HTML, CSS, JavaScript
Backend: Django
Database: SQLite

Acceptance criteria:
- Users can register/login and have a profile
- Users can create posts, comment, like posts
- Users can follow/unfollow others
- Basic frontend pages for feed, profile, and post

## Local setup (quick)
1. python -m venv .venv
2. .venv\Scripts\activate
3. pip install -r backend/requirements.txt
4. cd backend
5. python manage.py migrate
6. python manage.py runserver

If you'd like, I can continue by implementing the initial models and running migrations now.

## Usage & development
1. Create a virtual environment and activate it:
   - python -m venv .venv
   - .venv\Scripts\activate
2. Install dependencies:
   - pip install -r backend/requirements.txt
3. Run migrations:
   - cd backend
   - python manage.py makemigrations
   - python manage.py migrate
4. Seed sample data (creates users alice and bob with password "password"):
   - python manage.py seed
5. Run server:
   - python manage.py runserver
6. Access:
   - Frontend: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/ (create superuser with `python manage.py createsuperuser`)

## Notes
- SQLite is used by default (`db.sqlite3`).
- Basic features implemented: registration/login, profiles, create posts, comment, like, follow/unfollow.  
- Basic unit tests added in `backend/core/tests.py` and they pass.

If you'd like, I can add Docker support, CI, or expand frontend UI next.

## Docker (development)
Build the image and start the container:

1. docker compose build
2. docker compose up -d

The web service will be available at http://127.0.0.1:8000/ and uses the included SQLite database file.

Note: the Dockerfile uses `gunicorn` for serving the Django app in the container.

## API (REST)
- Token auth: POST /api-token-auth/ with `username` + `password` returns `token`.
- Posts: GET/POST /api/posts/ (POST requires token)
- Comments: GET/POST /api/comments/ (POST requires token)
- Profiles: GET /api/profiles/
- Likes: GET/POST /api/likes/ (POST requires token)

Example: use the token header `Authorization: Token <token>` to make authenticated requests.
