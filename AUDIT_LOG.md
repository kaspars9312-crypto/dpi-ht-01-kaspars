# Локальный аудит DPI-HT-01

Дата: 2026-09-22. Объект: существующее приложение `site/dist`, главная `/` и `/review/`.

**Итог: технические проверки пройдены; финальная сдача заблокирована отсутствующими личными полями и открытыми вопросами кейса.** Приложение не пересоздавалось. Генератор запускался с `--check`: повторный расчёт в памяти и сравнение с существующими файлами, без перезаписи набора данных. Публикация не выполнялась; финальный `submission.json` отсутствует.

## Результаты проверок

| Проверка | Результат и периметр |
|---|---|
| Сборка | `python site/build.py --check` — PASS. Существующие данные, черновик, HTML, JS, CSS, схема и копии документов соответствуют входным файлам и генератору. |
| JavaScript | `node --check site/app.js` — PASS. В проверенной браузерной сессии нет сообщений console error/warn. |
| Маршруты | 20 HTTP-проверок пройдены. `/` и `/review/` возвращают 200; `/review` перенаправляет на `/review/`. Ассеты, данные, схема, черновик и восемь документов доступны. `/submission.json`, `/.git/config` и неизвестный маршрут возвращают 404. |
| Один набор данных | Обе страницы имеют одинаковую HTML-оболочку, используют один `app.js` и единственный вызов `fetch('/site-data.json')`. Запрос одного пути подтверждён журналом локального сервера при открытии обеих страниц. HTTP-содержимое совпадает с локальным каноническим файлом. |
| Реестр | В реестре, каноническом наборе и черновике ровно 100 уникальных D001–D100; 75 `operational` и 25 `material_judgment`. |
| Полнота ответов | Все 100 вопросов, текущих координационных ответов, категорий, confidence и ссылок на первичку заполнены. Все 25 итогов guided review присутствуют. Обязательные личные поля не заполнены: см. блокеры ниже. |
| Соответствие данных | Поля решений и исходные позиции A/B сохранены при переносе в канонический набор; поля решений черновика сопоставлены с реестром. Финансовые структуры черновика совпадают с каноническими. Исходный Markdown финансовых документов сохранён полностью. |
| Финансовые разделы | Присутствуют семь ведомостей, три предварительных отчёта, сверки R1–R7 и 30 unresolved. Неизвестные значения не подменены нулями. |
| Доказательства | Для 14 первичных файлов идентификаторы Drive соответствуют SOURCE_MANIFEST; SHA-256 совпадает с локальными копиями. У каждого решения есть соответствующие URL, имя файла, контрольная сумма и непустой локатор. |
| Ссылки документов | Проверены 118 уникальных ссылок сгенерированных документов: известные первичные URL, существующие локальные документы либо допустимые D-ID. Внешняя доступность Drive повторно не проверялась. |
| Личные сведения | `student.id` и `student.name` — null; личные обоснования и флаги изменения относительно AI не выдуманы. Подтверждение студента не объявлено полученным. Guided review явно отделён от независимой проверки источников. |

Машиночитаемый результат: [site/audit-results.json](site/audit-results.json). Повторяемая проверка: [site/audit.py](site/audit.py).

## Проверка интерфейса в браузере

| Действие | Главная | `/review/` |
|---|---|---|
| Без фильтра и поискового запроса | 100 из 100 | 25 из 25 |
| Фильтр Unresolved | 30 | 7 |
| Фильтр Low confidence | 30 | 7 |
| Фильтр различий A/B | 20 | 10 |
| Фильтр Material judgment | 25 | Страница уже ограничена 25 material judgments |
| Поиск D049 | Одна соответствующая запись | Одна соответствующая запись |
| Поиск D075 | — | Одна запись; разрыв запасов и неизвестный текущий эффект видны |

На главной проверены запрос без результатов, возврат к полному списку после очистки, раскрытие всех 100 найденных карточек и их сворачивание. На обеих страницах проверена смена фильтров. Количество записей проверялось по DOM, а не только по счётчику интерфейса.

