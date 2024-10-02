# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

for tool in ["mitmproxy", "mitmdump", "mitmweb"]:
    excludes = []
    if tool != "mitmweb":
        excludes.append("mitmproxy.tools.web")
    if tool != "mitmproxy":
        excludes.append("mitmproxy.tools.console")

    options = []
    if tool == "mitmdump":
        # https://github.com/mitmproxy/mitmproxy/issues/6757
        options.append(("unbuffered", None, "OPTION"))

    a = Analysis(
        [tool],
        excludes=excludes,
        hiddenimports=collect_submodules('pika')+collect_submodules('rstream')+collect_submodules('mitmproxy')
    )
    pyz = PYZ(a.pure, a.zipped_data)

    EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        options,
        name=tool,
        console=True,
        icon="icon.ico",
    )
