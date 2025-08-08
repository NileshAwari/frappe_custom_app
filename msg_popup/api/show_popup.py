import frappe

def show(title, message, alert=False):
    """Display popup message from console"""
    frappe.msgprint(
        title=title,
        msg=message,
        indicator='red' if alert else 'blue',
        alert=alert
    )
    return f"Displayed: {title}"
