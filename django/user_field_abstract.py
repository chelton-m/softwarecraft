# apps/common/forms/mixins.py

class FreezeUserMixin:
    def handle_user_field(self, user, instance=None, permission="change"):
        model = self._meta.model
        perm_codename = f"{permission}_{model._meta.model_name}"

        if user.has_perm(f"{model._meta.app_label}.{perm_codename}"):
            self.fields["user"].queryset = model._meta.get_field("user").related_model.objects.filter(is_active=True)
        else:
            if instance:
                self.fields["user"].queryset = model._meta.get_field("user").related_model.objects.filter(id=instance.user.id)
                self.fields["user"].initial = instance.user
            else:
                self.fields["user"].queryset = model._meta.get_field("user").related_model.objects.filter(id=user.id)
                self.fields["user"].initial = user

            self.fields["user"].widget.attrs.update({"disabled": True, "readonly": True})
            self.fields["user"].required = False

    def set_user_on_clean(self, cleaned_data, instance, request_user):
        if self.fields["user"].widget.attrs.get("disabled"):
            cleaned_data["user"] = instance.user if instance and instance.pk else request_user