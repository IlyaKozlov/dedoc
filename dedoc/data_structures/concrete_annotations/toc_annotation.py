from flask_restx import fields, Api, Model

from dedoc.data_structures.annotation import Annotation


class TocAnnotation(Annotation):

    name = "toc"
    valid_values = ["True", "False"]

    def __init__(self, start: int, end: int, value: str):
        try:
            bool(value)
        except ValueError:
            raise ValueError("the value of toc annotation should be True or False")
        super().__init__(start=start, end=end, name=TocAnnotation.name, value=value)

    @staticmethod
    def get_api_dict(api: Api) -> Model:
        return api.model('TocAnnotation', {
            'start': fields.Integer(description='annotation start index', required=True, example=0),
            'end': fields.Integer(description='annotation end index', required=True, example=4),
            'value': fields.String(description='indicator if the line is included in toc or not',
                                   required=True,
                                   example="True",
                                   enum=TocAnnotation.valid_values)
        })
