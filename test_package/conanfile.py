#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from conans import ConanFile, CMake, tools, RunEnvironment
import os
import io


class TestPackageConan(ConanFile):
    def build(self):
        pass

    def test(self):
        output = io.StringIO()
        self.run("emcc --version", output=output)
        self.output.info(f"Installed: {str(output.getvalue())}")
        ver = str(self.requires["emsdk_installer"].conan_reference.version)
        assert(ver in str(output.getvalue()))
