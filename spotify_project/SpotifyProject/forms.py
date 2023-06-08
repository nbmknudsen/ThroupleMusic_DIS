from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange

from SpotifyProject.queries import get_song_by_name
from SpotifyProject.utils.choices import SongNameChoices, ArtistNameChoices, AlbumNameChoices


class FilterMusicForm(FlaskForm):
    # song = SelectField('Songy',
    #                        choices=SongNameChoices.choices())
    # artist = SelectField('Artist',
    #                    choices=ArtistNameChoices.choices())
    # album = SelectField('Variety',
    #                       choices=AlbumNameChoices.choices())
    song = StringField('Songs')
    submit = SubmitField('Filter')


# class AddProduceForm(FlaskForm):
#     category = SelectField('Category',
#                            validators=[DataRequired()],
#                            choices=ProduceCategoryChoices.choices())
#     item = SelectField('Item (Subcategory)',
#                        validators=[DataRequired()],
#                        choices=ProduceItemChoices.choices())
#     variety = SelectField('Variety',
#                           validators=[DataRequired()],
#                           choices=ProduceVarietyChoices.choices())
#     unit = SelectField('Unit',
#                        validators=[DataRequired()],
#                        choices=ProduceUnitChoices.choices())
#     price = IntegerField('Price',
#                          validators=[DataRequired(), NumberRange(min=0, max=100)])
#     farmer_pk = IntegerField('Farmer',
#                              validators=[DataRequired()],
#                              render_kw=dict(disabled='disabled'))
#     submit = SubmitField('Add produce')

#     def validate_price(self, field):
#         farmer = get_farmer_by_pk(self.farmer_pk.data)
#         if farmer is None:
#             raise ValidationError("You need to be a farmer to sell produce!")
