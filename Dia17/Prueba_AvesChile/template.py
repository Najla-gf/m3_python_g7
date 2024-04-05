from string import Template

html_template = Template('''<!DOCTYPE html>
<html leng="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="author" content="Najla Gatica">
<meta name="description" content="Aves de Chile">
<meta name="keywords" content="aves, fauna, pajaros, naturaleza, chile">
<title>Aves de Chile</title>
<link rel="icon" href="assets/img/bird.png" type="image/png">
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>

<style>
        body {
        font-family: 'Poppins', sans-serif;
        font-weight: 300;
        font-style: normal;
        }
</style>

<h1 class="text-center">Aves de Chile</h1>

<div class="container">
        <div class="row">
$body

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
''')

aves_template = Template ('''
                <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-3">
                        <div class="card">
                                <img src="$url" class="card-img-top" alt="Pajaro">
                                <div class="card-body">
                                        <h5 class="card-title">$name_spa</h5>
                                        <p class="card-text">$name_eng</p>
                                </div>
                        </div>
                </div>
''')