Карточки показывают позиции A/B, текущий итог, guided review, доказательства и влияние на отчётность. Для D049 виден уточнённый смысл €5 000: чистая неоплаченная сумма операций текущего периода (€80 000 − €75 000), а не полный конечный payroll payable при неподтверждённом начальном остатке. Оригинальный исход guided review сохранён в истории данных.

На главной проверены все семь панелей сверок, 30 записей unresolved и раскрытие трёх финансовых отчётов. P&L, Balance Sheet и Cash Flow отображают таблицы и ссылки на доказательства. Просмотр узкого окна подтвердил читаемость карточек и финансовых таблиц. Это проверка отображения и соответствия зафиксированным данным, а не новое независимое финансовое заключение.

## Найденные и исправленные дефекты

1. Знак раскрытия карточки не менялся из-за ошибочного CSS-селектора. Исправлен селектор открытой карточки; поворот индикатора после раскрытия проверен в браузере.
2. Фильтр имел неоднозначную доступную подпись. Добавлено явное `aria-label="Показать"`; выбор по этому имени проверен на обеих страницах.
3. Браузер запрашивал отсутствующий favicon и получал 404. Добавлен локальный `favicon.svg`, ссылка в HTML и копирование ассета генератором. Проверка маршрута favicon — 200.

Исправлены исходные ассеты `site/app.js`, `site/styles.css`, `site/index.html` и их существующие копии в `site/dist`. В `site/build.py` добавлен режим проверки без перезаписи и включён favicon. В ходе этих исправлений реестр, `site-data.json` и `submission.draft.json` не менялись.

## Блокеры финальной сдачи

**50 ошибок предоставленной JSON-схемы:** у каждого из 25 material judgments отсутствуют личное `studentReasoning` (схема требует строку минимум 20 символов) и `changedFromAI` (требуется boolean). Сохранённые null намеренны: автоматически подставлять текст или false нельзя.

Перечень этих 25 решений: D041–D049, D056–D059, D064–D068, D071–D075, D091, D100.

**Ещё два содержательных блокера:** отсутствуют реальные `student.id` и `student.name`. Предоставленная схема требует наличие этих ключей, но сама не исключает null; поэтому они учтены отдельно от 50 ошибок схемы. Итого **52 блокера заполнения**. Они не являются 52 финансовыми unresolved.

В `site/schema_check.py` реализованы и проверены все ключевые слова, которые использует предоставленная схема; неизвестное ключевое слово останавливает проверку. Это специализированная проверка данной схемы, а не универсальный движок JSON Schema Draft 2020-12. Список точных путей ошибок находится в `site/schema-validation.json` и показан в разделе черновика сайта. Статус `canSubmit` остаётся false.

`studentReasoning` не выводится из согласия с guided review. `changedFromAI` не вычисляется вместо личного ответа студента. Guided review не подтверждает независимую проверку первичных источников. Личное подтверждение не сфабриковано.

## Сохранённые финансовые ограничения

Все **30 unresolved** сохранены; среди material judgments их семь: D046, D047, D048, D056, D071, D074, D075. Confidence этих открытых решений — low.

| Сверка | Статус в приложении | Видимая разница / ограничение |
|---|---|---|
| R1 Assets = Liabilities + Equity | NOT VERIFIABLE | Полная разница неизвестна; её нельзя объявить нулевой или ограничить €9 000. |
| R2 Cash-to-bank | PASS в банковском периметре | €0; конечный cash €60 000. Классификация owner payments €110 000 остаётся открытой, поэтому полный Cash Flow qualified. |
| R3 Revenue / AR | PARTIAL | Четыре договора сходятся с разницей €0; полный AR и признание web revenue не подтверждены. |
| R4 Inventory / COGS | FAIL | Count net €121 000 против movement net €112 000: **+€9 000**. Отдельно показан неподтверждённый AP bridge €45 000. |
| R5 PPE | PARTIAL | Cost register: €0; depreciation, AD и полный net PPE не подтверждены. |
| R6 Debt / Interest | PARTIAL | Principal: €0; арифметика interest expense минус cash соответствует €2 000, но полный interest roll-forward не подтверждён. |
| R7 Equity roll-forward | NOT VERIFIABLE | Opening equity, полный net profit, distributions и прочие движения неизвестны; разница неизвестна. |

