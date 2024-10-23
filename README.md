# Parcial materia Programacion III 
## Profesor Pablo Scrigna

El proyecto es un programa realizado en Python que guarda en una base de datos un SKU, modelo y compatibilidad de "Casa de respuestos IADES".

### Tecnologías utilizadas
* **Backend:** Python
* **Base de datos:** MongoDB

## Base de datos 
Utilizo MongoDB como base de datos para almacenar la información de los SKU cargados, modelo, nombre y compatibilidad.

**Estructura básica:**

* **SKU:** Almacena el ID de los respuestos.
* **modelo:** Contiene información sobre el modelo del respuesto.
* **compatibilidad:** Guarda los detalles de la compatibilidad del respuesto con otras marcas.

**Conexión:**
La conexión a la base de datos se establece a través de una cadena de conexión almacenada en la variable de entorno `URL`. 
