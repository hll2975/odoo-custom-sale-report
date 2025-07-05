{
    "name": "Custom Sale Report",
    "version": "15.0.1.0.0",
    "summary": "Reporte personalizado PDF para órdenes de venta",
    "category": "Sales",
    "author": "Hernán",
    "license": "MIT",
    "depends": ["sale_management"],
    "data": [
        "views/sale_order_view_inherit.xml",
        "reports/custom_sale_report.xml",
        "reports/report_templates.xml"
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
}
