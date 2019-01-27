import sqlite3

connection = sqlite3.connect("base.db")
cursor = connection.cursor()

sql_themes = 'SELECT * FROM themes'
cursor.execute(sql_themes)
themes = {}
for i in cursor.fetchall():
    themes[i[0]] = i[1]

sql_questions = 'SELECT * FROM questions ORDER BY date(Date) DESC' # ASC
cursor.execute(sql_questions)
questions = cursor.fetchall()
for i in questions:
    print("{date} | {title} | {theme} | {lvl}".format(date = i[-1], title = i[1], theme = themes[i[3]], lvl=i[-2]))

print(themes)
theme = int(input('Введите номер темы: '))
theme = (theme,)
sql_theme = 'SELECT Title, Url FROM questions WHERE theme=?'
cursor.execute(sql_theme, theme)
theme_notes = cursor.fetchall()
print(theme_notes)
print(len(theme_notes))

connection.close()