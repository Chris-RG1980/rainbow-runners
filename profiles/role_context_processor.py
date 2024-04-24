def user_groups(request):
    is_coordinator = is_in_group(request.user, 'co-ordinators')
    is_admin = is_in_group(request.user, 'admin')
    return {'is_admin': is_admin,
            'is_coordinator': is_coordinator}


def is_in_group(user, group_name):
    """
    Check if the user is in the given group.
    """
    return user.groups.filter(name=group_name).exists()
