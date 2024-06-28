import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Item {
    id: card
    property string title: "Card Title"
    property bool wrapText: true // 控制文本换行模式
    default property alias content: contentContainer.data

    width: Math.max(parent.width * 0.8, 200) // 默认宽度为父级宽度的80%，但不小于200
    implicitHeight: columnLayout.implicitHeight + 20 // 动态调整高度以适应内容

    Rectangle {
        id: background
        anchors.fill: parent
        color: "#232324" // RGB(35, 35, 36)
        border.color: "#363637" // RGB(54, 54, 55)
        border.width: 2
        radius: 10

        Column {
            id: columnLayout
            anchors.fill: parent
            anchors.margins: 10
            spacing: 10

            Text {
                id: titleText
                text: card.title
                font.pixelSize: 20
                color: "white"
                wrapMode: card.wrapText ? Text.WordWrap : Text.NoWrap
                elide: card.wrapText ? Text.ElideNone : Text.ElideRight
            }

            Column {
                id: contentContainer
                width: parent.width
                spacing: 10
            }
        }
    }
}