from string import Template

html_template = Template('''<!DOCTYPE html>
<html>
<head>
<title>Aves de Chile</title>
</head>
<body>

<h1>Aves de Chile</h1>

$body

</body>
</html>
''')

aves_template = Template ('''
        <h1>$title_es</h1>
        <h2>$title_en</h2>
        <img src="$url">
        ''')