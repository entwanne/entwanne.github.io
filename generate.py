import jinja2


files = {}

fr_flag = '<img src="/img/fr_flag.png" alt="FR" title="Français" />'
en_flag = '<img src="/img/gb_flag.png" alt="EN" title="English" />'

files['index.html'] = {
    'title': 'Antoine Rozo (entwanne)',
    'job': 'Développeur Python',
    'avatar': 'img/entwanne.png',
    'avatar_alt': 'entwanne',
    'lang': 'fr',
    'header_links': f'<a href="#">{fr_flag}</a> — <a href="en/">{en_flag}</a>',
    'credits': '© Logos Python, PyConFr, Zeste de Savoir, Twitter & Github. Drapeaux par OpenMoji.',
    'sections': [
        {
            'title': 'Projets',
            'entries': [
                {
                    'title': 'Onitu',
                    'image': 'img/logo_onitu.png',
                    'image_alt': 'logo',
                    'description': '''
                    Outil de synchronisation de fichiers à travers plusieurs services (<i>Google Drive</i>, <i>Dropbox</i>, <i>Amazon S3</i>).<br/>
	            Réalisé avec <i>Python</i> et <i>zeromq</i>.
                    ''',
                    'links': [
                        ('Site officiel', 'http://onitu.github.io'),
                        ('Code source', 'https://github.com/onitu/onitu'),
                    ],
                },
                {
                    'title': 'Rodolphe',
                    'image': 'img/logo_rodolphe.png',
                    'image_alt': 'logo',
                    'description': '''
                    Forum d'images anonyme.<br/>
	            Réalisé avec <i>Python</i> et <i>Django</i>.
                    ''',
                    'links': [
                        ('Code source', 'https://github.com/RodolpheOrg/Rodolphe'),
                    ],
                },
                {
                    'title': 'Not A Game Manager',
                    'image': 'img/logo_nagm.png',
                    'image_alt': 'logo',
                    'description': '''
                    Petit moteur de jeux type RPG.<br/>
	            Réalisé avec <i>Python</i> et <i>Pyglet</i>.
                    ''',
                    'links': [
                        ('Code source', 'https://github.com/entwanne/NAGM'),
                    ],
                },
                {
                    'title': "Et d'autres encore",
                    'image': 'img/dots.png',
                    'image_alt': 'logo',
                    'description': 'Divers projets et expérimentations, en Python mais pas que, à retrouver sur mon profil <i>Github</i>.',
                    'links': [
                        ('Profil <i>Github</i>', 'https://github.com/entwanne'),
                    ],
                },
            ],
        },
        {
            'title': 'Publications',
            'entries': [
                {
                    'title': 'Notions de Python avancées',
                    'image': 'img/logo_cours_python_avance.png',
                    'image_alt': 'logo',
                    'description': 'Cours sur les notions avancées du langage Python : itérateurs, générateurs, décorateurs, métaclasses, etc.',
                    'links': [
                        ('Publication', 'https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/'),
                        ('Code source', 'https://github.com/entwanne/cours_python_avance'),
                    ],
                },
                {
                    'title': "Les secrets d'un code pythonique",
                    'image': 'img/logo_article_code_pythonique.png',
                    'image_alt': 'logo',
                    'description': "Article dédié à la philosophie Python et la structuration d'un bon code.",
                    'links': [
                        ('Publication', 'https://zestedesavoir.com/articles/1079/les-secrets-dun-code-pythonique/'),
                        ('Code source', 'https://github.com/entwanne/article_pythonic_code'),
                    ],
                },
                {
                    'title': 'La programmation orientée objet en Python',
                    'image': 'img/logo_cours_python_poo.png',
                    'image_alt': 'logo',
                    'description': 'Cours portant sur la programmation orientée objet en Python : classes, méthodes, héritage, opérateurs et autres.',
                    'links': [
                        ('Publication', 'https://zestedesavoir.com/tutoriels/1253/la-programmation-orientee-objet-en-python/'),
                        ('Code source', 'https://github.com/ArnaudCalmettes/cours-python3-poo'),
                    ],
                },
                {
                    'title': 'Sortie de Python 3.6',
                    'image': 'img/logo_article_python36.png',
                    'image_alt': 'logo',
                    'description': 'Article évoquant les nouveautés apportées par la version 3.6 de Python.',
                    'links': [
                        ('Publication', 'https://zestedesavoir.com/articles/1540/sortie-de-python-3-6/'),
                    ],
                },
            ],
        },
        {
            'title': 'Divers',
            'entries': [
                {
                    'title': 'Documentation Python FR',
                    'image': 'img/logo_python.png',
                    'image_alt': 'logo',
                    'description': 'Participation à la traduction en français de la documentation Python.',
                    'links': [
                        ('Code source', 'https://github.com/python/python-docs-fr'),
                    ],
                },
                {
                    'title': 'Réalisations graphiques',
                    'image': 'img/picsou.png',
                    'image_alt': 'logo',
                    'description': 'Différents modèles vectoriels dessinés avec <i>Inkscape</i>.',
                    'links': [
	                ('Galerie <i>Deviantart</i>', 'https://entwanne.deviantart.com/gallery'),
	                ('Boutique <i>RedBubble</i>', 'https://www.redbubble.com/people/entwanne/shop'),
                    ],
                },
            ],
        },
        {
            'title': 'Contact',
            'entries': [
                {
                    'image': 'img/logo_email.png',
                    'image_title': 'E-mail',
                    'raw': '<h4>antoine <i>[dot]</i> rozo <i>[at]</i> gmail <i>[dot]</i> com</h4>',
                },
                {
                    'image': 'img/logo_twitter.png',
                    'image_title': 'Twitter',
                    'raw': '<h4><a href="http://twitter.com/entwanne">@entwanne</a></h4>',
                },
                {
                    'image': 'img/logo_github.png',
                    'image_title': 'Github',
                    'raw': '<h4><a href="https://github.com/entwanne">entwanne</a></h4>',
                },
            ],
        },
    ],
    'css': 'css/bootstrap.min.css',
}

