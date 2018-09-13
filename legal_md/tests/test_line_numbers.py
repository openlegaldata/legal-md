from legal_md.tests import MarkdownExtensionTest


class LineNumbersTest(MarkdownExtensionTest):
    maxDiff = None
    extensions = [
            'legal_md.extensions.line_numbers',
        ]

    def test_single_line(self):
        self.assert_md_file('single_line')

    def test_mixed(self):
        self.assert_md_file('mixed')

    def test_case_text(self):
        self.assert_md_file('case_text')

    def test_lines_with_single_line_breaks(self):
        self.assert_md_file('lines_with_single_line_breaks')





