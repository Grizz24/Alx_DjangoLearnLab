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
