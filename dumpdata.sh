#!/bin/sh
mkdir -p workdir/fixtures
./manage.py dumpdata --indent=2 --natural-foreign email_auth cmsplugin_cascade.cascadeclipboard cmsplugin_cascade.pluginextrafields cmsplugin_cascade.sharedglossary filer post_office.emailtemplate shop --exclude filer.clipboard --exclude filer.clipboarditem --exclude filer.file > workdir/fixtures/skeleton.json
