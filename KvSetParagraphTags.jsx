// KvSetParagraphTags

#target InDesign

var ErrCounter = 0;
var ErrMessage = '';

function SetParagraphTag(group, style, tag, tagClass) {
    try {
        var myStyle = app.activeDocument.paragraphStyleGroups.itemByName(group).paragraphStyles.itemByName(style);
        if (myStyle.styleExportTagMaps.length === 0) {
            myStyle.styleExportTagMaps.add('EPUB', tag, tagClass, '');
            myStyle.styleExportTagMaps[0].emitCss = false;
        } else {
            for (j=0; myStyle.styleExportTagMaps.length>j; j++) {
                myStyle.styleExportTagMaps[j].remove();
            }
            myStyle.styleExportTagMaps.add('EPUB', tag, tagClass, '');
            myStyle.styleExportTagMaps[0].emitCss = false;
        }
    } catch (err) {
    	var ErrOut = "Отсутствует стиль абзаца \"" + group + ": " + style + "\"";
        $.writeln (ErrOut);
        ErrCounter++;
        ErrMessage = ErrMessage + ErrOut + '\n';
    }
}

function SetCharacterTag(group, style, tag, tagClass) {
    try {
        var myStyle = app.activeDocument.characterStyleGroups.itemByName(group).characterStyles.itemByName(style);
        if (myStyle.styleExportTagMaps.length === 0) {
        myStyle.styleExportTagMaps.add('EPUB', tag, tagClass, '');
        myStyle.styleExportTagMaps[0].emitCss = false;
        } else {
            for (j=0; myStyle.styleExportTagMaps.length>j; j++) {
                myStyle.styleExportTagMaps[j].remove();
            }
            myStyle.styleExportTagMaps.add('EPUB', tag, tagClass, '');
            myStyle.styleExportTagMaps[0].emitCss = false;
        }
    } catch (err) {
        var ErrOut = "Отсутствует стиль символа " + group + ": " + style;
        $.writeln (ErrOut);
        ErrCounter++;
        ErrMessage = ErrMessage + ErrOut + '\n';
    }
}


var classKill = 'kill';

var arrPS1 = [
    ['Заголовок 18', 'h1', classKill],
    ['Подзаголовок в тексте', 'h3', classKill],
    ['Основной 8', 'p', classKill],
    ['Стих', 'p', 'lyric'],
    ['Основной 8 (буквица)', 'p', classKill],
    ['бе', 'p', classKill],
    ['Основной 8 (маркер)', 'li', classKill],
    ['Основной 8 (маркер точка)', 'li', classKill],
    ['Основной 8 (нумер 111)', 'li', classKill],
    ['Основной 8 (нумер 123)', 'li', classKill],
    ['Уважаемые', 'h4', classKill,],
    ['Подверсток 1', 'p', classKill],
    ['Подверсток список', 'li', classKill],
    ['ЛИД', 'p', 'big'],
    ['Подпись', 'p', 'signed'],
    ['Врезка_цитата', 'div', classKill],
    ['foto_podp', 'div', classKill],
    ['foto_podp_author', 'p', classKill],
    ['Рубрика 1', 'div', classKill],
    ['Рубрика 2', 'div', classKill],
    ['Рубрика 3', 'div', classKill],
    ['Рубрика 3_2', 'div', classKill],
    ['Рубрика 5', 'div', classKill],
    ['Заголовок 48', 'h1', classKill],
    ['Заголовок 36', 'h1', classKill],
    ['Заголовок 24', 'h1', classKill],
    ['Подзаголовок 18', 'h2', classKill],
];

var arrPS2 = [
    ['table_L', 'p', classKill],
    ['table_BL', 'p', classKill],
    ['table_BR', 'p', classKill],
    ['table_C', 'p', classKill],
    ['table_BC', 'p', classKill],
    ['table_R', 'p', classKill],
];

var arrCS1 = [
    ['Точка колонтитула', 'span', classKill],
    ['точка маркер', 'span', classKill],
    ['Bold', 'strong', classKill],
    ['Italic', 'em', classKill],
    ['Выделение в тексте', 'strong', classKill],
    ['Буквица', 'span', classKill],
];

function main() {
    for (i = 0; arrPS1.length>i; i++) {
        SetParagraphTag('верстка', arrPS1[i][0], arrPS1[i][1], arrPS1[i][2]);
    }
    for (i = 0; arrPS2.length>i; i++) {
        SetParagraphTag('Таблица', arrPS2[i][0], arrPS2[i][1], arrPS2[i][2]);
    }
    for (i = 0; i < arrCS1.length; i++) {
        SetCharacterTag('верстка', arrCS1[i][0], arrCS1[i][1], arrCS1[i][2]);
    };
    
    if (ErrCounter > 0) {
    	alert ('ОШИБКИ! Количество: ' + ErrCounter + 'шт.\n' + ErrMessage);
    } else {
        $.writeln ('Готово!');
    	alert ('Готово!');
    }
}

app.doScript(main, ScriptLanguage.JAVASCRIPT, [], UndoModes.ENTIRE_SCRIPT, "KvSetParagraphTags");