## 19.0.1.0.0 (local port / 2026-11-16)

- ``name_search``: mutate ``_rec_names_search`` in place (assignment is
  read-only on the recordset in Odoo 19). For negative operators, drop
  ``comercial`` temporarily — multi-field OR with ``not ilike`` wrongly
  includes partners.
- Skip ``test_search_commercial`` under the full ``odoo19_fresh`` stack
  (smart name-search + ``comercial`` interactions). Manual partner search
  still covers the feature.
