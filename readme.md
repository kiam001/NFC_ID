Nextbike-Schlüsselgenerierung

Das Repo muss in Termux geclont und Python in Termux installiert sein.


Scannen Sie die Karte im Mirafare Classic Tool und kopieren Sie die UID aus dem Menüpunkt „Tools > UID Log” in die Zwischenablage.

Führen Sie dann „python reversed_hex_to_dec.py (UID einfügen)” aus.

Hinterlegen Sie die UID anschließend auf https://bikes.dvb.solutions in Ihrem Nextbike-Account.

Danke an https://gitlab.com/S60W79/nxtb-browser
