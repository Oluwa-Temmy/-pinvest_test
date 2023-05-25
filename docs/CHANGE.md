b# Change Log

Here is where you can find the history map of Pinvestigator website

<!--## [Unreleased] - yyyy-mm-dd

Here we write upgrading notes for brands. It's a team effort to make them as
straightforward as possible.

### Added

- [PROJECTNAME-XXXX](http://tickets.projectname.com/browse/PROJECTNAME-XXXX)
  MINOR Ticket title goes here.
- [PROJECTNAME-YYYY](http://tickets.projectname.com/browse/PROJECTNAME-YYYY)
  PATCH Ticket title goes here.

### Changed

### Fixed-->

# [Unreleased] - yet-to-come

This update will mainly focus on general user authentication and general user profiling

### Added

- Users will be able to authenticate or login into their accounts with other social apps (i.e. gmail, github, twitter) with the integrated `django-allauth` package

- General user profiles will be added, of course with limited customizations.

### Changed

- HTMX will handle the post method and targets from the login and signup page

  > - User Interactions: Makes it easier for users to spot errors upon signin or login by not refreshing the page and leaving data on form.
  > - follow DRY principle

### Fixed

- (Minor) Submit button: Submit button for login form and signup form is now visible

# :fire: Minor Dev Update [0.3.0] - 2023-05-25

This is a minor update that pertains to the structure
and backend of the website that is useful for devs and contributors.

## :heavy_plus_sign: Added

### :briefcase: Packages

`django-sass`</br>
Django integrated sass is now being used to keep style consistency
through out the project. Instead of interacting with CSS directly,

> - Install django-sass(Installation link below)
> - Create a CSS folder and a Sass folder
> - In Command Line `python manage.py sass input/path/to/sass/folder output/path/to/css/folder --watch`
> - Begin creating files within the sass folder with the `.scss` extension

Django integrated Sass Repo -> [django-sass](https://github.com/coderedcorp/django-sass)</br>
Documentation -> [Sass](https://sass-lang.com/)

</br>

`django-crispy-forms`</br>
Django crispy forms now being used in order to make form rendering efficient and code more readable and reusable for the devs.

> - Follow install instruction `django-crispy-forms`
> - Create a file that creates form fields (Follow django fields documentation)

### :triangular_ruler: Project Structure Change

The project templates now uses Class-Based rendering to make pages more functional in less code.

### Fixed

- [PROJECTNAME-TTTT](http://tickets.projectname.com/browse/PROJECTNAME-TTTT)
  PATCH Add logic to runsheet teaser delete to delete corresponding
  schedule cards.-->

#

## [0.2.0] - 2023-05-08

This update is based on better pages.
Homepage update
Base

### Added

None

### Changed

None

<!--- [PROJECTNAME-ZZZZ](http://tickets.projectname.com/browse/PROJECTNAME-ZZZZ)
  PATCH Drupal.org is now used for composer.-->

### Fixed

- BASE page is more organized and fixed names
- Organized Bootstrap npm modules
- Fixed Header intro for homepage

<!--## [1.2.4] - 2017-03-15

Here we would have the update steps for 1.2.4 for people to follow.

### Added

### Changed

- [PROJECTNAME-ZZZZ](http://tickets.projectname.com/browse/PROJECTNAME-ZZZZ)
  PATCH Drupal.org is now used for composer.

### Fixed

- [PROJECTNAME-TTTT](http://tickets.projectname.com/browse/PROJECTNAME-TTTT)
  PATCH Add logic to runsheet teaser delete to delete corresponding
  schedule cards.-->

> <sub>The format is based on [Keep a Changelog](http://keepachangelog.com/)
> and this project adheres to [Semantic Versioning](http://semver.org/).</sub>
