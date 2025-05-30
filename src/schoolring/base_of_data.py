import sqlite3
import datetime


class DataBaseManager:

    def __init__(self):
        pass

    def add_user(self, data):
        """Adds a new user to the system"""

        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'INSERT INTO users(login, password, school_num, building_num, phone_num, FIO) ' \
                 f'VALUES("{data.login}", "{data.repeat_password}", "{int(data.school_num)}", ' \
                 f'"{int(data.building_num)}", "{data.phone_num}", "{data.FIO}")'

        cur.execute(comand).fetchall()
        con.commit()

    def get_user_name(self, id):
        pass

    def serch_logins(self, login) -> list:
        """Get a list of logins of all existing users"""

        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'SELECT login FROM users WHERE login="{login}"'
        logins = [i[0] for i in cur.execute(comand).fetchall()]
        return logins

    def get_FIO(self, login):
        """Getting a full name from the lign database"""

        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'SELECT FIO FROM users WHERE login="{login}"'
        FIO = [i[0] for i in cur.execute(comand).fetchall()]
        return FIO

    def get_password(self, login):
        """Finds the user's password by login"""

        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'SELECT password FROM users WHERE login="{login}"'
        return cur.execute(comand).fetchall()

    def get_schedule_today(self, template_id):
        """Gets the call schedule for today"""

        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'SELECT play_time, music, title FROM schedule WHERE template={template_id}'
        return cur.execute(comand).fetchall()

    def get_list_template(self):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'SELECT title FROM template'
        return cur.execute(comand).fetchall()

    def get_schedule(self, template):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        template_id = cur.execute(f'SELECT id FROM template WHERE title="{template}"').fetchall()[0][0]
        comand = f'SELECT title, play_time, music FROM schedule WHERE template = "{template_id}"'
        return cur.execute(comand).fetchall()

    def save_shedule_row(self, data: list, temp_id):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'INSERT INTO schedule(title, play_time, music, template) ' \
                 f'VALUES("{data[0]}", "{data[1]}", "{data[2]}", "{temp_id}")'
        cur.execute(comand).fetchall()
        con.commit()

    def get_all_templates(self):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        templates = cur.execute(f'SELECT title FROM template WHERE NOT (title is NULL )').fetchall()
        finish_lst = [i[0] for i in templates]
        return finish_lst

    def get_active_templates(self):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        templates = cur.execute(f'SELECT title, date FROM template WHERE NOT (date is NULL)').fetchall()
        return templates

    def get_id_template(self, title):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        templates = cur.execute(f'SELECT id FROM template WHERE title="{title}"').fetchall()
        if templates:
            return templates[0]
        else:
            return ''

    def add_special_date(self, template, date):
        print('true save')
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'INSERT INTO template(title, date, default) ' \
                 f'VALUES("{template}", "{date}", "{0}")'
        cur.execute(comand).fetchall()
        con.commit()

    def update_special_date(self, template, date, id):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'UPDATE template(title, date) ' \
                 f'SET("{template}", "{date}")' \
                 f'WHERE id="{id}"'
        cur.execute(comand).fetchall()
        con.commit()

    def delete_special_date(self, template, date):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'DELETE FROM template ' \
                 f'WHERE title="{template}" AND date="{date}"'
        cur.execute(comand).fetchall()
        con.commit()

    def get_list_template_for_comobox(self):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'SELECT title FROM template WHERE date is NULL'
        return cur.execute(comand).fetchall()

    def add_template(self, name):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'INSERT INTO template(title)' \
                 f'VALUES("{name}")'
        cur.execute(comand).fetchall()
        con.commit()

    def save_default(self, title):
        self._clear()
        self._set(title)

    def _clear(self):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'UPDATE template ' \
                 f'SET "default"=0'
        cur.execute(comand).fetchall()
        con.commit()

    def _set(self, title):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'UPDATE template ' \
                 f'SET "default"=1 ' \
                 f'WHERE title="{title}"'
        cur.execute(comand).fetchall()
        con.commit()

    def get_default_schedule(self):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'SELECT play_time, music, title FROM schedule ' \
                 f'WHERE template in (SELECT id FROM template WHERE "default"=1)'
        result = cur.execute(comand).fetchall()
        return result

    def check_udate_default(self):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'SELECT "default" FROM template'
        result = cur.execute(comand).fetchall()
        finish = []
        print(result)
        for i in result:
            finish.append(i[0])
        return finish

    def get_special_date_on_today(self):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        a = f"{datetime.date.today(): %d-%m-%Y}"
        date = a.replace('-', '.')
        date = date.replace(' ', '')
        comand = f'SELECT id FROM template WHERE date="{date}"'
        result = cur.execute(comand).fetchall()
        print(result)
        try:
            return result[0][0]
        except Exception:
            return []

    def clear_changes(self):
        self._clear()

    def get_perents_tempolate_id(self, special_id):
        con = sqlite3.connect('./DB/schoolring.sqlite')
        cur = con.cursor()
        comand = f'SELECT id FROM template WHERE title in (SELECT title FROM template WHERE id={special_id}) ' \
                 f'AND date IS NULL'
        result = cur.execute(comand).fetchall()
        return result[0][0]
