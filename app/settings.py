_extensions = [
    'codehilite',
    'fenced_code',
    'abbr',
    'attr_list',
    'def_list',
    'tables',
    'app.mdx.haiku',
    'app.mdx.comment',
    'app.mdx.mathjax',
]

FLATPAGES_PAGES_AUTO_RELOAD = True
FLATPAGES_PAGES_ROOT = 'pages'
FLATPAGES_PAGES_EXTENSION = '.md'
FLATPAGES_PAGES_MARKDOWN_EXTENSIONS = _extensions

FLATPAGES_POSTS_AUTO_RELOAD = True
FLATPAGES_POSTS_ROOT = 'posts'
FLATPAGES_POSTS_EXTENSION = '.md'
FLATPAGES_POSTS_MARKDOWN_EXTENSIONS = _extensions

FLATPAGES_REPOS_AUTO_RELOAD = True
FLATPAGES_REPOS_ROOT = 'repos'
FLATPAGES_REPOS_EXTENSION = '.md'
FLATPAGES_REPOS_MARKDOWN_EXTENSIONS = _extensions

FLATPAGES_TOPICS_AUTO_RELOAD = True
FLATPAGES_TOPICS_ROOT = 'topics'
FLATPAGES_TOPICS_EXTENSION = '.md'
FLATPAGES_TOPICS_MARKDOWN_EXTENSIONS = _extensions

FREEZER_BASE_URL = 'https://www.ccs.neu.edu/home/abaisero/'
FREEZER_REMOVE_EXTRA_FILES = True
FREEZER_DESTINATION = '../build'


# TODO update!
SECRET_KEY = 'super-secret'
