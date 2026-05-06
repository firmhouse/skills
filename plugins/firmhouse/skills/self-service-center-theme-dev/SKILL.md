---
name: self-service-center-theme-dev
description: Develop and maintain Firmhouse Self Service Center templates through the SSC GraphQL API. Use when Codex needs to fetch, edit, bootstrap, or publish SSC template files for a merchant workspace.
---

# Self Service Center Theme Dev

## Overview

Use this skill to manage the Liquid templates that power the Firmhouse Self Service Center for a merchant project.
Use the SSCv2 component docs at `https://docs.firmhouse.com/self-service-center-v2/components/overview` as the main entry point for page-template and component-tag documentation.
Use Tailwind CSS v4 utility classes in template markup for styling updates.

## Prerequisites

- Work from the merchant workspace you are actively using.
- Inspect the current working directory before doing anything else.
- If the current working directory is empty or has no checked-out project files yet, stop and ask the user to initialize a git repository there before continuing.
- During that bootstrap guidance, tell the user to add `.env` to `.gitignore` and create a `.env.sample` file that documents the expected token configuration.
- Read the project access token from workspace `.env` using `FIRMHOUSE_API_TOKEN=<token>`.
- Read an optional endpoint override from workspace `.env` using `FIRMHOUSE_API_URL=<url>`.
- Default the GraphQL endpoint to `https://portal.firmhouse.com/graphql` when no override is provided.
- Treat the workspace `.env` as the only source of token and endpoint configuration; do not pass those values as script arguments.

## First Use

On the first use of this skill in a workspace, explain the setup before attempting any GraphQL calls.

Tell the user they need to:

1. Create or obtain a Firmhouse "Self Service Center Templates Token" for the specific project they want to edit.
2. Ensure the workspace `.gitignore` includes `.env` so secrets are not committed.
3. Add a workspace `.env.sample` file that documents the expected token variable, for example `FIRMHOUSE_API_TOKEN=<token>`.
4. Create a workspace `.env` file with `FIRMHOUSE_API_TOKEN`.
5. If the template files do not exist locally yet, retrieve all templates, write them to the workspace, and commit that baseline before making changes.

If the token configuration is missing, stop after explaining the setup and ask the user to add it before continuing.

## Required Workflow

Follow this sequence:

1. Inspect the current working directory first. If it is empty, follow the first-use guidance above and stop.
2. On first use in a workspace, explain the token and `.env` setup before making GraphQL calls.
3. Check the Liquid docs at `https://developer.firmhouse.com/liquid/available-tags` for relevant Liquid objects and properties.
4. Check the SSCv2 docs at `https://docs.firmhouse.com/self-service-center-v2/components/overview` before planning changes.
5. Resolve the target template file from [references/available_templates.md](references/available_templates.md).
6. Fetch the current merchant template with `scripts/get_ssc_template.py`.
7. When the workspace does not already contain the templates, fetch all templates and write them to the workspace before editing.
8. Propose a full updated Liquid body, not a partial snippet, unless the user explicitly asks for a partial.
9. Save the updated template body into the current workspace before publishing so the applied version is tracked locally.
10. Apply the update with `scripts/update_ssc_template.py`.
11. If GraphQL returns validation errors, fix the full body and retry.
12. Keep the helper scripts inside this plugin; do not copy them into the merchant repository unless the user explicitly asks for that.

## Commands

### Read all templates

```bash
python3 scripts/get_ssc_template.py
```

### Read all templates and write them into the workspace

```bash
python3 scripts/get_ssc_template.py \
  --write-to-dir "$PWD"
```

### Read one template

```bash
python3 scripts/get_ssc_template.py \
  --template dashboard.liquid
```

### Update one template from a local file

```bash
python3 scripts/update_ssc_template.py \
  --template dashboard.liquid \
  --body-file /absolute/path/to/dashboard.liquid
```

## References

- Supported templates: [references/available_templates.md](references/available_templates.md)
- GraphQL queries and mutation shape: [references/graphql_operations.md](references/graphql_operations.md)
- SSCv2 component docs overview: `https://docs.firmhouse.com/self-service-center-v2/components/overview`
- Liquid object docs: `https://developer.firmhouse.com/liquid/available-tags`

## Guardrails

- Only work with supported template file names from [references/available_templates.md](references/available_templates.md).
- Do not continue from an empty workspace; ask the user to initialize the repository first.
- On first use, explain the `.env`, `.env.sample`, and token setup before making API calls.
- Keep secrets in `.env`; never write tokens into committed files.
- Do not add CLI flags for token or endpoint overrides; scripts must read configuration from workspace `.env`.
- Do not copy helper scripts into the merchant repository unless the user explicitly asks for that.
- Prefer full template bodies for remote updates to avoid truncating existing Liquid.
- Use Tailwind CSS v4 classes for styling changes.
- Use the SSCv2 component docs and Liquid docs before guessing at available tags, objects, or properties.
