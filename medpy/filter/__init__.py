"""
===================================================
Image filter and manipulation (:mod:`medpy.filter`)
===================================================
.. currentmodule:: medpy.filter

This package contains various image filters and image
manipulation functions.

Smoothing :mod:`medpy.filter.smoothing`
=======================================
Image smoothing / noise reduction in grayscale images.

.. module:: medpy.filter.smoothing
.. autosummary::
    :toctree: generated/

    anisotropic_diffusion
    gauss_xminus1d

Binary :mod:`medpy.filter.binary`
=================================
Binary image manipulation.

.. module:: medpy.filter.binary
.. autosummary::
    :toctree: generated/

    size_threshold
    largest_connected_component
    bounding_box

Image :mod:`medpy.filter.image`
=================================
Grayscale image manipulation.

.. module:: medpy.filter.image
.. autosummary::
    :toctree: generated/

    sls
    ssd
    average_filter
    sum_filter
    local_minima
    otsu
    resample

Label :mod:`medpy.filter.label`
=================================
Label map manipulation.

.. module:: medpy.filter.label
.. autosummary::
    :toctree: generated/

    relabel_map
    relabel
    relabel_non_zero
    fit_labels_to_mask

Noise :mod:`medpy.filter.noise`
===============================
Global and local noise estimation in grayscale images.

.. module:: medpy.filter.noise
.. autosummary::
    :toctree: generated/

    immerkaer
    immerkaer_local
    separable_convolution


Utilities :mod:`medpy.filter.utilities`
=======================================
Utilities to apply filters selectively and create your own ones.

.. module:: medpy.filter.utilities
.. autosummary::
    :toctree: generated/

    xminus1d
    intersection
    pad

Hough transform :mod:`medpy.filter.houghtransform`
==================================================
The hough transform shape detection algorithm.

.. module:: medpy.filter.houghtransform
.. autosummary::
    :toctree: generated/

    ght
    ght_alternative
    template_ellipsoid
    template_sphere

Intensity range standardization :mod:`medpy.filter.IntensityRangeStandardization`
=================================================================================
A learning method to align the intensity ranges of images.

.. module:: medpy.filter.IntensityRangeStandardization
.. autosummary::
    :toctree: generated/

    IntensityRangeStandardization

"""

# Copyright (C) 2013 Oskar Maier
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .binary import bounding_box as bounding_box
from .binary import largest_connected_component as largest_connected_component
from .binary import size_threshold as size_threshold
from .houghtransform import ght as ght
from .houghtransform import ght_alternative as ght_alternative
from .houghtransform import template_ellipsoid as template_ellipsoid
from .houghtransform import template_sphere as template_sphere
from .image import average_filter as average_filter
from .image import local_minima as local_minima
from .image import otsu as otsu
from .image import resample as resample
from .image import sls as sls
from .image import ssd as ssd
from .image import sum_filter as sum_filter
from .IntensityRangeStandardization import (
    InformationLossException as InformationLossException,
)
from .IntensityRangeStandardization import (
    IntensityRangeStandardization as IntensityRangeStandardization,
)
from .IntensityRangeStandardization import (
    SingleIntensityAccumulationError as SingleIntensityAccumulationError,
)
from .IntensityRangeStandardization import UntrainedException as UntrainedException
from .label import fit_labels_to_mask as fit_labels_to_mask
from .label import relabel as relabel
from .label import relabel_map as relabel_map
from .label import relabel_non_zero as relabel_non_zero
from .smoothing import anisotropic_diffusion as anisotropic_diffusion
from .smoothing import gauss_xminus1d as gauss_xminus1d
from .utilities import intersection as intersection
from .utilities import pad as pad
from .utilities import xminus1d as xminus1d

__all__ = [
    "largest_connected_component",
    "size_threshold",
    "bounding_box",
    "sls",
    "ssd",
    "average_filter",
    "sum_filter",
    "otsu",
    "local_minima",
    "resample",
    "anisotropic_diffusion",
    "gauss_xminus1d",
    "fit_labels_to_mask",
    "relabel",
    "relabel_map",
    "relabel_non_zero",
    "ght",
    "ght_alternative",
    "template_ellipsoid",
    "template_sphere",
    "pad",
    "intersection",
    "xminus1d",
    "IntensityRangeStandardization",
    "UntrainedException",
    "InformationLossException",
    "SingleIntensityAccumulationError",
]
