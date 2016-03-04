# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FeatureClassHopper
                                 A QGIS plugin
 allows to step through the display of classified atributes
                             -------------------
        begin                : 2016-03-04
        copyright            : (C) 2016 by Quentin Bitram
        email                : Qu-Bit@users.noreply.github.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load FeatureClassHopper class from file FeatureClassHopper.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ft_class_hopper import FeatureClassHopper
    return FeatureClassHopper(iface)
