# AGENTS

Krótki przewodnik dla agentów pracujących w tym repo.

## Cel repo

- Nauka DevOps: automatyzacja lifecycle Dockera w Pythonie.
- Priorytet: build/run/log/cleanup, bez niepotrzebnych zmian logiki biznesowej.

## Mapa projektu

- `src/docker_automation/cli.py` - wejście CLI i routing komend.
- `src/docker_automation/config.py` - stałe (`IMAGE_TAG`, `BUILD_PATH`).
- `src/docker_automation/docker_client.py` - fabryka `get_client()`.
- `src/docker_automation/commands/*.py` - implementacje komend.
- `tests/unit/` - testy jednostkowe (mock Docker SDK).
- `tests/integration/` - testy smoke CLI.
- `scripts/check_docs.py` - walidacja commit message + docs gate.

## Zasady implementacyjne

1. Dostęp do Dockera tylko przez `get_client()`.
2. Stałe trzymać w `config.py`, nie rozrzucać po funkcjach.
3. Nową komendę dodaj w `commands/` i zarejestruj w `cli.py`.

## Zasady git i commit

- Tylko prompt `/Prepare Commit` może automatycznie tworzyć commit.
- Pozostałe agenty nie commitują i nie pushują bez jawnej prośby użytkownika.
- Docs gate: gdy commit zawiera zmiany kodu, w changed set musi być `README.md` lub `AGENTS.md`.
- Gdy docs gate nie przechodzi i `README.md`/`AGENTS.md` mają już lokalne unstaged zmiany, można je automatycznie dodać do stage (bez tworzenia nowej treści).

## Walidacja PR

- Zakres PR jest walidowany skryptem `python scripts/check_docs.py`.
- Format commit title: `type(scope): summary` lub `type: summary`.
- Dozwolone typy: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `build`, `ci`.
- Testy CI: `pytest tests/unit` i `pytest tests/integration`.

## Workflow promptów

- `/Workflow Help` - lista dostępnych workflowów.
- `/New Branch` - aktualizacja `main` i utworzenie feature branch.
- `/Validate Changes` - lokalne testy + docs gate.
- `/Prepare Commit` - przygotowanie i utworzenie commitu.
- `/Open PR` - sync brancha, walidacja, push i otwarcie PR.
- `/Close Branch` - zamknięcie zmergowanego brancha i powrót na `main`.
