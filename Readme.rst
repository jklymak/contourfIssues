================================================================
Issues with contourf and pcolor and anti-aliasing in pdf viewers
================================================================

``contourf`` and ``pcolormesh`` can look bad in pdf viewers, with lots
of extra "gridlines" or lines around the boundaries of the contours.

.. figure:: exampleContour.pdf.png
   :alt: example contour.pdf

   This is an example contourf (converted to png at 100 dpi to mimic
   what a screen would show).

The same plot rendered by Matplotlib into a 100-dpi png does not have the
extra whitish dashed lines around each contour

.. figure:: exampleContour.png
   :alt: example contour.pdf

   This is an example contourf directly printed to a 100-dpi png.
