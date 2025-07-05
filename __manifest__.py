{
    "name": "Custom Sale Report",
    "version": "15.0.1.0.0",
    "summary": "Reporte PDF personalizado de órdenes de venta con condiciones comerciales.",
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
}

