# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['LSS_Reader.py'],
             pathex=['C:\\Users\\bu\\PY38\\Liquid_Surface_ChemMatCARS\\LSS_Reader'],
             binaries=[],
             datas=[('*.ui','.'),
                    ('mpl2dwidget.py','.'),
                    ('mplwidget.py','.'),
                    ('*.png','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='LSS_Reader',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='LSS_Reader')
