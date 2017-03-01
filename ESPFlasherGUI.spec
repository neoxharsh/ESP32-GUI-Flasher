# -*- mode: python -*-

block_cipher = None


a = Analysis(['ESPFlasherGUI.py'],
             pathex=['D:\\Python\\ESPToolGUI'],
             binaries=[],
             datas=[('esptool.exe','.'),('esptool.py','.'),('espLogo.png','.'),('ICON.ico','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ESPFlasherGUI',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='ICON.ico')
