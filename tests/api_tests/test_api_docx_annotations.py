from typing import List

from tests.api_tests.abstrac_api_test import AbstractTestApiDocReader


class TestApiDocxAnnotations(AbstractTestApiDocReader):

    def __check_annotation_in(self, target_annotation: dict, annotations: List[dict]):
        filtered = [annotation for annotation in annotations if annotation["name"] == target_annotation["name"]]
        self.assertIn(target_annotation, filtered)

    def test_example_1(self):
        result = self._send_request("annotation_docx/example_1.docx")['content']['structure']['subparagraphs']
        annotations = [subparagraph['annotations'] for subparagraph in result]

        # bold, italic, underlined
        self.__check_annotation_in({'start': 0, 'end': 12, 'name': 'italic', 'value': 'True'}, annotations[1])
        self.__check_annotation_in({'start': 0, 'end': 10, 'name': 'bold', 'value': 'True'}, annotations[2])
        self.__check_annotation_in({'start': 0, 'end': 16, 'name': 'underlined', 'value': 'True'}, annotations[3])
        self.__check_annotation_in({'start': 0, 'end': 6, 'name': 'italic', 'value': 'True'}, annotations[4])
        self.__check_annotation_in({'start': 8, 'end': 13, 'name': 'bold', 'value': 'True'}, annotations[5])
        self.__check_annotation_in({'start': 0, 'end': 20, 'name': 'bold', 'value': 'True'}, annotations[6])
        self.__check_annotation_in({'start': 5, 'end': 20, 'name': 'underlined', 'value': 'True'}, annotations[6])
        # alignment

        self.__check_annotation_in({'start': 0, 'end': 10, 'name': 'alignment', 'value': 'left'}, annotations[7])
        self.__check_annotation_in({'start': 0, 'end': 14, 'name': 'alignment', 'value': 'center'}, annotations[8])
        self.__check_annotation_in({'start': 0, 'end': 11, 'name': 'alignment', 'value': 'right'}, annotations[9])
        self.__check_annotation_in({'start': 0, 'end': 29, 'name': 'alignment', 'value': 'both'}, annotations[10])
        # indent
        self.__check_annotation_in({'start': 0, 'end': 12, 'name': 'indentation', 'value': '0'}, annotations[11])
        self.__check_annotation_in({'start': 0, 'end': 11, 'name': 'indentation', 'value': '720'}, annotations[12])
        self.__check_annotation_in({'start': 0, 'end': 11, 'name': 'indentation', 'value': '1440'}, annotations[13])

    def test_example_2(self):
        result = self._send_request("annotation_docx/example_2.docx")['content']['structure']['subparagraphs']
        annotations = [subparagraph['annotations'] for subparagraph in result]

        # heading, italic, bold, underlined
        self.__check_annotation_in({'start': 0, 'end': 31, 'name': 'italic', 'value': 'True'}, annotations[3])
        self.__check_annotation_in({'start': 0, 'end': 31, 'name': 'style', 'value': 'heading 4'}, annotations[3])
        self.__check_annotation_in({'start': 0, 'end': 29, 'name': 'italic', 'value': 'True'}, annotations[8])
        self.__check_annotation_in({'start': 0, 'end': 29, 'name': 'style', 'value': 'heading 9'}, annotations[8])
        self.__check_annotation_in({'start': 66, 'end': 73, 'name': 'italic', 'value': 'True'}, annotations[35])
        self.__check_annotation_in({'start': 75, 'end': 89, 'name': 'bold', 'value': 'True'}, annotations[35])
        self.__check_annotation_in({'start': 91, 'end': 111, 'name': 'underlined', 'value': 'True'}, annotations[35])
        self.__check_annotation_in({'start': 0, 'end': 153, 'name': 'size', 'value': '14.0'}, annotations[35])
        self.__check_annotation_in({'start': 153, 'end': 175, 'name': 'size', 'value': '20.0'}, annotations[35])
        self.__check_annotation_in({'start': 183, 'end': 199, 'name': 'size', 'value': '11.0'}, annotations[35])
        # alignment
        self.__check_annotation_in({'start': 0, 'end': 46, 'name': 'alignment', 'value': 'right'}, annotations[42])
        self.__check_annotation_in({'start': 0, 'end': 40, 'name': 'alignment', 'value': 'center'}, annotations[43])
        self.__check_annotation_in({'start': 0, 'end': 160, 'name': 'alignment', 'value': 'both'}, annotations[44])
        # bold, italic, underlined
        self.__check_annotation_in({'start': 75, 'end': 89, 'name': 'bold', 'value': 'True'}, annotations[35])
        self.__check_annotation_in({'start': 66, 'end': 73, 'name': 'italic', 'value': 'True'}, annotations[35])
        self.__check_annotation_in({'start': 91, 'end': 111, 'name': 'underlined', 'value': 'True'}, annotations[35])

    def test_spacing_1(self):
        result = self._send_request("annotation_docx/spacing_libreoffice.docx")['content']['structure']['subparagraphs']
        annotations = [subparagraph['annotations'] for subparagraph in result]

        self.assertTrue({'start': 0, 'end': 10, 'name': 'spacing', 'value': '0'} in annotations[0])
        self.assertTrue({'start': 0, 'end': 10, 'name': 'spacing', 'value': '0'} in annotations[1])
        self.assertTrue({'start': 0, 'end': 10, 'name': 'spacing', 'value': '57'} in annotations[2])
        self.assertTrue({'start': 0, 'end': 10, 'name': 'spacing', 'value': '114'} in annotations[3])
        self.assertTrue({'start': 0, 'end': 10, 'name': 'spacing', 'value': '114'} in annotations[4])
        self.assertTrue({'start': 0, 'end': 10, 'name': 'spacing', 'value': '114'} in annotations[5])
        self.assertTrue({'start': 0, 'end': 10, 'name': 'spacing', 'value': '114'} in annotations[6])
        self.assertTrue({'start': 0, 'end': 9, 'name': 'spacing', 'value': '0'} in annotations[7])

    def test_spacing_2(self):
        result = self._send_request("annotation_docx/"
                                    "spacing_microsoft_word.docx")['content']['structure']['subparagraphs']
        annotations = [subparagraph['annotations'] for subparagraph in result]

        self.__check_annotation_in({'name': 'spacing', 'start': 0, 'value': '0', 'end': 10}, annotations[0])
        self.__check_annotation_in({'name': 'spacing', 'start': 0, 'value': '0', 'end': 10}, annotations[1])
        self.__check_annotation_in({'name': 'spacing', 'start': 0, 'value': '200', 'end': 31}, annotations[2])
        self.__check_annotation_in({'name': 'spacing', 'start': 0, 'value': '200', 'end': 31}, annotations[3])
        self.__check_annotation_in({'name': 'spacing', 'start': 0, 'value': '400', 'end': 32}, annotations[4])
        self.__check_annotation_in({'name': 'spacing', 'start': 0, 'value': '400', 'end': 31}, annotations[5])
        self.__check_annotation_in({'name': 'spacing', 'start': 0, 'value': '600', 'end': 31}, annotations[6])
        self.__check_annotation_in({'name': 'spacing', 'start': 0, 'value': '400', 'end': 10}, annotations[7])
        self.__check_annotation_in({'name': 'spacing', 'start': 0, 'value': '0', 'end': 10}, annotations[8])

    def test_identation(self):
        result = self._send_request("annotation_docx/"
                                    "indentation_libreoffice.docx")['content']['structure']['subparagraphs']
        annotations = [subparagraph['annotations'] for subparagraph in result]
        self.__check_annotation_in({'start': 0, 'end': 62, 'name': 'indentation', 'value': '0'}, annotations[1])
        self.__check_annotation_in({'name': 'indentation', 'start': 0, 'value': '708', 'end': 11}, annotations[12])
