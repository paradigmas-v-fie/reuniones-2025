---
marp: true
theme: default
paginate: true
backgroundColor: #f8f9fa
color: #2c3e50
---

# Unit Testing
## Reduciendo el miedo al cambio

---

## Unit Testing
- Un método mediante el cual unidades individuales de código son probadas para asegurar que funcionan correctamente.
- Verifica la corrección funcional y completitud de unidades individuales de código.
- Son escritas y ejecutadas por desarrolladores de software para asegurar que el código satisface el diseño y se comporta como fue previsto.
- Su finalidad: aislar cada parte del programa y verificar su comportamiento de manera independiente.

---

## Que se verifica?

- La corrección funcional y completitud de una unidad de código.
- El manejo de errores.
- Chequeo de los valores de entrada y de salida.
- Optimizacion de algoritmos.

---

## Tipos de testing.

- Black box: Se enfoca en la salida del sistema a partir de entradas dadas, sin considerar la implementación interna. Ideal para pruebas de aceptación y funcionales.

- White box: Se basa en el conocimiento de la estructura interna del código. Permite pruebas más exhaustivas al considerar la lógica interna y los caminos de ejecución.

- Gray box: Combina elementos de las pruebas de caja negra y caja blanca. Se tiene conocimiento parcial de la implementación interna, lo que permite diseñar pruebas más efectivas.

---

## Testing unitario ideal

- Aislable
- Rápido de ejecutar
- Fácil de entender
- Independiente de otros tests
- Automatizable

---

## Por que testear?

- Asegura la calidad del software.
- Facilita la detección temprana de errores.
- Reduce el costo de corrección de errores.
- Mejora la confianza en el código.
- Facilita el mantenimiento y la evolución del software.

---

## Beneficios

- Permite al programador refactorizar el codigo posteriormente, con confianza.
- Testear las partes facilita la tarea de testear el sistema en su conjunto.
- Provee una documentacion viva del sistema.

---

# Lineamientos de unit testing

---

### Mantener los tests cortos y rápidos
- Idealmente la totalidad de los tests debe ser ejecutado antes de cada integración. Mantener los tests rápidos reduce el tiempo de feedback.

### Los tests deben ser completamente automaticos y no interactivos.
- Los tests deben ser automaticos para ser utiles. Si los resultados requieren inspeccion manual, no son test unitarios adecuados.

---

### Haga tests simples de ejecutar
- Configurar el ambiente de desarrollo para que los tests puedan ser corridos con un solo comando o un click.

### Medir la cobertura de los tests
- Utilizar herramientas que permitan medir la cobertura de los tests para identificar áreas no cubiertas.

---

### Arregla los tests que fallan de forma inmediata
- Cada desarrollador debe ser responsable de asegurarse que los nuevos tests corran exitosamente al integrarlos al repositorio. Si un test falla, debe ser corregido de forma inmediata para asegurarse que el problema se arregle.

---

### Mantener los tests a nivel unitario
- Testing unitario es acerca de testear clases. Tiene que haber una clase test por cada clase ordinaria y el comportamiento de cada clase debe ser probado de forma aislada. Evita la tentacion de testear un flujo entero usando un framework de unit testing, esos tests son lentos y dificiles de mantener.
### Empieza simple
- Un test simple es infinitamente mejor que ningun test.

---

# Las tres A de unit testing.

---

Arrange

El primer paso es preparar lo que se necesita para el test.

Decidir un nombre y hacerlo lo mas amigable y reconocible posible.

Preparar el los mocks si se necesitan. Crear datos de mock, componentes API o funciones, todo lo que sea necesario para que el test corra de manera aislada.

---

## Act

Este paso debe cubrir la ejecucion de la funcionalidad que se desea probar. Normalmente produce un resultado que sera utilizado en el siguiente paso.

---

## Assert

Este paso verifica que el resultado obtenido en el paso anterior es el esperado. Se deben realizar las comprobaciones necesarias para asegurar que la funcionalidad probada se comporta como se espera.

Determina si el test pasa o falla.

---

## Preguntas?
