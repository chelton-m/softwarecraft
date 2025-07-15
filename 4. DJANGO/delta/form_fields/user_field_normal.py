from .. import UserProfile  # noqa


def setup_user_field(self, instance):
    user_field = self.fields["user"]
    user = self.request.user if self.request else None

    if user and user.has_perm("business.change_dailyreport"):
        user_field.queryset = UserProfile.objects.filter(is_active=True)
    else:
        if instance:
            user_field.queryset = UserProfile.objects.filter(id=instance.user.id)
            user_field.initial = instance.user
        elif user:
            user_field.queryset = UserProfile.objects.filter(id=user.id)
            user_field.initial = user

        user_field.widget.attrs.update({"disabled": True, "readonly": True})
        user_field.required = False
