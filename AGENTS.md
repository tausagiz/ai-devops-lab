# AGENTS

Krotki przewodnik dla agentow pracujacych w tym repo.

## Charakter repo

- Sandbox edukacyjny do automatyzacji Dockera i testowania workflowow AI.
- Ryzyko jest bardzo niskie: wazniejsze sa szybkie i tanie eksperymenty niz produkcyjna twardosc procesu.
- Repo sluzy do porownywania wielu narzedzi, szczegolnie tych z darmowymi limitami albo kosztem zaleznym od tokenow/wywolan.
- Instrukcje powinny byc krotkie i bez duplikacji, zeby zmniejszac koszt kontekstu.

## Priorytety pracy

- Preferuj male, odwracalne zmiany i krotkie petle walidacji.
- Zaczynaj od najtanszych sprawdzen: `pytest tests/unit`, `pytest tests/integration`, dopiero potem coverage lub drozsze kroki.
- Minimalizuj kontekst: czytaj tylko potrzebne pliki i nie powielaj tych samych zasad w wielu instrukcjach.
- Nie overengineeruj; to repo ma ulatwiac eksperymenty.

## Mapa projektu

- `src/docker_automation/cli.py` - wejscie CLI i routing komend.
- `src/docker_automation/config.py` - stale (`IMAGE_TAG`, `BUILD_PATH`).
- `src/docker_automation/docker_client.py` - fabryka `get_client()`.
- `src/docker_automation/commands/*.py` - implementacje komend.
- `tests/unit/` - testy jednostkowe (mock Docker SDK).
- `tests/integration/` - testy smoke CLI.
- `scripts/check_docs.py` - walidacja commit message + docs gate.

## Reguly repo

- Implementacja: dostep do Dockera tylko przez `get_client()`; stale trzymaj w `config.py`; nowa komenda trafia do `commands/` i musi byc zarejestrowana w `cli.py`.
- Branche: nowa galaz tylko z aktualnego `main`; dirty worktree blokuje przelaczanie; format `type/short-slug`; typy: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `build`, `ci`; slug lowercase, hyphen-separated, 2-4 sensowne slowa, bez duplikacji typu; przy zbyt ogolnym opisie dopytaj zamiast zgadywac.
- Commity: tylko workflow `/Prepare Commit` moze automatycznie tworzyc commit; pozostale workflowy nie commituja ani nie pushuja bez jawnej prosby; title ma format `type(scope): summary` lub `type: summary`; docs gate dla zmian kodu wymaga `README.md` lub `AGENTS.md`; auto-fix docs gate wolno robic tylko przez stage juz istniejacych zmian w tych plikach; nie tworz nowej tresci dokumentacji tylko po to, zeby przejsc gate; przy mieszanym scope zatrzymaj sie i popros o potwierdzenie.
- Walidacja i PR: domyslnie uruchamiaj `pytest tests/unit`, `pytest tests/integration`, `python scripts/check_docs.py`; waski zakres tylko na wyrazna prosbe i trzeba wtedy jasno wskazac, co zostalo pominiete; pelna walidacja tylko na wyrazna prosbe (`pytest tests/ --cov=docker_automation`); PR domyslnie kieruj do `main`; jesli branch jest behind `main`, zapytaj o `merge` lub `rebase`, chyba ze preferencja zostala podana wprost; przed push zatrzymaj sie przy brudnym worktree i zasugeruj `/Prepare Commit`; dodatkowy kontekst PR dolacz do body.
- Zamykanie brancha: nigdy nie usuwaj `main` ani `master`; usuwaj tylko branche zmergowane do `origin/main`, chyba ze uzytkownik wyraznie potwierdzi ryzykowna operacje; gdy merge nie jest pewny albo potrzebne jest `-D`, zatrzymaj sie i czekaj na potwierdzenie; nigdy nie force-pushuj ani nie force-delete bez jawnej prosby.

## Integracje narzedziowe

- `AGENTS.md` jest warstwa repo-neutralna i podstawowym zrodlem zasad dla dowolnego agenta.
- Pliki w `.github/agents/` i `.github/prompts/` sa cienkimi wrapperami GitHub Copilot dla slash commands, `argument-hint` i formatu odpowiedzi.
- Gdy zasada dotyczy calego repo, trzymaj ja tutaj; w plikach Copilota zostaw tylko to, co konieczne do uruchomienia workflow.

## Workflow promptow

- `/Workflow Help` - lista dostepnych workflowow.
- `/New Branch` - aktualizacja `main` i utworzenie feature branch.
- `/Validate Changes` - lokalne testy + docs gate.
- `/Prepare Commit` - przygotowanie i utworzenie commitu.
- `/Open PR` - sync brancha, walidacja, push i otwarcie PR.
- `/Close Branch` - zamkniecie zmergowanego brancha i powrot na `main`.