P&L, Balance Sheet и Equity остаются preliminary / qualified. Балансирующие проводки не добавлялись. Незавершённые суммы не заполнялись нулями. Закрытие этих вопросов требует недостающих первичных доказательств, а не исправления интерфейса.

## Воспроизведение и контроль версии

Из каталога проекта, Python 3, без установки пакетов:

```powershell
python site/serve.py --port 8765
```

Локальные адреса: `http://127.0.0.1:8765/` и `http://127.0.0.1:8765/review/`. Сервер слушает только loopback и отдаёт `site/dist`.

В другом терминале:

```powershell
python site/build.py --check
python site/audit.py
node --check site/app.js
```

Автоматизированный аудит завершился с `PASS_WITH_DECLARED_SUBMISSION_BLOCKERS`: 10 групп проверок, 20 HTTP-проверок. JSON отчёта аудита — единственный результат, который перезаписывает `site/audit.py`.

- SHA-256 `site/dist/site-data.json`: `25006f7ae6eca01b2f31465d658a42fd537c8dc078738819e4ab5580e184c0e4`.
- SHA-256 `submission.draft.json`: `1190913519a830396700ddce7028c3de5894b065906a7501d7803589da97420b`.
- Корневой черновик и его копия в `site/dist` побайтно совпадают.

Созданы для аудита: `AUDIT_LOG.md`, `site/audit.py`, `site/audit-results.json`; добавлен локальный ассет `site/favicon.svg` и его копия. Финальный `submission.json` не создан, публикация не выполнялась.

## English display layer completion — 2026-09-22

- Both the home page (`/`) and `/review/` use `display-data-en.json` through the shared `app.js` display layer.
- The visible Cyrillic text count is **0**. Canonical `site-data.json` and source evidence records remain unchanged.
- Existing financial qualifications, all 30 unresolved issues, the `student.id` and `student.name` fields, and personal-reasoning blockers remain unchanged.
- No publication, GitHub push, or Vercel deployment was performed. The completed final `submission.json` is retained locally.

## Controlled report redesign — 2026-09-22

- Rebuilt the local report from the completed `submission.json`; schema validation completed with **0 errors**.
- Replaced the obsolete draft/submission-blocked messaging. The public report now identifies `submission.json` as the completed canonical package while retaining every financial qualification.
- Redesigned the home page as a concise audit report: reporting scope, qualified-result warning, four key metrics, executive conclusion, financial statements, seven reconciliation summaries, board recommendation, priority judgments, and a searchable 100-decision explorer.
- Redesigned `/review/` as **Guided Review Trail** containing exactly 25 material judgments with A/B positions, guided confirmation, disagreements, confidence, unresolved status, statement effect, and the required disclosure.
- Removed public direct Drive links, raw source documents, raw register/audit downloads, hashes, and schema downloads. Source IDs, filenames, document types, locators, and abbreviated checksum references remain in the compact audit appendix.
- Moved the answer template and submission rules to “Methodology and submission structure”; they are no longer presented as primary evidence.
- Performed an English-language display check: the generated public data and interface contain no Cyrillic or transliterated-Russian sentence display fields. No accounting conclusion was altered and no deployment was performed.

## Financial-detail completeness correction — 2026-09-22

- Restored seven collapsed Financial Schedules, three collapsed detailed preliminary statements, and seven collapsed reconciliation details on the home page.
- The public display carries only English presentation of amounts, stated results, scopes, and qualifications already present in the completed package; it introduces no assumptions, balancing entries, or new calculations.
- Privacy treatment remains unchanged: no external source links, raw source files, raw package/register/schema, hashes, or audit-file downloads are exposed.

