import os

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

    def test_os_line_breaks(self):
        """Test on line breaks (e.g. \r\n, ...) """
        with open(os.path.join(self.RESOURCE_DIR, 'os_line_breaks.html')) as html_file:
            self.assertEqual(self.convert_md('1| ab\r\n\r\n2| cd'), html_file.read().strip())

    def test_lines_with_single_line_breaks(self):
        self.assert_md_file('lines_with_single_line_breaks')





