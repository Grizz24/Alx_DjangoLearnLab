# Permissions and Groups Setup

## Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

## How to enforce permissions
- Use @permission_required('bookshelf.can_edit', raise_exception=True) in views
- Assign users to groups in the admin or via a management script
