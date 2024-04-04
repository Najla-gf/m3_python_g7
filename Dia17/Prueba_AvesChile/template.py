from string import Template

html_template = Template('''<!DOCTYPE html>
<html leng="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Aves de Chile</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>

<h1 class="text-center">Aves de Chile</h1>

<div class="container">
        <div class="row">
$body

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
''')

aves_template = Template ('''
                <div class="col-md-3 mb-4">
                        <div class="card">
                                <img src="$url" class="card-img-top" alt="Pajaro">
                                <div class="card-body">
                                        <h5 class="card-title">$name_spa</h5>
                                        <p class="card-text">$name_eng</p>
                                </div>
                        </div>
                </div>

        ''')