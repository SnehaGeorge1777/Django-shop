# SoftSec Shop

This project is generated as an implementation of [Django-Shop](https://django-shop.readthedocs.io/) for the teaching purposes at SoftSec institute.

## Requirements
* Python 3.9
* NodeJS 20
* NPM 10

## Setup
```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
npm install
```

## Initialize and Run server
```bash
pipenv run ./manage.py initialize_shop_demo # only run this if the database is not initialized

pipenv run ./manage.py runserver
```

## Add new feature / page
1. Create *Django-CMS Cascade plugin* in `shop/cascade`
2. Create `View template` for the plugin in `shop/templates`
3. You can consider creating a rest API for reading/writing data in `shop/views`
4. Use the Django CMS UI to create a new page
5. Create the page layout and add the Plugin in the page

*If you want to make the migration for the created page (i.e., migrate your changes to other machines), do it via [Django-CMS Cascade Clipboard](https://djangocms-cascade.readthedocs.io/en/latest/clipboard.html)*:

6. Export the page configuration to CascadeClipboard (on Django CMS UI)
7. Dump the CascadeClipboard data to `workdir/fixtures/skeleton.json` via `dumpdata.sh` 
8. Update the `page_scaffold` in `shop/management/commands/shop.py` to add metadata for the page created above. The `reverse_id` is the `identifier` of the Clipboard you created in Step 6
9. Delete the database, and run the `initialize_shop_demo`
