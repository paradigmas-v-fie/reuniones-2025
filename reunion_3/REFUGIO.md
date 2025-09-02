# Refugio de mascotas

El refugio debe:
- Listar mascotas disponibles para adoptar
- Llevar registro de adopciones para seguimiento
- Definir políticas globales de convivencia de mascotas

## Políticas del Refugio (GLOBALES)
El refugio establece límites máximos de convivencia por tipo de mascota en cualquier hogar:
- Máximo 3 perros
- Máximo 5 gatos
- Máximo 10 aves
- (Extensible a otros tipos: peces, tortugas, etc.)

## Mascotas
- Tienen apodo y número de identificación
- Pueden saludar() a los visitantes (solo si están rehabilitadas)
- Tienen fecha de ingreso al refugio
- **RESPONSABILIDAD CLAVE**: Cada tipo de mascota conoce su límite máximo de convivencia y debe validarlo

### Tipos de mascotas y rehabilitación:
- **Perros**: 1 mes de rehabilitación, máximo 3 por hogar
- **Gatos**: 6 meses de rehabilitación, máximo 5 por hogar
- **Aves**: Sin período de rehabilitación, máximo 10 por hogar

## Adoptantes
Personas registradas que pueden adoptar mascotas según su categoría:

### Novato
- Puede tener **UNA sola mascota** de cualquier tipo
- Lanza excepción si intenta adoptar más de una

### Tránsito
- Puede tener múltiples mascotas pero **solo del mismo tipo**
- Lanza excepción si intenta mezclar tipos diferentes
- Respeta los límites globales del refugio

### Avanzado (antes Benefactor)
- Puede tener mascotas de diferentes tipos
- Solo limitado por las políticas globales del refugio
- Lanza excepción si excede límites por tipo

## Requisitos Técnicos

### Uso de Excepciones (OBLIGATORIO)
- AdopcionInvalidaError: base para todas las excepciones
- LimiteExcedidoError: cuando se supera el límite de mascotas
- TipoIncompatibleError: para tránsito con tipos mezclados
- MascotaNoDisponibleError: mascota no rehabilitada

### Inversión de Responsabilidad
La validación del límite máximo debe estar en la mascota, NO en el adoptante:
```python
# CORRECTO - La mascota valida su propio límite
def puede_convivir_con(self, mascotas_existentes):
    mismo_tipo = [m for m in mascotas_existentes if type(m) == type(self)]
    if len(mismo_tipo) >= self.limite_maximo:
        raise LimiteExcedidoError(...)
