# Available SSCv2 Templates

Supported template file names:
1. `dashboard.liquid`
2. `catalog.liquid`
3. `other.liquid`
4. `subscription_profile.liquid`
5. `shared_head.liquid`

Notes:
- Only these file names can be updated via `updateSelfServiceCenterTemplate`.
- Template body is validated with strict Liquid parsing and the registered SSC tag set on save.
- CSS is regenerated after each template update.
