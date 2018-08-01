#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bincrafters import build_template_installer
import platform
import os


if __name__ == "__main__":

    builder = build_template_installer.get_builder()

    settings = dict()
    settings['arch_build'] = 'x86_64'

    if platform.system() == 'Windows':
        settings['os_build'] = 'Windows'
    elif platform.system() == 'Linux':
        settings['os_build'] = 'Linux'
    elif platform.system() == 'Darwin':
        settings['os_build'] = 'Macos'

    builder.add(settings=settings.copy())
    builder.run()
