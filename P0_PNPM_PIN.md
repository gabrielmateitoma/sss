# P0 pnpm Invocation Pin

The isolated Pi writer runtime uses Corepack with `pnpm@11.17.0` cached under:

`/srv/ai/ruflow/pi-writer/home/.corepack`

Every Ruflow Pi writer invocation that uses pnpm during AUT-05 must execute with:

`COREPACK_HOME=/srv/ai/ruflow/pi-writer/home/.corepack`

This is part of the P0 environment identity. A pnpm resolved outside that isolated Corepack home is not accepted as AUT-05 evidence.
