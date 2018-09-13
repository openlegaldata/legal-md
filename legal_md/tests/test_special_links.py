from legal_md.tests import MarkdownExtensionTest


class SpecialLinksTest(MarkdownExtensionTest):
    maxDiff = None
    extensions = [
            'legal_md.extensions.special_links',
        ]

    def test_match_tags(self):
        self.assert_md_file('match_tags')





