from setuptools import setup

APP = ['menubar_app.py']
DATA_FILES = [
    ('icons', [
        'icons/menubar_icon.png',
        'icons/icon.icns',
        'icons/Autology_icon.icns'
    ])
]
OPTIONS = {
    'argv_emulation': False,
    'packages': [
        'websockets', 
        'asyncio', 
        'objc', 
        'Foundation', 
        'AppKit', 
        'CoreFoundation',
        'importlib',
        'threading'
    ],
    'includes': [
        'importlib.machinery',
        'importlib.util',
        'threading',
        'Foundation',
        'AppKit',
        'objc',
        'CoreFoundation',
        'CoreFoundation._CoreFoundation',
        'CoreFoundation._inlines',
        'Foundation._Foundation',
        'Foundation._inlines',
        'AppKit._AppKit',
        'AppKit._inlines',
        'objc._objc',
        'objc._machsignals'
    ],
    'resources': ['icons'],
    'frameworks': ['Python.framework'],
    'plist': {
        'CFBundleName': 'Autology Remote Connect',
        'LSUIElement': True,
        'NSHighResolutionCapable': True,
        'NSAppleEventsUsageDescription': 'Aplikacja wymaga dostępu do menu systemowego',
        'NSPrincipalClass': 'NSApplication',
    },
    'iconfile': 'icons/icon.icns',
}

setup(
    app=APP,
    name="Autology Remote Connect",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
) 