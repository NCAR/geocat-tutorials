.. geocat-tutorials documentation master file, created by
   sphinx-quickstart on Fri Oct  7 11:21:01 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

GeoCAT-tutorials
=================
Welcome to GeoCAT-tutorials! This version of this content was made for 
presentation at the Fall 2022 ESDS event.

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: GeoCAT

   Overview <./notebooks/geocat/00-Overview.ipynb>
   GeoCAT Project Structure <./notebooks/geocat/01-Structure.ipynb>

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: GeoCAT-viz

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: GeoCAT-comp

   Introduction <./notebooks/geocat-comp/00-Introduction.ipynb>
   A Soft Starter: Relative Humidity <./notebooks/geocat-comp/01-using_geocat_comp.ipynb>
   A More Complicated Example: Calculating Climatological Averages <./notebooks/geocat-comp/02-more_advanced_functionality.ipynb>

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: UXarray


.. grid:: 1 1 2 2
    :gutter: 2

    .. grid-item-card:: GeoCAT Overview
         :link: ./notebooks/geocat/00-Overview.ipynb

         GeoCAT team and projects

    .. grid-item-card:: GeoCAT-viz
   
         GeoCAT's visualization library

    .. grid-item-card:: GeoCAT-comp
         :link: ./notebooks/geocat-comp/00-Introduction.ipynb

         GeoCAT's computational library

    .. grid-item-card:: UXarray
        
         Tools for unstructured grids
