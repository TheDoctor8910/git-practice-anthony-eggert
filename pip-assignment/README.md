# PIP PIP Hooray

## Purpose of this Script
This script generates an interactable globe showing population density around the world. This serves to give users an idea of how people are dispersed and concentrated around the world.

## Steps Followed

1. Added the .zip and .shp files to the gitignore.
2. Generated a new Python project with a virtual environment in a subfolder on the repository.
3. Copied the globe.py code from the assignment.
4. Ran `pip install` with all the missing libraries from globe.py.
5. Used `pip freeze` to export the requirements to all_requirements.txt.
6. Used pipdeptree to generate dependency_tree.txt.
7. Ran `pip uninstall` on the requirements file.
8. Ran `pip install` on the requirements file to test using it on a clean environment.
9. Ran globe.py to verify the code works as expected.

## Dependency Tree
Below is the output of pipdeptree: 

geopandas==1.0.1
  - numpy [required: >=1.22, installed: 2.2.3]
  - packaging [required: Any, installed: 24.2]
  - pandas [required: >=1.4.0, installed: 2.2.3]
    - numpy [required: >=1.23.2, installed: 2.2.3]
    - python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
      - six [required: >=1.5, installed: 1.17.0]
    - pytz [required: >=2020.1, installed: 2025.1]
    - tzdata [required: >=2022.7, installed: 2025.1]
  - pyogrio [required: >=0.7.2, installed: 0.10.0]
    - certifi [required: Any, installed: 2025.1.31]
    - numpy [required: Any, installed: 2.2.3]
    - packaging [required: Any, installed: 24.2]
  - pyproj [required: >=3.3.0, installed: 3.7.1]
    - certifi [required: Any, installed: 2025.1.31]
  - shapely [required: >=2.0.0, installed: 2.0.7]
    - numpy [required: >=1.14,<3, installed: 2.2.3]

pipdeptree==2.25.0
  - packaging [required: >=24.1, installed: 24.2]
  - pip [required: >=24.2, installed: 25.0.1]

plotly==6.0.0
  - narwhals [required: >=1.15.1, installed: 1.27.1]
  - packaging [required: Any, installed: 24.2]

requests==2.32.3
  - certifi [required: >=2017.4.17, installed: 2025.1.31]
  - charset-normalizer [required: >=2,<4, installed: 3.4.1]
  - idna [required: >=2.5,<4, installed: 3.10]
  - urllib3 [required: >=1.21.1,<3, installed: 2.3.0]

setuptools==68.2.0

wheel==0.41.2

## Observations
I noticed only a few issues while working on this assignment. I had to manually start tracking all_requirements.txt and dependency_tree.txt, but that may have been a side effect of how I was working on the project and repository. I also noticed that, in the code to add a trace to the figure, marker_line_color, marker_line_width, and colorbar_title expected dictionary values instead of strings and floats.