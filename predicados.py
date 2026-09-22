# Universo:
alumnos = {"A1", "A2", "A3", "A4"}
profesores = {"P1", "P2", "P3", "P4"}
materias = {"M1", "M2", "M3", "M9"}
carreras = {"C1", "C2", "C3", "C4"}
salones = {"S1", "S2", "S3", "S4"}

universo = alumnos | profesores | materias | carreras | salones

print("=== UNIVERSO ===")
print("Alumnos:", alumnos)
print("Profesores:", profesores)
print("Materias:", materias)
print("Carreras:", carreras)
print("Salones:", salones)
print("Universo completo:", universo)


# Relaciones
alumno_carrera = {
    ("A1", "C1"),
    ("A2", "C1"),
    ("A3", "C3"),
    ("A4", "C4")
}

profesor_materia = {
    ("P1", "M1"),
    ("P2", "M2"),
    ("P3", "M3"),
    ("P4", "M9")
}


# Predicados
# 1) X es un alumno
def es_alumno(x):
    return x in alumnos


# 2) X es un profesor
def es_profesor(x):
    return x in profesores


# 3) X es una materia
def es_materia(x):
    return x in materias


# 4) X es una carrera
def es_carrera(x):
    return x in carreras


# 5) X es un salón
def es_salon(x):
    return x in salones


# 6) X es de la carrera Y
def es_de_la_carrera(x, y):
    return (x, y) in alumno_carrera


# 7) X da la clase Y
def da_la_clase(x, y):
    return (x, y) in profesor_materia


# Consultas positivas y negativas
print("\n=== CONSULTAS ===")

# Predicado 1
print("1. Positiva:", es_alumno("A1"))
print("1. Negativa:", es_alumno("P1"))

# Predicado 2
print("2. Positiva:", es_profesor("P1"))
print("2. Negativa:", es_profesor("A1"))

# Predicado 3
print("3. Positiva:", es_materia("M1"))
print("3. Negativa:", es_materia("A1"))

# Predicado 4
print("4. Positiva:", es_carrera("C1"))
print("4. Negativa:", es_carrera("A1"))

# Predicado 5
print("5. Positiva:", es_salon("S1"))
print("5. Negativa:", es_salon("A1"))

# Predicado 6
print("6. Positiva:", es_de_la_carrera("A1", "C1"))
print("6. Negativa:", es_de_la_carrera("A2", "C2"))

# Predicado 7
print("7. Positiva:", da_la_clase("P1", "M1"))
print("7. Negativa:", da_la_clase("A2", "M1"))