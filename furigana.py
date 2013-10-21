"""
# Furigana/Ruby annotations extension for Markdown.

This extension provides a simple syntax to use furigana in a markdown
document.

## Usage
The following construct

    [a](-b)

gets transformed into

    <ruby><rb>a</rb><rp>(</rp><rt>b</rt><rp>)</rp></ruby>

If you now write the following text in your markdown document

    [図](-と)[書](-しょ)[館](-かん)で[本](-ほん)を[読](-よ)みます。

this becomes

    <ruby><rb>図</rb><rp>(</rp><rt>と</rt><rp>)</rp></ruby><ruby><rb>書</rb><rp>(</rp><rt>しょ</rt><rp>)</rp></ruby>
    <ruby><rb>館</rb><rp>(</rp><rt>かん</rt><rp>)</rp></ruby>で<ruby><rb>本</rb><rp>(</rp><rt>ほん</rt><rp>)</rp></ruby>
    を<ruby><rb>読</rb><rp>(</rp><rt>よ</rt><rp>)</rp></ruby>みます。


## Installation
Just copy the script into your python markdown extension directory, eg.
`/usr/lib/python3/dist-packages/markdown/extensions/`

## License
furigana_markdown is licensed under the MIT license.
"""

import markdown
from markdown.inlinepatterns import Pattern
from markdown.util import etree

RUBY_RE = r'(\[)(.*?)\]\(\-(.*?)\)'

class FuriganaExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('ruby', RubyPattern(md), '<link')

class RubyPattern(Pattern):
    def __init__ (self, md):
        Pattern.__init__(self, RUBY_RE)
        self.md = md
    def handleMatch(self, m):
        el = etree.Element('ruby')
        el1 = etree.SubElement(el, 'rb')
        el1.text = m.group(3)
        el2 = etree.SubElement(el, 'rp')
        el2.text = '('
        el3 = etree.SubElement(el, 'rt')
        el3.text = m.group(4)
        el4 = etree.SubElement(el, 'rp')
        el4.text = ')'
        return el

def makeExtension(configs=None):
    return FuriganaExtension(configs=configs)
