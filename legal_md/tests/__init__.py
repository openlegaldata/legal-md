from unittest import TestCase

import os

import markdown


class MarkdownExtensionTest(TestCase):
    maxDiff = None
    extensions = [
        ]
    RESOURCE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources')

    def assert_md_file(self, resource_name, msg=None):
        """Compare resource markdown file with corresponding html file"""
        with open(os.path.join(self.RESOURCE_DIR, resource_name + '.md')) as md_file:
            with open(os.path.join(self.RESOURCE_DIR, resource_name + '.html')) as html_file:
                md_content = md_file.read()
                expected = html_file.read().strip()
                actual = markdown.markdown(md_content, extensions=self.extensions)

                self.assertEqual(expected, actual, msg)
