from django import forms


class ColorPickerWidget(forms.TextInput):
    input_type = 'color'


class CategorySelectWidget(forms.CheckboxSelectMultiple):
    template_name = 'widgets/checkbox_categories.html'

    def optgroups(self, name, value, attrs=None):
        from .snippets import Category
        categories = Category.objects.all().select_related()

        groups = []
        has_selected = False

        for index, category in enumerate(categories):
            subgroup = []
            group_name = category.name
            subindex = 0
            choices = []

            for term in category.terms.all():
                choices.append((term.pk, term.name))

            groups.append((group_name, subgroup, index))

            for subvalue, sublabel in choices:
                selected = (
                    str(subvalue) in value and
                    (not has_selected or self.allow_multiple_selected)
                )
                has_selected |= selected
                subgroup.append(self.create_option(
                    name, subvalue, sublabel, selected, index,
                    subindex=subindex, attrs=attrs,
                ))
                if subindex is not None:
                    subindex += 1
        return groups
