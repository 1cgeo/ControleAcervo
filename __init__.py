# -*- coding: utf-8 -*-

def classFactory(iface):
    from .pluginMain import PluginControleAcervo
    return PluginControleAcervo(iface)