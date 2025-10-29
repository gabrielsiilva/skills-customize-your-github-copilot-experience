# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes

## Conventional Commits

Usamos o padrão Conventional Commits para mensagens de commit. Formato básico:
tipo[escopo opcional]: descrição curta

Tipos comuns:
- feat: nova funcionalidade
- fix: correção de bug
- docs: documentação
- style: formatação/código sem impacto funcional
- refactor: refatoração sem mudança de comportamento
- perf: melhoria de performance
- test: adição/alteração de testes
- chore: tarefas de manutenção (build, ferramentas)
- ci: alterações em pipelines/CI
- revert: reverter um commit anterior

Regras e exemplos:
- Mensagem curta em inglês ou português, no imperativo e sem ponto final.
- Escopo opcional entre parênteses (ex.: feat(assignment): ...).
- Linhas adicionais: corpo para detalhes e rodapé para referências ou breaking changes.

Exemplos:
```text
feat(assignments): add download link for starter code
fix(api): handle empty assignments list
docs: update README with setup instructions
style: format CSS following project conventions
refactor: simplify assignment loading logic
perf(assignments): reduce DOM updates when rendering list
test: add unit tests for assignment parser
chore(deps): bump eslint to latest
ci: add GitHub Actions workflow for tests
revert: Revert "feat(assignments): add download link for starter code"
```

Breaking change:
- Indicar no rodapé com `BREAKING CHANGE: descrição` e, se aplicável, referenciar issues com `#numero`.

Uso de issues:
- Relacione a issue no rodapé ou na descrição curta: `fix: close #123` ou `feat: add X (#456)`.