# Pinvestigator [3/16/2023] - Static template wont load

### Issue:

Literal Traceback:
File "C:\Users\osayi\AppData\Local\Programs\Python\Python311\Lib\site-packages\django\template\base.py", line 568, in invalid_block_tag
raise self.error
(django.template.exceptions.TemplateSyntaxError: Invalid block tag on line 8: 'static'css/base.css''. Did you forget to register or load this tag?

### Related Directory:

`C:\Users\osayi\Desktop\github_repos\Pinvestigator\pinvestigate\main\templates\main\base.html`
`C:\Users\osayi\Desktop\github_repos\Pinvestigator\pinvestigate\pinvestigate\settings.py`

### Suspicion:

Probably an error in loading static.

### Attempted Fixes:

Tried to retype `{% load static %}` in different areas in and out of html

### Solution [3/16/2023]:

`{% load static %}` at the top of html doc
`{% static 'css/base.css' %}` in base.html
Add a static files directory into settings.py as `STATIC_URL = 'static/'`

#

# Pinvestigator [03/16/2023] - base.html will not extend to index.html

### Issue:

{% extends 'main/base.html' %} is not showing up
No error
Literal text shows up on page

### Related Directory:

`C:\Users\osayi\Desktop\github_repos\Pinvestigator\pinvestigate\main\templates\main\index.html`

### Suspicion:

probably not writing in the right directory

### Attempted Fixes:

### Solution [03/16/2023]:

I was only going live with the raw html so it didnt have css. When running the server it works fine

#

# Pinvestigator [03/17/2023] - Main Background will not load images

### Issue:

Background image and related css for the main background does not load

### Related Directory:

`C:\Users\osayi\Desktop\github_repos\Pinvestigator\pinvestigate\main\templates\main\index.html`
`C:\Users\osayi\Desktop\github_repos\Pinvestigator\pinvestigate\main\static\css\index.css`
`C:\Users\osayi\Desktop\github_repos\Pinvestigator\pinvestigate\main\static\image`

### Suspicion:

Maybe I am loading the static files wrong, but I am not sure

### Attempted Fixes:

Changing the STATIC_ROOT (revert)
Changing the STATIC_URL (revert)
Clear Cache

### Solution [03/18/2023]:

Address the parent directory using `..`
`background-image: url(../image/corkbord2.jpg)`

#### Note:

Django automatically loads index files as landing page when running the website

#

# Pinvestigator [03/18/2023] - The CSS will not load and file will not extend properly

### Issue:

CSS will not load due to related `{% block %}`

### Related Directory:

`LoginPage html and css`

### Suspicion:

The issue with trying to load multiple blocks has been an issue

### Attempted Fixes:

### Solution [03/18/2023]:

Remember to put static
`{% static '/main/css/login_page_css/LoginPage.css' %}`
then put
`{% load static %}`

#### Note:

for multiple blocks in extend
`{% block name %}`
`{% endblock name %}`

keep the `extend` as the first element that is loaded

#

# Pinvestigator [] -

### Issue:

### Related Directory:

### Suspicion:

### Attempted Fixes:

### Solution []:

#### Note:

#

# Pinvestigator [] -

### Issue:

### Related Directory:

### Suspicion:

### Attempted Fixes:

### Solution []:

#### Note:

#
