# WinHostsFileUpdater

## Übersicht

**HostsFileUpdater** ist ein Python-Skript, das die Hosts-Datei Ihres Windows-Systems automatisch aktualisiert. Es überprüft die Internetverbindung und Administratorrechte, lädt eine neue Hosts-Datei herunter, benennt die alte Hosts-Datei um und ersetzt sie durch die neue Datei. Schließlich leert es den DNS-Cache, um sicherzustellen, dass die Änderungen sofort wirksam werden.

## Funktionen

- Überprüft die Internetverbindung
- Überprüft Administratorrechte
- Lädt eine neue Hosts-Datei herunter
- Bennent die bestehende Hosts-Datei um
- Verschiebt die heruntergeladene Datei in das Systemverzeichnis
- Leert den DNS-Cache

## Voraussetzungen

- Python 3.x
- Administratorrechte
- Internetverbindung

## Installation

1. Klonen Sie das Repository:
    ```bash
    git clone https://github.com/IhrBenutzername/HostsFileUpdater.git
    ```
2. Navigieren Sie in das Verzeichnis:
    ```bash
    cd HostsFileUpdater
    ```

## Nutzung

1. Stellen Sie sicher, dass Sie das Skript mit Administratorrechten ausführen.
2. Führen Sie das Skript aus:
    ```bash
    python main.py
    ```

## Detaillierte Funktionsweise

1. **Überprüfung der Internetverbindung**: Das Skript prüft, ob eine Verbindung zu Google hergestellt werden kann.
2. **Überprüfung der Administratorrechte**: Das Skript überprüft, ob es mit Administratorrechten ausgeführt wird.
3. **Herunterladen der Datei**: Die neue Hosts-Datei wird von der angegebenen URL heruntergeladen und lokal gespeichert.
4. **Umbenennen der bestehenden Hosts-Datei**: Die vorhandene Hosts-Datei wird in `hosts_{datum}.old` umbenannt.
5. **Verschieben und Umbenennen der heruntergeladenen Datei**: Die heruntergeladene Datei wird in das Systemverzeichnis verschoben und in `hosts` umbenannt.
6. **Leeren des DNS-Caches**: Der DNS-Cache wird geleert, um die Änderungen sofort wirksam zu machen.

## Fehlerbehandlung

- Falls keine Internetverbindung besteht, wird eine entsprechende Fehlermeldung ausgegeben.
- Falls das Skript nicht mit Administratorrechten ausgeführt wird, wird eine entsprechende Fehlermeldung ausgegeben.
- Falls der Download fehlschlägt, wird eine entsprechende Fehlermeldung mit dem HTTP-Statuscode ausgegeben.
- Falls die bestehende Hosts-Datei nicht gefunden wird, wird eine entsprechende Fehlermeldung ausgegeben.
- Falls die Datei nicht verschoben werden kann, wird eine entsprechende Fehlermeldung ausgegeben.
- Falls das Leeren des DNS-Caches fehlschlägt, wird eine entsprechende Fehlermeldung ausgegeben.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Die vollständige Lizenz finden Sie in der [LICENSE](LICENSE)-Datei.

Hinweis: Die nachfolgende Übersetzung ist nur zur Information. Der offizielle und rechtlich bindende Text der MIT-Lizenz ist auf Englisch.

**Deutsche Übersetzung (informell)**:

MIT-Lizenz

Copyright (c) 2024 Ihr Name

Hiermit wird unentgeltlich jeder Person, die eine Kopie der Software und der zugehörigen Dokumentationsdateien (die "Software") erhält, die Erlaubnis erteilt, uneingeschränkt mit der Software zu handeln, einschließlich, aber nicht beschränkt auf, das Recht, sie zu nutzen, zu kopieren, zu ändern, zusammenzuführen, zu veröffentlichen, zu verbreiten, unterzulizenzieren und/oder zu verkaufen, und Personen, denen diese Software zur Verfügung gestellt wird, diese Rechte zu verschaffen, unter den folgenden Bedingungen:

Der obige Urheberrechtshinweis und dieser Erlaubnishinweis sind in allen Kopien oder wesentlichen Teilen der Software beizufügen.

DIE SOFTWARE WIRD OHNE JEDE AUSDRÜCKLICHE ODER IMPLIZIERTE GARANTIE BEREITGESTELLT, EINSCHLIESSLICH DER GARANTIEN DER MARKTGÄNGIGKEIT, DER EIGNUNG FÜR EINEN BESTIMMTEN ZWECK UND DER NICHTVERLETZUNG. IN KEINEM FALL SIND DIE AUTOREN ODER URHEBER FÜR JEGLICHE ANSPRÜCHE, SCHÄDEN ODER SONSTIGE HAFTUNGEN VERANTWORTLICH, OB IN EINEM VERTRAG, EINER UNERLAUBTEN HANDLUNG ODER ANDERWEITIG, DIE SICH AUS DER SOFTWARE ODER DER VERWENDUNG ODER ANDEREN GESCHÄFTEN MIT DER SOFTWARE ERGEBEN.

## Kontakt

Bei Fragen oder Problemen wenden Sie sich bitte an [Ihr Name](mailto:IhreEmail@example.com).
