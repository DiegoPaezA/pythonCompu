# -*- mode: python -*-

block_cipher = None


a = Analysis(['control.py'],
             pathex=['/home/diegopaez/PycharmProjects/VFCMarjorie2'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)
pyz = PYZ(a.pure,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas +=  ,
          name='control',
          debug=False,
          strip=None,
          upx=True,
          console=False )
