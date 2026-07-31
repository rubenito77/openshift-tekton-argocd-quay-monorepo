# OpenShift Tekton Argo CD Quay — Monorepo

Laboratorio de CI/CD sobre OpenShift.

## Arquitectura

- GitHub almacena código y configuración.
- Tekton ejecuta integración continua.
- Buildah construye la imagen.
- Red Hat Quay almacena las imágenes.
- Argo CD despliega el estado declarado en Git.
- OpenShift ejecuta la aplicación.

## Ambientes

| Ambiente | Namespace |
|---|---|
| CI/CD | `monorepo-cicd` |
| Desarrollo | `monorepo-dev` |

## Aplicación

Aplicación FastAPI de demostración.

Endpoints: `/`, `/health`, `/ready`, `/info`, `/docs`.
