# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.7.0
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x03\x7f\
i\
mport QtQuick\x0aim\
port QtQuick.Con\
trols\x0aimport QtQ\
uick.Layouts\x0aimp\
ort \x22qrc:/Contro\
ls\x22\x0a\x0aApplication\
Window {\x0a    vis\
ible: true\x0a    w\
idth: 640\x0a    he\
ight: 480\x0a    ti\
tle: \x22Hello QML\x22\
\x0a    color: \x22#2a\
2a2b\x22\x0a\x0a    Colum\
n {\x0a        anch\
ors.fill: parent\
\x0a        anchors\
.centerIn: paren\
t\x0a        Card {\
\x0a            tit\
le: \x22Custom Card\
 Title\x22\x0a        \
    wrapText: tr\
ue // \xe8\xae\xbe\xe7\xbd\xae\xe4\xb8\xba \
true \xe4\xbb\xa5\xe5\x90\xaf\xe7\x94\xa8\xe6\x8d\
\xa2\xe8\xa1\x8c\xef\xbc\x8cfalse \xe4\xbb\xa5\
\xe9\x9a\x90\xe8\x97\x8f\xe8\xb6\x85\xe5\x87\xba\xe9\x83\xa8\xe5\
\x88\x86\x0a\x0a            \
// \xe8\x87\xaa\xe5\xae\x9a\xe4\xb9\x89\xe5\x86\x85\xe5\
\xae\xb9\x0a            T\
ext {\x0a          \
      text: \x22Thi\
s is a custom te\
xt inside the ca\
rd. This text is\
 very long and s\
hould be either \
wrapped or elide\
d based on the w\
rapText property\
.\x22\x0a             \
   font.pixelSiz\
e: 16\x0a          \
      color: \x22wh\
ite\x22\x0a           \
 }\x0a\x0a            \
Button {\x0a       \
         text: \x22\
Click Me\x22\x0a      \
          onClic\
ked: {\x0a         \
           conso\
le.log(\x22Button c\
licked!\x22)\x0a      \
          }\x0a    \
        }\x0a      \
  }\x0a\x0a    }\x0a\x0a}\x0a\
\x00\x00\x04\xa2\
i\
mport QtQuick 2.\
15\x0aimport QtQuic\
k.Controls 2.15\x0a\
import QtQuick.L\
ayouts 1.15\x0a\x0aIte\
m {\x0a    id: card\
\x0a    property st\
ring title: \x22Car\
d Title\x22\x0a    pro\
perty bool wrapT\
ext: true // \xe6\x8e\xa7\
\xe5\x88\xb6\xe6\x96\x87\xe6\x9c\xac\xe6\x8d\xa2\xe8\xa1\x8c\xe6\
\xa8\xa1\xe5\xbc\x8f\x0a    defaul\
t property alias\
 content: conten\
tContainer.data\x0a\
\x0a    width: Math\
.max(parent.widt\
h * 0.8, 200) //\
 \xe9\xbb\x98\xe8\xae\xa4\xe5\xae\xbd\xe5\xba\xa6\xe4\xb8\xba\
\xe7\x88\xb6\xe7\xba\xa7\xe5\xae\xbd\xe5\xba\xa6\xe7\x9a\x848\
0%\xef\xbc\x8c\xe4\xbd\x86\xe4\xb8\x8d\xe5\xb0\x8f\xe4\xba\
\x8e200\x0a    implici\
tHeight: columnL\
ayout.implicitHe\
ight + 20 // \xe5\x8a\xa8\
\xe6\x80\x81\xe8\xb0\x83\xe6\x95\xb4\xe9\xab\x98\xe5\xba\xa6\xe4\
\xbb\xa5\xe9\x80\x82\xe5\xba\x94\xe5\x86\x85\xe5\xae\xb9\x0a\x0a\
    Rectangle {\x0a\
        id: back\
ground\x0a        a\
nchors.fill: par\
ent\x0a        colo\
r: \x22#232324\x22 // \
RGB(35, 35, 36)\x0a\
        border.c\
olor: \x22#363637\x22 \
// RGB(54, 54, 5\
5)\x0a        borde\
r.width: 2\x0a     \
   radius: 10\x0a\x0a \
       Column {\x0a\
            id: \
columnLayout\x0a   \
         anchors\
.fill: parent\x0a  \
          anchor\
s.margins: 10\x0a  \
          spacin\
g: 10\x0a\x0a         \
   Text {\x0a      \
          id: ti\
tleText\x0a        \
        text: ca\
rd.title\x0a       \
         font.pi\
xelSize: 20\x0a    \
            colo\
r: \x22white\x22\x0a     \
           wrapM\
ode: Text.WordWr\
ap\x0a             \
   elide: Text.E\
lideNone\x0a       \
     }\x0a\x0a        \
    Column {\x0a   \
             id:\
 contentContaine\
r\x0a              \
  width: parent.\
width\x0a          \
      spacing: 1\
0\x0a            }\x0a\
        }\x0a    }\x0a\
}\
"

qt_resource_name = b"\
\x00\x08\
\x06[\x9fs\
\x00C\
\x00o\x00n\x00t\x00r\x00o\x00l\x00s\
\x00\x05\
\x00\x5c\xfc\xe3\
\x00V\
\x00i\x00e\x00w\x00s\
\x00\x07\
\x08sX\xfc\
\x00a\
\x00p\x00p\x00.\x00q\x00m\x00l\
\x00\x08\
\x08\x87a\x1c\
\x00C\
\x00a\x00r\x00d\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x16\x00\x02\x00\x00\x00\x01\x00\x00\x00\x04\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00:\x00\x00\x00\x00\x00\x01\x00\x00\x03\x83\
\x00\x00\x01\x90Y\xf8\xc9\xc0\
\x00\x00\x00&\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x90Y\xf7\xd9\xcb\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
