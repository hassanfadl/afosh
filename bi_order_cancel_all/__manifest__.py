# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.


{
    'name': ' All in Cancel/Reset Orders(Sales, Purchase, Delivery, Shipment) in Odoo',
    'version': '12.0.0.0',
    'category': 'Sales',
    "author": "BrowseInfo",
    "website": "http://www.browseinfo.in",
    'summary': 'This module helps to reverse the confirmed Sales order,purchase order allow to cancel sales order/purchase order/picking and invoice and set to draft',
    'description': """
    When cancelling sale order, if there are related invoices or delivery orders. It automatically cancels it too. All in Cancel/Reset Orders(Sales, Purchase, Delivery, Shipment) in Odoo, cancel DO
    -Sales Order reverse workflow, Sale order cancel, Sale order cancel, Sales order cancel, cancel Sales order, cancel sale order, cancel confirmed sales order, cancel confirm order, set to draft sales order, cancel done sales order, revese sales order process, cancel confirm quotation.reverse delivery order.
    Sale order reverse workflow
Sales reverse workflow, Sale cancel, Sales cancel order feature on sale. Cancel sales order, Reverse sales order
    modify confirm sales order
    -stock picking reverse workflow, stock picking cancel, delivery order cancel, incoming shipment cancel, cancel picking order, cancel delivery order, cancel incoming shipment, cancel order, set to draft picking, cancel done picking, revese picking process, cancel done delivery order.reverse delivery order.

stock picking reverse workflow, stock picking cancel, delivery order cancel, delivering cancel, cancel picking order, cancel delivery order, cancel shipment shipment, cancel order, set to draft picking, cancel done picking, revese picking process, cancel done delivery order. orden de entrega inversa.

When cancelling sale order, if there are related invoices or delivery orders. It automatically cancels it too.
    -Sales Order reverse workflow, Sale order cancel, Sale order cancel, Sales order cancel, cancel Sales order, cancel sale order, cancel confirmed sales order, cancel confirm order, set to draft sales order, cancel done sales order, revese sales order process, cancel confirm quotation.reverse delivery order.
    Sale order reverse workflow
Sales reverse workflow, Sale cancel, Sales cancel order feature on sale. Cancel sales order, Reverse sales order , 
    modify confirm sales order
    -stock picking reverse workflow, stock picking cancel, delivery order cancel, incoming shipment cancel, cancel picking order, cancel delivery order, cancel incoming shipment, cancel order, set to draft picking, cancel done picking, revese picking process, cancel done delivery order.reverse delivery order.

stock picking reverse workflow, stock picking cancel, delivery order cancel, delivering cancel, cancel picking order, cancel delivery order, cancel shipment shipment, cancel order, set to draft picking, cancel done picking, revese picking process, cancel done delivery order. orden de entrega inversa.

sélection de stock reverse workflow, sélection de stock annuler, annulation de commande, annulation de livraison, annulation de commande, annulation de livraison, annulation de livraison, annulation de la commande, annulation de la sélection, annulation de la préparation, annulation du bon de livraison. ordre de livraison inverse.
 -purchases Order reverse workflow, purchase order cancel, purchase order cancel, purchases order cancel, cancel purchases order, cancel purchase order, cancel confirmed purchases order, cancel confirm order, set to draft purchases order, cancel done purchases order, revese purchases order process, cancel confirm quotation.reverse delivery order.
    purchase order reverse workflow
purchases reverse workflow, purchase cancel, purchases cancel order feature on purchase. Cancel purchases order, Reverse purchases order
    modify confirm purchases order
    cancel stock picking , reset all orders
    `cancel and reset to draft picking
    cancel reset picking
    cancel picking
    cancel delivery order
    cancel incoming shipment
    reverse stock picking
    reverse delivery order
    Cancel invoice based on sales
    cancel invoice based on purchase
    cancel all in one order
    cancel all orders
    all order cancel
    all order reset
    all order reverse
    reverse order all in one
    """,
    'price': '20',
    'currency': "EUR",
    'depends': ['sale_stock','account_cancel','stock_picking_cancel_extended','purchase','bi_inventory_adjustment_cancel_reverse'],
    'data': [
                'security/cancel_order_security.xml',
                'views/sale_view.xml',
                'views/purchase_view.xml',
    ],
    'live_test_url':'https://youtu.be/8fZri9yrwEM',
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    "images":['static/description/Banner.png'],
}
