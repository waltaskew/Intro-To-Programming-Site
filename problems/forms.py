from django import forms

class QuestionForm(forms.Form):
    """Form for validating simple question and answers.
    """
    answer = forms.CharField(max_length=255)

    def clean_answer(self):
        """Check if the value is the answer to the form's problem.
        """
        answer = self.cleaned_data['answer']
        if answer != self.answer:
            message = 'Nope.  %s is not the right answer.' % answer
            raise forms.ValidationError(message)
