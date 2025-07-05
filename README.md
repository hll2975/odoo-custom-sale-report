 # custom_sale_report

Este módulo extiende la funcionalidad de los reportes estándar de Odoo para generar un documento PDF personalizado de las órdenes de venta.

## 🎯 Objetivo
Proporcionar un reporte QWeb claro, profesional y adaptable para PyMEs y entornos personalizados, con campos adicionales y formato específico.

## 📦 Características
- Encabezado con logo de la empresa, datos del cliente y vendedor
- Tabla de líneas de venta detallada
- Totales con desglose de impuestos
- Condiciones comerciales editables
- Totalmente heredado desde `report_saleorder_document`
- Sin dependencias externas

## 🧱 Requisitos
- Odoo 15 o superior
- Módulo `sale_management` instalado

## 🚀 Instalación
1. Clonar el repositorio en la carpeta de addons:
   ```bash
   git clone https://github.com/tu_usuario/custom_sale_report.git

2. Reiniciar el servidor de Odoo

3. Activar el modo desarrollador e instalar el módulo desde Aplicaciones

📄 Estructura Técnica
Herencia de vistas y reportes en reports/

Campo nuevo editable en sale.order para condiciones comerciales (editable desde UI)

Plantilla QWeb clara y modularizada

✍️ Autores
Desarrollado por [Tu Nombre] - Desarrollador Odoo | [LinkedIn/Portafolio]

🧪 Licencia
MIT


---

### 🔧 Fragmento QWeb básico (en `report_templates.xml`)

```xml
<t t-name="custom_sale_report.custom_report_saleorder">
  <t t-call="web.external_layout">
    <div class="page">
      <h2>Orden de Venta - Personalizada</h2>
      <p>Cliente: <t t-esc="o.partner_id.name"/></p>
      <p>Vendedor: <t t-esc="o.user_id.name"/></p>
      <!-- Detalle del pedido -->
      <table class="table table-sm">
        <thead>
          <tr>
            <th>Producto</th><th>Cantidad</th><th>Precio</th><th>Subtotal</th>
          </tr>
        </thead>
        <tbody>
          <tr t-foreach="o.order_line" t-as="line">
            <td><t t-esc="line.name"/></td>
            <td><t t-esc="line.product_uom_qty"/></td>
            <td><t t-esc="line.price_unit"/></td>
            <td><t t-esc="line.price_subtotal"/></td>
          </tr>
        </tbody>
      </table>
      <p>Total: <t t-esc="o.amount_total"/></p>
      <p><strong>Condiciones:</strong> <t t-esc="o.x_commercial_terms"/></p>
    </div>
  </t>
</t>
