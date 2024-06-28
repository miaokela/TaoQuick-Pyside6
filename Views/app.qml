import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "qrc:/Controls"

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "Hello QML"
    color: "#2a2a2b"

    Column {
        anchors.fill: parent
        anchors.centerIn: parent
        Card {
            title: "Custom Card Title"
            wrapText: true // 设置为 true 以启用换行，false 以隐藏超出部分

            // 自定义内容
            Text {
                text: "This is a custom text inside the card. This text is very long and should be either wrapped or elided based on the wrapText property."
                font.pixelSize: 16
                color: "white"
            }

            Button {
                text: "Click Me"
                onClicked: {
                    console.log("Button clicked!")
                }
            }
        }

    }

}
