# trafficology

Using Python 3.11.3, PostgreSQL 16

## Dev Setup

1. Install [pip](https://pip.pypa.io/en/stable/getting-started/) 
2. Install [pipx](https://github.com/pypa/pipx) (required for poetry installation), `py -m pip install --user pipx`
3. Install [poetry](https://python-poetry.org/docs/), `pipx install poetry`
4. Setup environment variables
5. Run `poetry install` to install project dependencies
6. Install [Anaconda](https://www.anaconda.com/) (required for postGIS installation)

---
Can't get the following to work with Windows... cmake causing the trouble.

7. Install [postGIS](https://postgis.net/)
   - Install [GEOS](https://libgeos.org/usage/download/) (version 3.12.1)
     - [cmake](https://cmake.org/download/)
     - [Visual Studio C++](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)
     - [Doxygen](https://www.doxygen.nl/)
   - Install [Proj](https://proj.org/en/9.3/install.html) (version 9.3)
   - Install [GDAL](https://gdal.org/download.html) (version 3.8.3)
---