## Teacher-feedback reporting and submission-endpoint correction — 2026-09-23

- Rebuilt the public display from the completed canonical `submission.json` without changing the decision register, guided-review population, student data, or unresolved matters.
- Added visible provisional tables: P&L provisional subtotal **€65,000 before unquantified insurance and other unresolved effects**; cash flow **€139,000 operating**, **€(80,000) investing**, **€31,000 financing before €(110,000) owner-related cash**, and **€(20,000)** net change to **€60,000** closing cash; balance-sheet scenario assets **€531,000**, listed liabilities **€406,000**, and illustrative residual equity **€125,000**. Candidate inputs and cash-equals-expense treatment are explicitly labelled assumptions, not final or audited amounts.
- Retained the €9,000 inventory conflict (movement €112,000 versus count €121,000) and the genuinely missing insurance amount; neither is treated as zero or resolved by a balancing entry.
- Replaced generic public operational summaries with specific English treatments and known monetary effects for every operational decision, including D001–D013.
- Copied canonical `submission.json` to `site/dist/submission.json` as the required public endpoint. Both root and distribution JSON files validate against the supplied schema with **0 errors** and are semantically identical.
- Local checks: `/` HTTP 200, `/review/` HTTP 200 and displays exactly 25 material judgments, `/submission.json` HTTP 200 with `application/json`; the generated English display has no Cyrillic text.

## Teacher-feedback selected-scenario correction — 2026-09-23

- Added a visible **Selected provisional case assumptions** section and three full, non-collapsible selected-scenario statements on the home page: Provisional Profit and Loss, Provisional Cash Flow, and Provisional Balance Sheet.
- The selected scenario uses only documented case inputs: €360,000 web-revenue candidate, €405,000 COGS candidate, €131,000 cash-equals-expense assumption for rent/marketing/software/utilities, €24,000 depreciation candidate, and an explicit €0 insurance-recognition assumption pending evidence. The €65,000 provisional net profit remains explicitly non-final.
- The selected balance-sheet scenario presents €531,000 selected assets, €406,000 listed liabilities, and €125,000 provisional equity, calculated as selected assets less listed liabilities. It is not a balancing conclusion.
- The €9,000 inventory conflict is visibly retained: selected movement inventory €112,000 versus €121,000 physical-count alternative. Missing insurance evidence remains disclosed as an unquantified alternative, not evidence of zero.
- The generated decision explorer retains 100 decisions (75 operational / 25 material judgments), with concrete English recorded determinations for every operational ID, including D001–D013. Guided-review disclosure, student details, A/B fields, confidence, evidence metadata, and unresolved statuses are retained.
- Rebuilt from source. Root `submission.json` and `site/dist/submission.json` each validate against the supplied schema with **0 errors**; the distribution copy is semantically identical. Local checks returned HTTP 200 for `/`, `/review/`, and `/submission.json`; `/review/` reports exactly 25 material judgments; rendered public display text contains no Cyrillic.

## Guided-reasoning restoration — 2026-09-23

- Replaced the identical generated `Guided confirmation of the recorded outcome` text in all **25** material-judgment `studentReasoning` fields with plain-English translations of the student's recorded spoken guided-review responses.
- The restored records preserve admissions of uncertainty and assistance. In particular, D057 states that the student requested the model entry and does not claim an independent allowance calculation; D056 preserves the initial cash-versus-expense misunderstanding and correction; D046/D047 and D071/D074/D075 retain low-confidence limits.
- `/review/` now displays a separate **Student's spoken reasoning (English translation)** section for every material judgment, alongside the outcome, A/B positions, statement effect and evidence metadata.
- The display explicitly says these are guided spoken responses, not an independent reread of source evidence or a no-AI review claim. No financial amount, decision status, evidence citation, confidence rating, or unresolved item was changed.
- Rebuild validation passed: 100 decisions, 25 material judgments, zero empty or generic reasoning fields, and byte-equivalent root/distribution `submission.json`. Local browser verification confirmed the new D041 reasoning is visible in `/review/`.
