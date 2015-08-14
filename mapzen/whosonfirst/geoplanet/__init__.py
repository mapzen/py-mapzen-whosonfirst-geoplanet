# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

import sqlite3

class names:

    def __init__(self, db_path):

        db_conn = sqlite3.connect(db_path)
        db_curs = db_conn.cursor()

        self.db_path = db_path
        self.db_conn = db_conn
        self.db_curs = db_curs

    # please to be writing function to index/import names

    def append_names(self, feature):

        props = feature['properties']
        wofid = props['wof:id']

        concordances = props.get('wof:concordances', {})
        gpid = concordances.get('gp:id', None)

        if gpid == None:
            return False

        sql = "SELECT * FROM names WHERE id=?"
        params = (gpid,)

        self.db_curs.execute(sql, params)
        rows = self.db_curs.fetchall()

        if len(rows) == 0:
            return False

        langs = []

        if len(rows) == 0:
            return True

        for r in rows:

            ignore, name, lang, type = r

            lang = lang.lower()

            if not type:
                type = "p"
            else:
                type = type.lower()
                
            if lang != "eng" and type == "q":
                type = "p"

            if type == "p" and not lang in langs:
                langs.append(lang)

            k = "name:%s_%s" % (lang, type)
            # print "%s = %s" % (k, name)
            # names +=  1

            n = props.get(k, [])

            if not name in n:
                n.append(name)

            props[k] = n

        # props['wof:languages'] = langs
        
        feature['properties'] = props
        return True

