---
marp: true
theme: gaia
paginate: true
backgroundColor: #fff
---

# Patrones de Diseño
Soluciones probadas para problemas recurrentes

**Facultad de Ingeniería del Ejército**

---

# ¿Qué es un patrón de diseño?

- **Soluciones reutilizables** a problemas comunes en el diseño de software
- **Plantillas conceptuales**, no código específico
- **Lenguaje común** entre desarrolladores
- **Mejores prácticas** documentadas y probadas

---

# Categorías de Patrones

### 🏗️ **Creacionales**
Mecanismos de creación de objetos

### 🔧 **Estructurales**
Composición de clases y objetos

### 🎯 **Comportamiento**
Comunicación entre objetos y distribución de responsabilidades

---

# Patrón Factory Method
Creación de objetos sin especificar la clase exacta

- Define una interfaz para crear objetos
- Las subclases deciden qué clase instanciar
- Delega la creación de objetos a métodos especializados
- **Ejemplo:** Fábrica de vehículos que crea autos o motos según el tipo solicitado

---

# Patrón Singleton
Garantiza una única instancia de la clase

- Asegura que una clase tenga solo una instancia
- Proporciona acceso global a esa instancia
- Controla la instanciación mediante métodos especiales
- **Ejemplo:** Configuración de sistema compartida en toda la aplicación

---

# Patrón Strategy
Define una familia de algoritmos intercambiables

- Encapsula algoritmos en clases separadas
- Permite cambiar algoritmos dinámicamente
- El cliente puede elegir la estrategia apropiada
- **Ejemplo:** Sistema de pagos que puede procesar con tarjeta, efectivo o transferencia

---

# Patrón Observer
Notificación automática de cambios de estado

- Define dependencia uno-a-muchos entre objetos
- Notifica automáticamente a dependientes cuando cambia el estado
- Mantiene consistencia entre objetos relacionados
- **Ejemplo:** Sistema de monitoreo que notifica a múltiples displays cuando hay alertas

---

# Patrón Decorator
Añade funcionalidad dinámicamente

- Extiende funcionalidad de objetos sin alterar su estructura
- Permite combinar comportamientos de forma flexible
- Alternativa a la herencia para extensión de funcionalidad
- **Ejemplo:** Sistema de café donde se pueden agregar ingredientes (leche, chocolate) dinámicamente

---

# Chain of Responsibility
Cadena de manejadores

- Permite que múltiples objetos manejen una solicitud
- Forma una cadena de receptores potenciales
- Desacopla emisor y receptor de la solicitud
- **Ejemplo:** Sistema de soporte con diferentes niveles de escalación

---

# Adapter Pattern
Compatibilidad entre interfaces incompatibles

- Permite que interfaces incompatibles trabajen juntas
- Actúa como traductor entre dos sistemas
- Facilita la integración de código legacy
- **Ejemplo:** Integración de sistema de pagos antiguo con interfaz moderna

---

# Principios SOLID en Patrones

**S** - Single Responsibility
**O** - Open/Closed
**L** - Liskov Substitution
**I** - Interface Segregation
**D** - Dependency Inversion

Los patrones de diseño naturalmente promueven estos principios

---

# Cuándo usar patrones

✅ **Usar cuando:**
- El problema es recurrente y conocido
- Necesitas flexibilidad y extensibilidad
- La complejidad se justifica

❌ **Evitar cuando:**
- La solución simple es suficiente
- Añade complejidad innecesaria
- No entiendes completamente el patrón

---

# Antipatrones comunes

🚫 **God Object** - Una clase que hace demasiado
🚫 **Spaghetti Code** - Código sin estructura clara
🚫 **Copy-Paste Programming** - Duplicación en lugar de abstracción
🚫 **Premature Optimization** - Optimizar antes de medir

---

# Ejemplo Integrado: Sistema de Pedidos
**Combinando múltiples patrones:**

- **Strategy:** Para diferentes métodos de pago
- **Observer:** Para notificar cambios en el pedido
- **Factory:** Para crear diferentes tipos de productos
- **Command:** Para procesar acciones del pedido

**Resultado:** Sistema flexible y extensible que integra varios patrones de diseño

---

# Conclusiones

- Los patrones son **herramientas**, no reglas absolutas
- Resuelven problemas **recurrentes** y probados
- Facilitan la **comunicación** entre desarrolladores
- Promueven código **mantenible** y **escalable**
- La **experiencia** ayuda a reconocer cuándo aplicarlos

---

# Referencias y Recursos

📚 **Libros fundamentales:**
- "Design Patterns" - Gang of Four
- "Head First Design Patterns" - Freeman & Freeman

🔧 **Práctica:**
- Refactoring.guru
- Python Design Patterns
- Implementar en proyectos reales

---

# ¡Gracias!

**Preguntas y Discusión**

**Recuerden:** El mejor patrón es el que resuelve tu problema específico de manera elegante y mantenible.

🚀 **A programar con patrones!**
