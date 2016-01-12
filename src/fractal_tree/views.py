from django.shortcuts import render
from django.views import generic
from django import forms

from crispy_forms.helper import *
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


def index(request):
    treeform = FractalTreeForm()
    params = [4,10,17, 30, [2,-3,4,-5]]
    if request.method == 'POST':
        params = map(request.POST.__getitem__, 
            ['iterations', 'trapezoidal_sections', 'linear_coeff', 'quadratic_coeff'])
        params = map(lambda x: int(x), params)
        params.append( map(lambda x: int(x), request.POST['children'].strip(' ').split(',')))

    return render(request, "fractal_tree/fractal-space.html", {'form': treeform, 'params': params})


# FRACTAL_DIMENSION = 4
# TRAPEZOIDAL_SECTIONS = 10
# CHILDREN = [3, -7]
# DEGREE1_COEFF = 17
# DEGREE2_COEFF = 30

class FractalTreeForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        # self.helper.form_id = 'fractal_tree_form'
        # self.helper.form_class = 'blueForms'
        # self.helper.form_method = 'post'
        # self.helper.form_action = 'index'
        # self.helper.layout = Layout(
        #     Fieldset(
                
        #         'iterations', 'trapezoidal_sections', 'children', 'linear_coeff', 'quadratic_coeff'
        #     ),
        #     ButtonHolder(
        #         Submit('submit', 'Submit', css_class='button white')
        #     )
        # )

        self.helper.add_input(Submit('submit', 'Submit'))
        super(FractalTreeForm, self).__init__(*args, **kwargs)

    iterations = forms.IntegerField(
        label = "Iterations",
        required = True,
        initial = 4,
        min_value = 2,
        max_value = 10,
        )

    trapezoidal_sections = forms.IntegerField(
        label = "Trapezoidal sections",
        required = True,
        initial = 10,
        min_value = 2,
        max_value = 100,
        )

    children = forms.CharField(
        label = "Branch structure",
        required = True,
        initial = "2, -4, 6",
        )

    linear_coeff = forms.IntegerField(
        label = "Linear deviation",
        required = True,
        initial = 17,
        min_value = 2,
        max_value = 1000,
        )

    quadratic_coeff = forms.IntegerField(
        label = "Quadratic deviation",
        required = True,
        initial = 30,
        min_value = 2,
        max_value = 1000,
        )



#class index(generic.TemplateView):
#    template_name = "about.html" #"fractal_tree/fractal-space.html"
