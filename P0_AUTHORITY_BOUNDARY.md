# P0 Authority Boundary

For Ruflow AUT-05, `gabrielmateitoma/sss` is the only GitHub repository in the writer mutation boundary.

The Pi writer credential must be a GitHub fine-grained personal access token selected for this repository only, with the minimum repository permissions required for Git push and read-only work-item inspection. It must not include the canonical repository `gabrielmateitoma/system0-orchestration`.

Do not grant Workflows/Actions/administration/secrets permission. Do not grant autonomous merge authority.

Reviewer access is read-only; because this sandbox is public, GitHub repository read access does not require a reviewer GitHub write credential.
