import os
import glob
import shutil

for path in glob.glob('scratch-gui/build/*.html'):
  with open(path, 'r') as fr:
    print(f"Patching HTML {path}")
    contents = fr.read()
    contents = contents.replace('</head>', '<meta name="robots" content="noindex"></head>')
    contents = contents.replace('<link rel="manifest" href="manifest.webmanifest">', '')
    with open(path, 'w') as fw:
      fw.write(contents)

os.remove('scratch-gui/build/sw.js')
os.remove('scratch-gui/build/manifest.webmanifest')
os.remove('scratch-gui/build/fullscreen.html')
os.remove('scratch-gui/build/embed.html')
os.remove('scratch-gui/build/index.html')

shutil.copy('scratch-gui/build/editor.html', 'scratch-gui/build/index.html')
shutil.copy('robots.txt', 'scratch-gui/build/robots.txt')