files['en/index.html'] = {
    'title': 'Antoine Rozo (entwanne)',
    'job': 'Python Developer',
    'avatar': '../img/entwanne.png',
    'avatar_alt': 'entwanne',
    'lang': 'en',
    'header_links': f'<a href="../">{fr_flag}</a> — <a href="#">{en_flag}</a>',
    'credits': '© Python, PyConFr, Zeste de Savoir, Twitter & Github logos. Flags by OpenMoji.',
    'sections': [
        {
            'title': 'Projects',
            'entries': [
                {
                    'title': 'Onitu',
                    'image': '../img/logo_onitu.png',
                    'image_alt': 'logo',
                    'description': '''
                    File synchronization tool between several services (<i>Google Drive</i>, <i>Dropbox</i>, <i>Amazon S3</i>).<br/>
	            Realized with <i>Python</i> and <i>zeromq</i>.
                    ''',
                    'links': [
                        ('Official website', 'http://onitu.github.io'),
                        ('Source code', 'https://github.com/onitu/onitu'),
                    ],
                },
                {
                    'title': 'Rodolphe',
                    'image': '../img/logo_rodolphe.png',
                    'image_alt': 'logo',
                    'description': '''
                    Anonymous imageboard.<br/>
	            Realized with <i>Python</i> and <i>Django</i>.
                    ''',
                    'links': [
                        ('Source code', 'https://github.com/RodolpheOrg/Rodolphe'),
                    ],
                },
                {
                    'title': 'Not A Game Manager',
                    'image': '../img/logo_nagm.png',
                    'image_alt': 'logo',
                    'description': '''
	            Little role-playing-game engine.<br/>
	            Realized with <i>Python</i> and <i>Pyglet</i>.
                    ''',
                    'links': [
                        ('Source code', 'https://github.com/entwanne/NAGM'),
                    ],
                },
                {
                    'title': "And ever more",
                    'image': '../img/dots.png',
                    'image_alt': 'logo',
                    'description': 'Various projects and experiments, in Python or not, that you can find on my <i>Github</i> profile.',
                    'links': [
                        ('<i>Github</i> profile', 'https://github.com/entwanne'),
                    ],
                },
            ],
        },
        {
            'title': 'Publications',
            'entries': [
                {
                    'title': 'Advanced Python notions',
                    'image': '../img/logo_cours_python_avance.png',
                    'image_alt': 'logo',
                    'description': 'French course on advanced notions of Python language: iterators, générators, decorators, metaclasses, etc.',
                    'links': [
                        ('Publication <i>(FR)</i>', 'https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/'),
                        ('Source code', 'https://github.com/entwanne/cours_python_avance'),
                    ],
                },
                {
                    'title': 'Secrets of pythonic code',
                    'image': '../img/logo_article_code_pythonique.png',
                    'image_alt': 'logo',
                    'description': 'French article dedicated to Python philosophy and structuration of a good code.',
                    'links': [
                        ('Publication <i>(FR)</i>', 'https://zestedesavoir.com/articles/1079/les-secrets-dun-code-pythonique/'),
                        ('Source code', 'https://github.com/entwanne/article_pythonic_code'),
                    ],
                },
                {
                    'title': 'Object-oriented programming in Python',
                    'image': '../img/logo_cours_python_poo.png',
                    'image_alt': 'logo',
                    'description': 'French course of object-oriented programming in Python: classes, methods, inheritance, operators and so more.',
                    'links': [
                        ('Publication <i>(FR)</i>', 'https://zestedesavoir.com/tutoriels/1253/la-programmation-orientee-objet-en-python/'),
                        ('Source code', 'https://github.com/ArnaudCalmettes/cours-python3-poo'),
                    ],
                },
                {
                    'title': 'Python 3.6 release',
                    'image': '../img/logo_article_python36.png',
                    'image_alt': 'logo',
                    'description': 'French article about new features introduced by Python 3.6.',
                    'links': [
                        ('Publication <i>(FR)</i>', 'https://zestedesavoir.com/articles/1540/sortie-de-python-3-6/'),
                    ],
                },
            ],
        },
        {
            'title': 'Miscellaneous',
            'entries': [
                {
                    'title': 'French Python documentation',
                    'image': '../img/logo_python.png',
                    'image_alt': 'logo',
                    'description': 'Contribution to French translation of Python documentation.',
                    'links': [
                        ('Source code', 'https://github.com/python/python-docs-fr'),
                    ],
                },
                {
                    'title': 'Graphics',
                    'image': '../img/picsou.png',
                    'image_alt': 'logo',
                    'description': 'Different vector models drawn with <i>Inkscape</i>.',
                    'links': [
	                ('<i>Deviantart</i> gallery', 'https://entwanne.deviantart.com/gallery'),
	                ('<i>RedBubble</i> shop', 'https://www.redbubble.com/people/entwanne/shop'),
                    ],
                },
            ],
        },
        {
            'title': 'Contact',
            'entries': [
                {
                    'image': '../img/logo_email.png',
                    'image_title': 'E-mail',
                    'raw': '<h4>antoine <i>[dot]</i> rozo <i>[at]</i> gmail <i>[dot]</i> com</h4>',
                },
                {
                    'image': '../img/logo_twitter.png',
                    'image_title': 'Twitter',
                    'raw': '<h4><a href="http://twitter.com/entwanne">@entwanne</a></h4>',
                },
                {
                    'image': '../img/logo_github.png',
                    'image_title': 'Github',
                    'raw': '<h4><a href="https://github.com/entwanne">entwanne</a></h4>',
                },
            ],
        },
    ],
    'css': '../css/bootstrap.min.css',
}


def grouper(iterable, n):
    group = []
    for i, value in enumerate(iterable):
        group.append(value)
        if i % n == n - 1:
            yield group
            group = []
    if group:
        yield group


env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./"))
env.globals.update(grouper=grouper)
tpl = env.get_template('template.html.jinja')

for filename, context in files.items():
    tpl.stream(context).dump(filename)
