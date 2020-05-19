# Dane code

```python

import danecode

#you can have typo errors in the arguments

department = "Santnder"
municipality = "Riongro"

municipality_data = danecode.get_data(department, municipality)

#Returns
municipality_data = {
    'department': 'Santander',
    'department_code': '68',
    'municipality': 'Rionegro',
    'municipality_code': '68615'
}

```
