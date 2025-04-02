
<!DOCTYPE html>
<html>
    <head>
        <title>Weekly Schedule</title>
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
                margin-bottom: 20px;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
            .day-column {
                width: 20%;
            }
        </style>
    </head>
    <body>
        <h1>Weekly Schedule</h1>
        
        {% for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] %}
        <h2>{{ day }}</h2>
        <table>
            <tr>
                <th>Period</th>
                <th>Course Name</th>
                <th>Teacher</th>
                <th>Room Number</th>
            </tr>
            {% for item in schedule %}
            <tr>
                <td>{{ item[0] }}</td>
                <td>{{ item[1] }}</td>
                <td>{{ item[2] }}</td>
                <td>{{ item[3] }}</td>
            </tr>
            {% endfor %}
        </table>
        {% endfor %}
    </body>
</html>
