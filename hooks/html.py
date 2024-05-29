"""Add support for ```{=html} code blocks."""

import re

# global list of original html blocks
BLOCKS = []

# fragments that need to be replaced
TWEAKS = [
    ("<pyshell>", "&lt;pyshell&gt;"),
    ("<module>", "&lt;module&gt;"),
    ("&gt;&gt;&gt ", "&gt;&gt;&gt; "),
    (">>> ", "&gt;&gt;&gt; "),
]


def replace_md(match):
    """Extract html code blocks during on_page_markdown."""

    idx = len(BLOCKS)
    repl = "```\n### code block " + str(idx) + "\n```"
    code = match.group(1)
    for old, new in TWEAKS:
        code = code.replace(old, new)
    BLOCKS.append(code)
    return repl


def replace_out(match):
    """Put back the html code blocks during on_post_page."""

    before = '<pre><code>'
    idx = int(match.group(1))
    return before + BLOCKS[idx].rstrip()


def on_page_markdown(markdown, page, config, files):
    """Called after the page's markdown is loaded."""

    return re.sub(r"```{=html}(.*?)```",
                  replace_md, markdown, flags=re.DOTALL)


def on_post_page(output, page, config):
    """Called after the template is rendered."""

    before = "<pre><span></span><code>"
    return re.sub(before + r"### code block (.*?)\n",
                  replace_out, output, flags=re.MULTILINE)
