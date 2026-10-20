"""
Caso empresarial: Sistema de gestión de pedidos de una distribuidora

Una distribuidora de productos tecnológicos “Las naranjas” necesita un prototipo en Python para gestionar las solicitudes de sus clientes, controlar las últimas operaciones de despacho y consultar productos por su código. Actualmente, las tareas manuales ocasionan errores en el orden de atención, dificultad para revisar operaciones recientes y demoras al localizar productos.

Desarrolle un programa de consola que utilice una cola FIFO, una pila LIFO y un árbol binario de búsqueda.
"""

"""
Datos iniciales obligatorios
Cola FIFO: Solicitudes P001, P002, P003, registradas en ese orden, con sus datos como estudiantes.
Pila LIFO: Despachos D001, D002, D003, registrados en ese orden.
Árbol binario de búsqueda: Códigos: 50, 30, 70, 20, 40, 60, 80, insertados en ese orden.
"""

# A) Gestión de solicitudes mediante FIFO

# 1. Registrar solicitudes con un código y el nombre del cliente (nombre de los estudiantes)

# 2. Agregar cada solicitud al final de la cola

# 3. Atender la siguiente solicitud respetando el orden de llegada

# 4. Mostrar las solicitudes pendientes

# 5. Controlar cuando no existan solicitudes para atender

# B) Registro de despachos mediante LIFO

# 6. Registrar un despacho con código de operación y código de producto

# 7. Agregar cada despacho a la pila

# 8. Consultar los despachos registrados

# 9. Retirar el último despacho registrado mediante desapilado

# 10. Controlar el intento de retirar elementos cuando la pila esté vacía

# C) Consulta de productos mediante árbol binario de búsqueda

# 11. Crear un árbol binario de búsqueda a partir de códigos numéricos de productos

# 12. Implementar la inserción respetando la propiedad de orden del árbol

# 13. Buscar un código e informar si existe

# 14. Mostrar los códigos mediante un recorrido inorden

# 15. Permitir la eliminación de un código, conservando las propiedades del árbol

# D) Integración, validaciones y demostración

# 16. Integrar las funcionalidades en un menú de consola

# 17. Validar entradas y opciones incorrectas

# 18. Demostrar que las tres estructuras funcionan de manera independiente y coordinada dentro del programa

# 19. Presentar pruebas que permitan verificar los resultados
