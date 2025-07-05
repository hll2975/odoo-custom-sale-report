# Custom Sale Report

> **🌐 Español | 🇬🇧 English below**

Este módulo extiende el reporte estándar de Odoo para personalizar la orden de venta en formato PDF, utilizando QWeb.

## ✨ Características
- Encabezado con logo, cliente y vendedor
- Tabla detallada de productos
- Totales con impuestos
- Campo adicional: "Condiciones Comerciales"
- Herencia limpia de `report_saleorder_document`

## 📦 Requisitos
- Odoo 15 o superior
- Módulo `sale_management`

## 🚀 Instalación

1. Cloná este repositorio dentro del directorio de addons de tu instancia Odoo:
   ```bash
   git clone https://github.com/TU_USUARIO/odoo-custom-sale-report.git

2. Reiniciá el servidor de Odoo.

3. Activá el modo desarrollador e instalá el módulo desde el backend.

📝 Licencia
MIT License

📸 Vista previa

🇬🇧 English
This Odoo module customizes the standard sales order PDF report using QWeb templates.

✨ Features

+ Header with company logo, customer and salesperson
- Detailed product table
- Totals with tax breakdown
- Extra editable field: "Commercial Terms"
- Clean inheritance of report_saleorder_document

📦 Requirements:

- Odoo 15 or higher
- sale_management module installed

🚀 Installation

1. Clone the repository into your Odoo addons folder:
git clone https://github.com/YOUR_USERNAME/odoo-custom-sale-report.git

2. Restart the Odoo server.

3. Activate developer mode and install the module from the Apps menu.

📝 License
MIT License

📸 Preview

Desarrollado por Tecnológica VHL| Built by Tecnológica VHL 
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
