### # web/generate_html.py
###
### def generate_html(matrix):
###     print("Matrix to HTML:", matrix)  # Depuración
###     html_content = """
###     <html>
###     <head>
###         <style>
###             table {{ width: 100%; border-collapse: collapse; }}
###             th, td {{ border: 1px solid black; padding: 8px; text-align: center; }}
###             th {{ background-color: #f2f2f2; }}
###         </style>
###     </head>
###     <body>
###         <h1>Matriz de Eisenhower</h1>
###         <table>
###             <tr>
###                 <th>Urgente e Importante</th>
###                 <th>No Urgente pero Importante</th>
###             </tr>
###             <tr>
###                 <td>{0}</td>
###                 <td>{1}</td>
###             </tr>
###             <tr>
###                 <th>Urgente pero No Importante</th>
###                 <th>No Urgente y No Importante</th>
###             </tr>
###             <tr>
###                 <td>{2}</td>
###                 <td>{3}</td>
###             </tr>
###         </table>
###     </body>
###     </html>
###     """
###
###     def format_tasks(tasks):
###         if not tasks:
###             return "No hay tareas en esta categoría."
###         return "<ul>" + "".join([f"<li>{'✅' if completed else '❌'} {task}</li>" for _, task, completed in tasks]) + "</ul>"
###
###     # Formatear las tareas para cada cuadrante
###     categories = ["Urgente e Importante", "No Urgente pero Importante", "Urgente pero No Importante", "No Urgente y No Importante"]
###     formatted_tasks = [format_tasks(matrix[category]) for category in categories]
###
###     # Generar contenido HTML
###     return html_content.format(*formatted_tasks)
###
### def save_html_file(content, path):
###     with open(path, 'w') as file:
###         file.write(content)
##
### web/generate_html.py
##
##def generate_html(matrix):
##        file.write(content)
#
#
#
#def generate_html(matrix):
#    html_content = """
#    <!DOCTYPE html>
#    <html lang="es">
#    <head>
#        <meta charset="UTF-8">
#        <style>
#            body {
#                font-family: Arial, sans-serif;
#                background-color: #f4f4f9;
#                color: #333;
#            }
#            table {
#                width: 100%;
#                border-collapse: collapse;
#                margin-top: 20px;
#            }
#            th, td {
#                border: 1px solid #ddd;
#                padding: 12px;
#                text-align: center;
#            }
#            th {
#                background-color: #4CAF50;
#                color: white;
#            }
#            tr:nth-child(even) {
#                background-color: #f2f2f2;
#            }
#            tr:hover {
#                background-color: #ddd;
#            }
#            ul {
#                list-style: none;
#                padding: 0;
#            }
#            li::before {
#                content: "• ";
#                color: #4CAF50;
#                font-weight: bold;
#            }
#        </style>
#    </head>
#    <body>
#        <h1>Matriz de Eisenhower</h1>
#        <table>
#            <tr>
#                <th>Urgente e Importante</th>
#                <th>No Urgente pero Importante</th>
#            </tr>
#            <tr>
#                <td>{0}</td>
#                <td>{1}</td>
#            </tr>
#            <tr>
#                <th>Urgente pero No Importante</th>
#                <th>No Urgente y No Importante</th>
#            </tr>
#            <tr>
#                <td>{2}</td>
#                <td>{3}</td>
#            </tr>
#        </table>
#    </body>
#    </html>
#    """
#
#    def format_tasks(tasks):
#        if not tasks:
#            return "No hay tareas en esta categoría."
#        return "<ul>" + "".join([f"<li>{'✅' if completed else '❌'} {task}</li>" for _, task, completed in tasks]) + "</ul>"
#
#    categories = ["Urgente e Importante", "No Urgente pero Importante", "Urgente pero No Importante", "No Urgente y No Importante"]
#    formatted_tasks = [format_tasks(matrix[category]) for category in categories]
#
#    return html_content.format(*formatted_tasks)
#
#def save_html_file(content, path):
#    with open(path, 'w') as file:
#        file.write(content)
#


# web/generate_html.py

def generate_html(matrix):
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title> Matriz de Eisenhower</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: center;
            }}
            th {{
                background-color: #4CAF50;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            tr:hover {{
                background-color: #ddd;
            }}
            ul {{
                list-style: none;
                padding: 0;
            }}
            li::before {{
                content: "• ";
                color: #4CAF50;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <h1>Matriz de Eisenhower</h1>
        <table>
            <tr>
                <th>Urgente e Importante</th>
                <th>No Urgente pero Importante</th>
            </tr>
            <tr>
                <td>{0}</td>
                <td>{1}</td>
            </tr>
            <tr>
                <th>Urgente pero No Importante</th>
                <th>No Urgente y No Importante</th>
            </tr>
            <tr>
                <td>{2}</td>
                <td>{3}</td>
            </tr>
        </table>
    </body>
    </html>
    """

    def format_tasks(tasks):
        if not tasks:
            return "No hay tareas en esta categoría."
        return "<ul>" + "".join([f"<li>{'✅' if completed else '❌'} {task}</li>" for _, task, completed in tasks]) + "</ul>"

    categories = ["Urgente e Importante", "No Urgente pero Importante", "Urgente pero No Importante", "No Urgente y No Importante"]
    formatted_tasks = [format_tasks(matrix[category]) for category in categories]

    return html_content.format(*formatted_tasks)

def save_html_file(content, path):
    with open(path, 'w') as file:
        file.write(content)

