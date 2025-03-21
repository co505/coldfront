
def add_project_status_choices(apps, schema_editor):
    ProjectStatusChoice = apps.get_model('project', 'ProjectStatusChoice')

    for choice in ['New', 'Active', 'Archived', ]:
        ProjectStatusChoice.objects.get_or_create(name=choice)


def add_project_user_role_choices(apps, schema_editor):
    ProjectUserRoleChoice = apps.get_model('project', 'ProjectUserRoleChoice')

    for choice in ['User', 'Manager', ]:
        ProjectUserRoleChoice.objects.get_or_create(name=choice)


def add_project_user_status_choices(apps, schema_editor):
    ProjectUserStatusChoice = apps.get_model('project', 'ProjectUserStatusChoice')

    for choice in ['Active', 'Pending Remove', 'Denied', 'Removed', ]:
        ProjectUserStatusChoice.objects.get_or_create(name=choice)


def add_manual_institution_choice(project, form):
    project.institution = form.cleaned_data['institution']


def add_automated_institution_choice(project, institution_map: dict):

    """
    Adding automated institution choices to a project. Taking PI email of current project
    and comparing to domain key from institution map.
    :param project: Project to add automated institution choices to.
    :param institution_map: Dictionary of institution keys, values.

    """

    email = project.pi.email

    try:
        split_domain = email.split('@')
    except IndexError:
        split_domain = None

    try:
        direct_dict_match = institution_map.get(split_domain[1])
    except IndexError:
        direct_dict_match = None


    if direct_dict_match:
        project.institution = direct_dict_match
    else:
        for key, value in institution_map.items():
            if key in split_domain[1]:
                project.institution = value
