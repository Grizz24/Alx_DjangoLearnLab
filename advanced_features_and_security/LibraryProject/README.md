# Permissions and Groups Setup

## Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

## How to enforce permissions
- Use @permission_required('bookshelf.can_edit', raise_exception=True) in views
- Assign users to groups in the admin or via a management script


# Security Measures
- DEBUG = False in production
- XSS/Clickjacking protections enabled (SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, etc.)
- CSRF and session cookies restricted to HTTPS
- CSRF tokens included in all forms
- All database queries use the Django ORM (no raw SQL)
- Content Security Policy applied via django-csp

HTTPS & Security Setup
----------------------

1) settings.py changes:
 - SECURE_SSL_REDIRECT = True
 - SECURE_HSTS_SECONDS = 31536000
 - SECURE_HSTS_INCLUDE_SUBDOMAINS = True
 - SECURE_HSTS_PRELOAD = True
 - SESSION_COOKIE_SECURE = True
 - CSRF_COOKIE_SECURE = True
 - X_FRAME_OPTIONS = "DENY"
 - SECURE_CONTENT_TYPE_NOSNIFF = True
 - SECURE_BROWSER_XSS_FILTER = True
 - SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

2) Nginx configuration:
 - TLS termination via certbot / Let's Encrypt
 - proxy_set_header X-Forwarded-Proto $scheme
 - Add security headers (HSTS, X-Frame-Options, etc.)

3) Certificates:
 - Certbot: `sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com`

4) Notes:
 - Test thoroughly before enabling HSTS preload.
 - Do not enable SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE on a site without HTTPS.
