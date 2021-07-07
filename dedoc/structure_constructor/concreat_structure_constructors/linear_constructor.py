from typing import Optional

from dedoc.data_structures.document_content import DocumentContent
from dedoc.data_structures.line_with_meta import LineWithMeta
from dedoc.data_structures.tree_node import TreeNode
from dedoc.data_structures.unstructured_document import UnstructuredDocument
from dedoc.structure_constructor.concreat_structure_constructors.abstract_structure_constructor import \
    AbstractStructureConstructor
from dedoc.structure_parser.heirarchy_level import HierarchyLevel


class LinearConstructor(AbstractStructureConstructor):

    def __init__(self):
        pass

    def structure_document(self,
                           document: UnstructuredDocument,
                           structure_type: Optional[str] = None) -> DocumentContent:
        lines = document.lines
        tree = TreeNode.create(lines=[])
        prev_line = None
        for line in lines:
            if self.__new_child(line, prev_line):
                tree.add_child(line)
            else:
                tree.add_text(line)
            prev_line = line

        tree.merge_annotations()
        return DocumentContent(tables=document.tables, structure=tree)

    def __new_child(self, line: LineWithMeta, prev_line: Optional[LineWithMeta]) -> bool:
        if line.hierarchy_level.paragraph_type == HierarchyLevel.root:
            return False
        return (prev_line is None or
                not line.hierarchy_level.can_be_multiline or
                line.hierarchy_level != prev_line.hierarchy_level)
