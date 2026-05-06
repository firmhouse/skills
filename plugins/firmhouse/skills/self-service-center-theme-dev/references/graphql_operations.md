# GraphQL Operations for SSCv2 Templates

Endpoint:
- `POST /graphql`

Authentication header:
- `X-Project-Access-Token: <token>`

Token guidance:
- Use a write project token for `updateSelfServiceCenterTemplate`.
- Read-only token usage depends on access policy and should be treated as query-only.

## Query: list templates

```graphql
query SelfServiceCenterTemplates {
  selfServiceCenterTemplates {
    id
    templateFileName
    body
    createdAt
    updatedAt
  }
}
```

## Query: fetch one template

```graphql
query SelfServiceCenterTemplate($templateFileName: String!) {
  selfServiceCenterTemplate(templateFileName: $templateFileName) {
    id
    templateFileName
    body
    createdAt
    updatedAt
  }
}
```

Variables example:

```json
{
  "templateFileName": "dashboard.liquid"
}
```

## Mutation: update template

```graphql
mutation UpdateSelfServiceCenterTemplate($templateFileName: String!, $body: String!) {
  updateSelfServiceCenterTemplate(
    input: {
      templateFileName: $templateFileName,
      body: $body
    }
  ) {
    errors {
      attribute
      message
    }
    selfServiceCenterTemplate {
      id
      templateFileName
      updatedAt
    }
  }
}
```

Variables example:

```json
{
  "templateFileName": "dashboard.liquid",
  "body": "{% latest_orders %}\n{% product_listing %}"
}
```
