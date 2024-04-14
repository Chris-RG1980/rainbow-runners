from django.contrib.auth.models import User, Group


def create_groups():
    """Create co-ordinators & admin groups """
    Group.objects.get_or_create(name='co-ordinators')
    Group.objects.get_or_create(name='admin')


create_groups()


def assign_users_to_coordinators():
    """Assign users to co-ordinators group"""
    group, created = Group.objects.get_or_create(name='co-ordinators')

    # List of usernames who should be coordinators
    coordinator_usernames = ['Chris', 'stuart']

    for username in coordinator_usernames:
        user = User.objects.get(username=username)
        user.groups.add(group)


def assign_users_to_admin():
    group, created = Group.objects.get_or_create(name='admin')

    # List of usernames who should be admin
    admin_usernames = ['Chris', 'adam1']

    for username in admin_usernames:
        user = User.objects.get(username=username)
        user.groups.add(group)


# assign_users_to_coordinators()
# assign_users_to_admin()
