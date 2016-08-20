### 
KvSetParagraphTags v. 1.0.2
Adobe InDesign script
vetl1489

###

#target InDesign

errCounter = 0
errMessage =""
classKill = "kill"

arrPS1 = [
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
]

arrPS2 = [
  ['table_L', 'p', classKill],
  ['table_BL', 'p', classKill],
  ['table_BR', 'p', classKill],
  ['table_C', 'p', classKill],
  ['table_BC', 'p', classKill],
  ['table_R', 'p', classKill],
]

arrCS1 = [
  ['Точка колонтитула', 'span', classKill],
  ['точка маркер', 'span', classKill],
  ['Bold', 'strong', classKill],
  ['Italic', 'em', classKill],
  ['Выделение в тексте', 'strong', classKill],
  ['Буквица', 'span', classKill],
]

setTag = (selectStyle = "character", group, style, tag, tagClass) ->
  try
    if selectStyle is "paragraph"
    then myStyle = app.activeDocument.paragraphStyleGroups.itemByName(group).paragraphStyles.itemByName(style)
    else myStyle = app.activeDocument.characterStyleGroups.itemByName(group).characterStyles.itemByName(style)
    if myStyle.styleExportTagMaps.length is 0
      myStyle.styleExportTagMaps.add 'EPUB', tag, tagClass, ''
      myStyle.styleExportTagMaps[0].emitCss = false
      return
    else
      do myStyle.styleExportTagMaps[j].remove for j in myStyle.styleExportTagMaps.length
      myStyle.styleExportTagMaps.add 'EPUB', tag, tagClass, ''
      myStyle.styleExportTagMaps[0].emitCss = false
      return
  catch
    errOut = "Отсутствует стиль абзаца \"#{group}: #{style}\""
    $.writeln (errOut);
    errCounter++;
    errMessage = errMessage + errOut + "\n";

main = ->
  setTag("paragraph", "верстка", i[0], i[1], i[2]) for i in arrPS1
  setTag("paragraph", "Таблица", i[0], i[1], i[2]) for i in arrPS2
  setTag("character", "верстка", i[0], i[1], i[2]) for i in arrCS1
  if errCounter > 0 then alert "ОШИБКИ! Количество: #{errCounter} шт.\n #{errMessage}"
  else $.writeln 'Готово!'
  alert 'Готово!'

app.doScript main, ScriptLanguage.JAVASCRIPT, [], UndoModes.ENTIRE_SCRIPT, "KvSetParagraphTags"




