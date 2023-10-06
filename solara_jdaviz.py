# Example solara script
# Requires pip installing solara
# To run: solara run solara_jdaviz.py

import solara

@solara.component
def Page():
    from jdaviz import Specviz
    from astrodbkit2.astrodb import Database

    db = Database('sqlite:///SIMPLE.db')
    t = db.query(db.Spectra).filter(db.Spectra.c.source=='TWA 26').spectra()
    spec1d = t[2]['spectrum']
    spec = Specviz()
    spec.load_data(data=spec1d)
    # spec.show()

    with solara.Column():
        solara.Markdown("# SIMPLE")

        display(spec.app)
