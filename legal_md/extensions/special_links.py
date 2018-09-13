import re
from urllib.parse import urlparse, parse_qs

from lxml import etree
from lxml.html import HtmlElement

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor


class SpecialLinksTreeprocessor(Treeprocessor):
    """

    This extension replaces links, e.g. [link text](link url), with special HTML if the use specific protocols as url.
    By doing so documents elements can be "tagged" with additional data.

    The following special links are supported:

    - Law references (law://): - NOT IMPLEMENTED YET
    - Literature references (literature://): - NOT IMPLEMENTED YET
    - Court decision references (decision://): - NOT IMPLEMENTED YET
    - Citation matches (match://): Used to visualize citation analysis
        - Hostname/Path: Reference id
        - Query parameters:
            - data-id: A unique identifier
            - data-color: Color as hex (e.g. #FFFFFF; do not forget to encode hash sign)
            - data-algorithm: Algorithm that found this match
            - data-algorithm-type: Broad category of algorithm

    match://case/123?data-id=match-2&data-color=%23ff4033&data-algorithm=bc&data-algorithm-type=citation

    """

    def handle_match(self, elem, href):
        parsed = urlparse(href)
        attrs = parse_qs(parsed.query)

        for key in attrs:
            val = attrs[key]

            if len(val) < 1:
                raise ValueError('Query parameter is not set.')
            if len(val) != 1:
                raise ValueError('Query parameters cannot be arrays.')

            val = val[0]

            elem.set(key, val)

            print('Sets: %s = %s' % (key, val))

        elem.tag = 'em'
        del elem.attrib['href']

        elem.set('class', 'match js-match')

        return elem

    def run(self, doc):
        # Iterate over all elements in doc tree
        for elem in doc.iter():

            # We are only interested in links
            if elem.tag == 'a':
                href = str(elem.get('href'))

                # Check protocols
                if href.startswith('match://'):
                    return self.handle_match(elem, href)

                elif href.startswith('ecli://'):
                    raise NotImplementedError('Case refs are not implemented')
                elif href.startswith('law://'):
                    raise NotImplementedError('Law refs are not implemented')


class SpecialLinksExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.treeprocessors.add(
            'special_links', SpecialLinksTreeprocessor(md), '_end'
        )


def makeExtension(*args, **kwargs):
    return SpecialLinksExtension(*args, **kwargs)
