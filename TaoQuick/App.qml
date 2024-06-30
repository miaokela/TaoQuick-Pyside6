import QtQuick
import QtQuick.Controls
import TaoQuick

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("QML Application")

    Column {

        BasicText {
            text: "Hello World"
        }

        CusButton_Blue {
            id: myButton
            text: "Click Me"
            selected: false
            onClicked: {
                console.log("Button clicked")
            }
        }
    }
}
