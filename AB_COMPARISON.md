# DPI-HT-01 — только сопоставление результатов A/B

Основание: последнее поручение пользователя использовать ровно десять локальных файлов A/B для сопоставления. Все десять доступны и прочитаны. Полная веха 4 не завершена: окончательные решения, разрешение споров по первичке и студенческая сертификация не выполнялись.

## Главный результат

Противоположных итоговых учётных позиций по 100 парам ответов не выявлено: основные рабочие суммы, классификации и признание пробелов совместимы. Это не означает, что 100 вопросов окончательно решены. У обеих сторон остаются неподтверждённые суммы и разрыв запасов 9 000 EUR.

Уверенность различается в **16 из 100** решений. Числовые/null-поля `statementEffect` различаются в **6 из 25** существенных суждений; это различия базы или предмета эффекта, разобранные ниже. Набор процитированных файлов различается у **22** решений; исходные ссылки обеих сторон сохранены в приложении и JSON.

Новые финансовые значения не определялись: ниже сопоставлены уже имеющиеся суммы и расчёты A/B. Их совпадение не повышает автоматически надёжность общей исходной информации. `student.id`, `student.name`, `studentReasoning`, финальные ответы и `changedFromAI` не заполнялись. Исходные файлы A/B не изменены.

## 1. Входные комплекты и границы проверки

| Аналитик | Прочитанный файл | Байты |
|---|---|---:|
| A | [analysis-agent-a.md](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/DPI-HT-01-A/analysis-agent-a.md>) | 40871 |
| A | [evidence-coverage-a.md](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/DPI-HT-01-A/evidence-coverage-a.md>) | 25239 |
| A | [decision-draft-a.json](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/DPI-HT-01-A/decision-draft-a.json>) | 202208 |
| A | [schedules-a.md](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/DPI-HT-01-A/schedules-a.md>) | 29690 |
| A | [reconciliation-a.md](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/DPI-HT-01-A/reconciliation-a.md>) | 23519 |
| B | [analysis-agent-b.md](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/DPI-HT-01-B/analysis-agent-b.md>) | 19249 |
| B | [evidence-coverage-b.md](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/DPI-HT-01-B/evidence-coverage-b.md>) | 12646 |
| B | [decision-draft-b.json](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/DPI-HT-01-B/decision-draft-b.json>) | 130713 |
| B | [schedules-b.md](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/DPI-HT-01-B/schedules-b.md>) | 28999 |
| B | [reconciliation-b.md](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/DPI-HT-01-B/reconciliation-b.md>) | 13134 |

Полные SHA-256 всех десяти переданных файлов сохранены в `AB_COMPARISON.json` → `inputs`. A — зафиксированная версия A-1.2; B — `independent_analysis_complete_with_unresolved_evidence_gaps`. Заявленный A хеш канонического массива решений пересчитан по записанной им схеме и совпал. У B сопоставимого внутреннего контрольного хеша заморозки нет; текущий полный файл идентифицирован SHA-256 для этого сравнения.

Оба автора прямо заявляют, что не читали другую сторону, и сообщают о завершении самостоятельного анализа. Это свидетельства в предоставленных отчётах. История отдельных чатов и техническая невозможность перекрёстного доступа по десяти файлам независимо не подтверждаются; повторные чаты и запросы аналитикам не запускались.

**Покрытие:** A и B описывают чтение и анализ 12/12 CASE FILES и 2/2 CODEX FILES, с локаторами и ограничениями. В журналах совпадают хеши всех 14 обязательных файлов и START HERE — 15 общих источников, расхождений нет. У B дополнительно есть raw-хеш Finance Reference; A читал справочник как возвращённый текст без raw/постраничной визуальной проверки. A прочитал текст 16 страниц восьми обязательных PDF и отдельно просмотрел три страницы с изображениями. B заявляет текстовый и визуальный просмотр всех 18 страниц девяти PDF, включая справочник. Это разная глубина визуальной проверки, а не заявленный пропуск обязательного файла. В текущем сопоставлении первичка заново не открывалась.

## 2. Структура 100 решений

| Проверка | A | B | Сопоставление |
|---|---:|---:|---|
| Число решений / уникальных ID | 100 / 100 | 100 / 100 | Точный набор D001–D100 |
| operational / material_judgment | 75 / 25 | 75 / 25 | Совпадает, в том числе список 25 ID |
| question, category, reviewTier | Сохранены | Сохранены | Между A/B нет различий во всех 100 парах |
| confidence: high / medium / low | 63 / 25 / 12 | 53 / 29 / 18 | B ниже в 16 решениях, выше — ни в одном |
| answer / evidence / confidence | Непустые | Непустые | Не доказывает разрешение неизвестных сумм |

Оригинальный Answer Template сейчас не перечитывался: соответствие ему заявлено обоими авторами, а текущая машинная проверка подтверждает совпадение метаданных A/B и ожидаемый набор ID/tiers из спецификации. Проверка финальной Submission Rules не заявляется.

У A `aiProposal` содержит первоначальную позицию, а `independentChallenge` ожидает B. У B собственная позиция хранится в `agentBPosition`/`agentBReasoning`, `independentChallenge` означает самостоятельное исследование, а `aiProposal` — null. Это различия ролей, не отсутствие независимого B. Устаревшее ожидание B в замороженном A сохранено как история; поле A не перезаписано. Студенческие поля у обоих остаются незаполненными.

## 3. Совпадающие числовые результаты и их ограничения

Источники этого раздела: `schedules-a.md`, `schedules-b.md`, оба анализа и оба JSON (ссылки в разделе 1). Все значения — EUR и позиции авторов, а не вновь утверждённая отчётность.

| Показатель | A | B | Общий предел вывода |
|---|---:|---:|---|
| Выручка | 960 000 | 960 000 | Предварительно; web 360 000 по CRM, нет полного первичного реестра |
| Поступления покупателей | 899 000 | 899 000 | 774 000 текущие продажи + 35 000 старая AR + 90 000 авансы |
| Конечные деньги | 60 000 | 60 000 | Банковский периметр пакета; не проверка всех возможных счетов |
| CFO / CFI / CFF | 139 000 / −80 000 / −79 000 | 139 000 / −80 000 / −79 000 | Оба относят оплаченные проценты в CFO |
| AR gross / net текущих продаж | 186 000 / 168 000 | 186 000 / 168 000 | Полная старая AR неизвестна |
| Запасы по count / по движению | 121 000 / 112 000 | 121 000 / 112 000 | Разница 9 000 не разрешена |
| Потребление / списание запасов | 405 000 / 22 000 | 405 000 / 22 000 | 396 000 consumption — альтернативный сценарий, не исправление |
| Закупки / оплаты поставщикам / closing AP | 459 000 / 378 000 / 126 000 | 459 000 / 378 000 / 126 000 | Opening AP 45 000 выведен условно |
| Payroll expense / paid / payable | 248 000 / 231 000 / 32 000 | 248 000 / 231 000 / 32 000 | Помесячных сумм нет |
| PPE cost / AD / net | 260 000 / 69 000 / 191 000 | 260 000 / 69 000 / 191 000 | Амортизация периода 24 000 не воспроизведена из регистра |
| Principal / interest expense / paid / payable | 131 000 / 12 000 / 10 000 / 2 000 | 131 000 / 12 000 / 10 000 / 2 000 | График, ставка и maturity split отсутствуют |
| Авансы клиентов / выплаты владельцу | 90 000 / 110 000 | 90 000 / 110 000 | Авансы — обязательства; distributions — предварительная классификация |
| R-17 / legal provision | 18 000 / 25 000 | 18 000 / 25 000 | Legal 20 000–30 000; нет двойного списания R-17 |
| Прибыль по известным строкам | 65 000 | 65 000 | Не окончательная net profit: insurance и другие вопросы неизвестны |
| Подытоги активов / обязательств | 540 000 / 406 000 | 540 000 / 406 000 | Неполные и предварительные; 134 000 разницы не подтверждённый капитал |
| Условный opening / closing equity | 170 000 / 125 000 | 170 000 / 125 000 | Диагностическая модель, не независимые остатки |

**Различие представления Opex:** A показывает 376 000 вместе с амортизацией 24 000. B показывает 352 000 без амортизации и затем отдельную строку 24 000. Это одна и та же сумма включённых расходов, не финансовое расхождение. Оба получают operating result 77 000 и known-line result 65 000. A выводит equity 125 000 преимущественно в диагностической сверке; B включает его в явно условную модель баланса. Ни один не утверждает полный капитал.

## 4. Шестнадцать различий confidence

| ID | A | B | Причина различия в контексте ответов |
|---|---|---|---|
| D003 | high | medium | Обе стороны признают Phoenix 100 000 и AR 30 000. B отдельно отмечает варианты имени и отсутствие оригинала email-приёмки; A оценивает достаточность описанного исполнения выше. |
| D005 | high | medium | A оценивает подтверждённое поступление 35 000 и его классификацию; B дополнительно учитывает неизвестный полный opening AR. Полнота начальной AR не подтверждена обеими сторонами. |
| D048 | medium | low | Оба оставляют inventory/COGS gap 9 000 открытым. A: medium для предварительной рабочей величины; B: low из-за неразрешённого противоречия. |
| D049 | high | medium | Суммы и функции payroll совпадают. A ставит high по классификации/арифметике; B — medium по внутренней ведомости и её ограничениям. Это различная оценка надёжности, не иной расчёт. |
| D050 | high | medium | Суммы и функции payroll совпадают. A ставит high по классификации/арифметике; B — medium по внутренней ведомости и её ограничениям. Это различная оценка надёжности, не иной расчёт. |
| D051 | high | medium | Суммы и функции payroll совпадают. A ставит high по классификации/арифметике; B — medium по внутренней ведомости и её ограничениям. Это различная оценка надёжности, не иной расчёт. |
| D056 | medium | low | Оба используют предварительные 24 000 без исходного depreciation schedule. A: medium; B: low. Никакая сторона не воспроизвела оценку по срокам/стоимостям. |
| D062 | high | medium | Суммы и функции payroll совпадают. A ставит high по классификации/арифметике; B — medium по внутренней ведомости и её ограничениям. Это различная оценка надёжности, не иной расчёт. |
| D066 | high | medium | Обе стороны признают Phoenix 100 000 и AR 30 000. B отдельно отмечает варианты имени и отсутствие оригинала email-приёмки; A оценивает достаточность описанного исполнения выше. |
| D074 | medium | low | Оба используют предварительные 24 000 без исходного depreciation schedule. A: medium; B: low. Никакая сторона не воспроизвела оценку по срокам/стоимостям. |
| D075 | medium | low | Оба оставляют inventory/COGS gap 9 000 открытым. A: medium для предварительной рабочей величины; B: low из-за неразрешённого противоречия. |
| D080 | high | medium | Суммы и функции payroll совпадают. A ставит high по классификации/арифметике; B — medium по внутренней ведомости и её ограничениям. Это различная оценка надёжности, не иной расчёт. |
| D083 | medium | low | Оба используют предварительные 24 000 без исходного depreciation schedule. A: medium; B: low. Никакая сторона не воспроизвела оценку по срокам/стоимостям. |
| D084 | high | medium | A оценивает подтверждённый closing AP 126 000; B снижает уверенность из-за условного opening AP 45 000 и roll-forward. Closing-сумма не различается. |
| D086 | medium | low | Оба оставляют inventory/COGS gap 9 000 открытым. A: medium для предварительной рабочей величины; B: low из-за неразрешённого противоречия. |
| D087 | high | medium | Суммы и функции payroll совпадают. A ставит high по классификации/арифметике; B — medium по внутренней ведомости и её ограничениям. Это различная оценка надёжности, не иной расчёт. |

Причины выше — сопоставление формулировок и методики авторов, а не новое присвоение confidence. Особенно D005 и D084 смешивают уверенность в конкретной подтверждённой сумме с полнотой соответствующей ведомости. Конечный уровень уверенности здесь не выбирается.

## 5. Шесть различий statementEffect

Порядок полей в векторах: **profit, cash, assets, liabilities, equity**. null не равен нулю. Все исходные базы приведены также в приложении по каждому существенному решению.

| ID | Эффект A | Эффект B | Значение различия |
|---|---|---|---|
| D064 | 180 000 / 0 / 180 000 / 0 / 180 000 | 180 000 / 180 000 / 180 000 / 0 / 180 000 | A: отдельное признание выручки до инкассации, cash=0. B: признание плюс уже состоявшийся сбор денег. Итоговые revenue, AR и CF совпадают; поля cash имеют разные базы и не сравниваются как две оценки одного денежного потока. |
| D065 | 200 000 / 0 / 200 000 / 0 / 200 000 | 200 000 / 142 000 / 200 000 / 0 / 200 000 | A: отдельное признание выручки до инкассации, cash=0. B: признание плюс уже состоявшийся сбор денег. Итоговые revenue, AR и CF совпадают; поля cash имеют разные базы и не сравниваются как две оценки одного денежного потока. |
| D066 | 100 000 / 0 / 100 000 / 0 / 100 000 | 100 000 / 70 000 / 100 000 / 0 / 100 000 | A: отдельное признание выручки до инкассации, cash=0. B: признание плюс уже состоявшийся сбор денег. Итоговые revenue, AR и CF совпадают; поля cash имеют разные базы и не сравниваются как две оценки одного денежного потока. |
| D067 | 120 000 / 0 / 120 000 / 0 / 120 000 | 120 000 / 95 000 / 120 000 / 0 / 120 000 | A: отдельное признание выручки до инкассации, cash=0. B: признание плюс уже состоявшийся сбор денег. Итоговые revenue, AR и CF совпадают; поля cash имеют разные базы и не сравниваются как две оценки одного денежного потока. |
| D075 | null / 0 / null / null / null | -22 000 / 0 / -22 000 / 0 / -22 000 | A показывает неизвестный полный эффект разрешения gap 9 000 (null, cash=0). B показывает только известное списание 22 000 от gross count до net count. Оба сохраняют 121 000 против 112 000. Это разные предметы эффекта; null не заменять на −22 000, а списание не учитывать повторно с D058/D072. |
| D091 | null / null / null / null / null | 0 / 0 / 0 / 0 / 0 | A оставляет совокупный эффект завершения исправлений неизвестным (null). B показывает нулевой непосредственный эффект самой рекомендации. Итоговая позиция одинакова: пока не утверждать счета как окончательные. Ноль и null нельзя механически взаимозаменять. |

У остальных 19 существенных суждений числовые/null-векторы совпадают. Суммировать эффекты разных решений нельзя: есть повторяющиеся события и разные локальные базы. Единую базу для будущей итоговой структуры ещё предстоит определить; текущие значения и исходники не менялись.

## 6. Сопоставление семи сверок

| Сверка | A | B | Вывод сравнения |
|---|---|---|---|
| Balance Sheet | NOT VERIFIED; условная разница 9 000 | FAIL ограниченной модели на 9 000; полная BS не подтверждена | Разные названия статуса для совместимого результата |
| Cash / bank / CF | PASS, closing 60 000 | PASS, closing 60 000 | Совпадает в банковском периметре |
| Revenue / AR | Текущая когорта PASS arithmetic; полный AR UNRESOLVED | CONDITIONAL по opening/полноте | Разная гранулярность статуса; 168 000 только текущие продажи |
| Inventory / COGS | FAIL +9 000 | FAIL +9 000 | Совпадают сумма и неразрешённость |
| PPE / AD | Cost arithmetic PASS; AD CONDITIONAL | CONDITIONAL | Оба не подтверждают расчёт 24 000 |
| Debt / interest | PASS closing; opening interest 0 implied | PASS по переданным суммам; opening 0 implied | Одинаковая оговорка, нет нового расчёта по ставке |
| Equity roll-forward | UNRESOLVED | NOT VERIFIED | Независимого opening нет; условные 170 000 → 125 000 |

Оба показывают косвенный CFO 130 000 при count-запасах против прямого 139 000. Разница 9 000 связана с тем же конфликтом модели запасов и не должна автоматически считаться вторым отдельным убытком. Оба показывают альтернативы 112 000 inventory либо 396 000 consumption как сценарии, не выбранные факты.

## 7. Карта открытых вопросов A/B

Коды U принадлежат разным пространствам имён: A-U01 закрыт как получение спецификации; B-U01 — открытый складской вопрос. Нельзя объединять записи только по номеру.

| Тема | У A | У B | Сопоставление |
|---|---|---|---|
| Stock gap 9 000 | U02 | U01 | Одинаковый открытый вопрос |
| Полный opening balance/equity | U03 | U03 | Одинаковый пробел; условные остатки не подтверждены |
| Insurance | U04 | U02 | Суммы и проводка неизвестны |
| Помесячный payroll | U05 | U08 | D014–D021 не разрешены |
| Depreciation register | U06 | U06 | Одинаковый пробел, разные confidence |
| Event Things opening AP | U07 | U05 | 45 000 — выведенный остаток |
| Полная AR / web sales | U08 | U04 и U07 | B разделяет тему на старую AR и web-доказательства |
| Утилизация 2 000 | U09 | U10 | Оба не начисляют обязательство по одной котировке |
| Owner recovery | U10 | U11 | B дополнительно фиксирует конфликт даты на фото |
| Loan terms / maturity | U11 | U13 | Совпадает по отсутствию документов |
| Opex accruals/prepayments | U12 | U12 | Оплата не подтверждает периодизацию |
| Earn-out | U13 | U15 | Оба отклоняют 312 000 и не подставляют 65 000 автоматически |
| Экономика сегментов / исполнение авансов | U14 | Нет отдельного U; analysis и D099 | Содержательно учтено обеими сторонами |
| Legal range 20 000–30 000 | D059/D073, schedules, не отдельный U | U09 | У B отдельная запись; оценку раскрывают оба |
| Phoenix acceptance / имена | D003/D066, без отдельного U | U14 | B выделяет риск и снижает confidence |
| Полнота банковского и учётного периметра | Оговорки analysis/reconciliation, без отдельного U | U16 | B выделяет риск отдельной записью |

13 открытых U у A и 16 у B нельзя трактовать как три новых финансовых ошибки: гранулярность и перечень выделенных тем различаются. Общие low-confidence ответы — D014, D015, D016, D017, D018, D019, D020, D021, D034, D060, D078, D089. Прочие ограничения не исчерпываются этой выборкой.

## 8. Дополнительные различия доказательств и представления

- **Изображение виллы:** B сообщает о датах 12 и 26 августа 2024 на брони при платеже 2026. A описывает просмотр фото, но мелкие декоративные надписи не использует как учётные записи. В текущем сопоставлении фото не открывалось; наблюдение B сохранено как вопрос, не подтверждено и не опровергнуто. Оба оставляют 70 000 в периоде банковской записи и предварительно относят к distributions. В B D047 замечание о вилле перенесено и на owner-card; применимость к отдельным 40 000 требует разграничения.

- **Различие ссылок:** различные наборы файлов у 22 решений не означают 22 споров. Часто одна сторона добавляет банк, CRM или позднее подтверждение, а другая опирается на меньший набор. Полные строки evidence сохранены без замены; источники не проверялись заново в Drive.

- **Самоссылки B:** в базах D071, D073 и D074 есть ссылки на собственный ID вместо ясного указания пары D057/D071, D059/D073 и D056/D074. Это недостаток пояснений о повторном эффекте, не обнаруженное двойное начисление: ведомости включают соответствующую сумму по одному разу. В текущем сравнении текст не исправлялся.

- **Финальный формат:** `amountEUR`, `economicEventId`, `unresolvedDependencies` и freeze-метаданные есть у A; B использует собственные `agentBPosition`, `agentBReasoning`, `uncertainty`. Отсутствие у B поля amountEUR не означает отсутствия суммы: она содержится в answer. Совпадение ответов AI не является личным решением студента.

## 9. Граница выполненной работы

Выполнены чтение десяти заданных файлов, структурное сопоставление 100 решений, смысловая проверка позиций, сравнение уверенности, эффектов, ведомостей, сверок и журналов покрытия. Результат: этот отчёт и машиночитаемое приложение `AB_COMPARISON.json` с исходными объектами A/B, точными evidence, пометками различий и хешами входов.

Не выполнены: выбор окончательных ответов или confidence, разрешение пробелов по новым источникам, пересчёт итоговой отчётности, сертификация студентом, создание submission.json/сайта/репозитория, публикация и отправка результатов вовне. Документы вехи 1 оставлены как исторический снимок; данный отчёт фиксирует только текущее сопоставление. Работа останавливается здесь.

## Приложение: все 100 пар решений

Ниже дословно сохранены answer и confidence обеих сторон; для 25 суждений — их собственные обоснования и базы эффектов. Локальные ссылки ведут в переданные JSON; полные evidence сохранены и в машиночитаемом приложении. Отметка «совместимы» означает только отсутствие противоположной позиции в прочитанных текстах, а не признание ответа правильным или окончательным.

### D001 — Resolve the source and treatment of NorthStar receipt.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** NorthStar / N STAR / North Star: поступление 180,000 EUR относится к исполненному договору в CRM, строка 4. Выручка 180,000 EUR; текущая дебиторская задолженность 0 EUR. Это одна операция с вариантами названия, а не дополнительные продажи.

**B (high):** Поступление 180 000 EUR от N STAR EVENTS сопоставлено с NorthStar, INV-26012; погашение дебиторской задолженности за принятые 12 февраля коробки. Остаток 0.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 4, RCPT-NS — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!A4:I4 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit
- 04 Contracts Returns and Angry Customers.pdf — стр. 1, INV-26012 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 4 (заголовок = строка 1), Reference=RCPT-NS
- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 1, INV-26012
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!A4:I4

### D002 — Resolve the source and treatment of Freedom receipt 1.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Freedom Festivals: поступление 142,000 EUR относится к исполненному договору в CRM, строка 5. Выручка 200,000 EUR; текущая дебиторская задолженность 58,000 EUR. Это одна операция с вариантами названия, а не дополнительные продажи.

**B (high):** Поступление 142 000 EUR по INV-26031; выручка 200 000, остаток AR 58 000. Обозначение 1/2 не доказывает существование второго платежа.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 6, RCPT-FF — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!A5:I5 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit
- 04 Contracts Returns and Angry Customers.pdf — стр. 1, INV-26031 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 6 (заголовок = строка 1), Reference=RCPT-FF
- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 1, INV-26031
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!A5:I5

### D003 — Resolve the source and treatment of Phoenix receipt.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Phoenix People / Phoenix HR: поступление 70,000 EUR относится к исполненному договору в CRM, строка 6. Выручка 100,000 EUR; текущая дебиторская задолженность 30,000 EUR. Это одна операция с вариантами названия, а не дополнительные продажи.

**B (medium):** 70 000 EUR PHOENIX PEOPLE TEAM сопоставлены с Phoenix HR/People, INV-26047; услуга завершена 29 апреля, выручка 100 000, AR 30 000.

**Отличия/оговорки сравнения:** Обе стороны признают Phoenix 100 000 и AR 30 000. B отдельно отмечает варианты имени и отсутствие оригинала email-приёмки; A оценивает достаточность описанного исполнения выше.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 7, RCPT-PHX — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!A6:I6 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit
- 04 Contracts Returns and Angry Customers.pdf — стр. 1, INV-26047 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 7 (заголовок = строка 1), Reference=RCPT-PHX
- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 1, INV-26047
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!A6:I6

### D004 — Resolve the source and treatment of Liberty receipt.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Liberty Hotels: поступление 95,000 EUR относится к исполненному договору в CRM, строка 7. Выручка 120,000 EUR; текущая дебиторская задолженность 25,000 EUR. Это одна операция с вариантами названия, а не дополнительные продажи.

**B (high):** 95 000 EUR погашают INV-26063 Liberty; поставка 120 000 признана 20 июня, AR 25 000.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 8, RCPT-LIB — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!A7:I7 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit
- 04 Contracts Returns and Angry Customers.pdf — стр. 1, INV-26063 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 8 (заголовок = строка 1), Reference=RCPT-LIB
- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 1, INV-26063
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!A7:I7

### D005 — Resolve the source and treatment of Opening receivable receipt.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** 35 000 EUR — погашение старой дебиторской задолженности, операционное поступление, без повторного признания выручки периода. Полный начальный остаток AR этим платежом не установлен.

**B (medium):** 35 000 EUR — сбор начальной AR, не новая выручка. Полный начальный остаток AR не представлен; равенство opening AR=35 000 является лишь рабочим допущением.

**Отличия/оговорки сравнения:** A оценивает подтверждённое поступление 35 000 и его классификацию; B дополнительно учитывает неизвестный полный opening AR. Полнота начальной AR не подтверждена обеими сторонами.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 3, RCPT-001 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 3 (заголовок = строка 1), Reference=RCPT-001

### D006 — Resolve the source and treatment of Finally Single web receipts.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** 250 000 EUR — поступления Finally Single web; выручка по CRM 270 000, дебиторская задолженность платформы 20 000. Банк подтверждает деньги; полные платформенные реестры/акты доставки отсутствуют.

**B (medium):** Платформа перечислила 250 000 EUR по Finally Single; CRM показывает выручку 270 000 и платформенную AR 20 000. Дополнительно к выручке поступление не признавать.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 9, PLAT-FSB — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!A8:I8 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 9 (заголовок = строка 1), Reference=PLAT-FSB
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!A8:I8

### D007 — Resolve the source and treatment of Never Call Back web receipts.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** 37 000 EUR — поступления Never Call Back web; выручка по CRM 90 000, валовой остаток 53 000. R-17 на 18 000 входит в этот остаток; после резерва остаток 35 000. Повторно не уменьшать выручку.

**B (medium):** Платформа перечислила 37 000 EUR по Never Call Back; CRM-выручка 90 000, AR gross 53 000. R-17 18 000 включён в эту группу: net AR 35 000 после полного обесценения.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 10, PLAT-NCB — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!A9:I9 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit
- 04 Contracts Returns and Angry Customers.pdf — стр. 2, R-17 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 10 (заголовок = строка 1), Reference=PLAT-NCB
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!A9:I9
- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 2, R-17
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, liquidator notice

### D008 — Resolve the source and treatment of New Beginnings deposit.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** 60,000 EUR — аванс за сентябрьское мероприятие; операционное поступление и договорное обязательство. Выручка на 31 августа: 0.

**B (high):** 60 000 EUR NB-SEP — аванс за мероприятие 15 сентября: операционный приток и обязательство по договору, выручка до 31 августа 0.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 11, DEP-NB — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!A10:I10 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit
- 04 Contracts Returns and Angry Customers.pdf — стр. 2, NB-SEP — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 11 (заголовок = строка 1), Reference=DEP-NB
- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 2, NB-SEP

### D009 — Resolve the source and treatment of Fresh Freedom deposit.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** 30,000 EUR — аванс за сентябрьское мероприятие; операционное поступление и договорное обязательство. Выручка на 31 августа: 0.

**B (high):** 30 000 EUR FF-SEP — аванс за мероприятие 24 сентября: операционный приток и обязательство по договору, выручка до 31 августа 0.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 12, DEP-FF2 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!A11:I11 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit
- 04 Contracts Returns and Angry Customers.pdf — стр. 2, FF-SEP — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 12 (заголовок = строка 1), Reference=DEP-FF2
- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 2, FF-SEP

### D010 — Resolve the source and treatment of Box supplier payment.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** BoxWorks: операционная выплата 105,000 EUR; закупки 130,000, подтверждённый остаток поставщика 25,000. Выплата не равна расходу периода. При отсутствии иных движений подразумевается начальный остаток 0; это вывод, а не отдельное подтверждение.

**B (high):** Оплата BoxWorks 105 000 EUR; покупки 130 000, подтверждённый AP 25 000. Платёж уменьшает AP, не определяет COGS.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 13, SUP-BOX — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 06 Purchases Invoices and Goods Received.pdf — стр. 1, таблица Supplier / document, строка BoxWorks batch — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 13 (заголовок = строка 1), Reference=SUP-BOX
- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 1, BoxWorks batch

### D011 — Resolve the source and treatment of Glass supplier payment.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Glass & Drama: операционная выплата 92,000 EUR; закупки 120,000, подтверждённый остаток поставщика 28,000. Выплата не равна расходу периода. При отсутствии иных движений подразумевается начальный остаток 0; это вывод, а не отдельное подтверждение.

**B (high):** Оплата Glass & Drama 92 000 EUR; покупки 120 000, подтверждённый AP 28 000.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 14, SUP-GLS — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 06 Purchases Invoices and Goods Received.pdf — стр. 1, таблица Supplier / document, строка Glass & Drama Ltd. — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 14 (заголовок = строка 1), Reference=SUP-GLS
- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 1, Glass & Drama

### D012 — Resolve the source and treatment of Print supplier payment.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Print Again: операционная выплата 81,000 EUR; закупки 95,000, подтверждённый остаток поставщика 14,000. Выплата не равна расходу периода. При отсутствии иных движений подразумевается начальный остаток 0; это вывод, а не отдельное подтверждение.

**B (high):** Оплата Print Again 81 000 EUR; покупки 95 000, подтверждённый AP 14 000.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 15, SUP-PRT — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 06 Purchases Invoices and Goods Received.pdf — стр. 1, таблица Supplier / document, строка Print Again SIA — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 15 (заголовок = строка 1), Reference=SUP-PRT
- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 1, Print Again

### D013 — Resolve the source and treatment of Event supplier payment.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Event Things: операционная выплата 100,000 EUR; закупки 114,000, подтверждённый остаток поставщика 59,000. Выплата не равна расходу периода. При отсутствии иных движений подразумевается начальная кредиторская задолженность 45 000 EUR; отдельного подтверждения начального остатка нет.

**B (medium):** Банк подтверждает Event Things: оплата 100 000 EUR. Покупки 114 000 и подтверждённый остаток 59 000 требуют начального AP 45 000 при отсутствии прочих движений. 55 000 = покупки минус остаток, но это не весь банковский платёж. Не исправлять банк до 55 000.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 16, SUP-EVT — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 06 Purchases Invoices and Goods Received.pdf — стр. 1, таблица Supplier / document, строка Event Things Europe — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 16 (заголовок = строка 1), Reference=SUP-EVT
- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 1, Event Things Europe

### D014 — Resolve the source and treatment of January payroll.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (low):** Сумма зарплаты за январь отдельно не установлена. Банк содержит единую строку Jan–Aug 231 000 EUR; таблица даёт начисления 248 000 по подразделениям. Не делить на восемь и не повторять итог как восемь отдельных выплат.

**B (low):** Сумма зарплаты за январь отдельно не установлена (null). Банк содержит один агрегат PAYROLL 231 000 EUR за январь–август; расход за весь период 248 000. Не делить на восемь и не учитывать общий платёж повторно.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 17, PAYROLL — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A4:E7 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 17 (заголовок = строка 1), Reference=PAYROLL
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A4:E7

### D015 — Resolve the source and treatment of February payroll.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (low):** Сумма зарплаты за февраль отдельно не установлена. Банк содержит единую строку Jan–Aug 231 000 EUR; таблица даёт начисления 248 000 по подразделениям. Не делить на восемь и не повторять итог как восемь отдельных выплат.

**B (low):** Сумма зарплаты за февраль отдельно не установлена (null). Банк содержит один агрегат PAYROLL 231 000 EUR за январь–август; расход за весь период 248 000. Не делить на восемь и не учитывать общий платёж повторно.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 17, PAYROLL — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A4:E7 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 17 (заголовок = строка 1), Reference=PAYROLL
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A4:E7

### D016 — Resolve the source and treatment of March payroll.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (low):** Сумма зарплаты за март отдельно не установлена. Банк содержит единую строку Jan–Aug 231 000 EUR; таблица даёт начисления 248 000 по подразделениям. Не делить на восемь и не повторять итог как восемь отдельных выплат.

**B (low):** Сумма зарплаты за март отдельно не установлена (null). Банк содержит один агрегат PAYROLL 231 000 EUR за январь–август; расход за весь период 248 000. Не делить на восемь и не учитывать общий платёж повторно.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 17, PAYROLL — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A4:E7 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 17 (заголовок = строка 1), Reference=PAYROLL
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A4:E7

### D017 — Resolve the source and treatment of April payroll.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (low):** Сумма зарплаты за апрель отдельно не установлена. Банк содержит единую строку Jan–Aug 231 000 EUR; таблица даёт начисления 248 000 по подразделениям. Не делить на восемь и не повторять итог как восемь отдельных выплат.

**B (low):** Сумма зарплаты за апрель отдельно не установлена (null). Банк содержит один агрегат PAYROLL 231 000 EUR за январь–август; расход за весь период 248 000. Не делить на восемь и не учитывать общий платёж повторно.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 17, PAYROLL — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A4:E7 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 17 (заголовок = строка 1), Reference=PAYROLL
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A4:E7

### D018 — Resolve the source and treatment of May payroll.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (low):** Сумма зарплаты за май отдельно не установлена. Банк содержит единую строку Jan–Aug 231 000 EUR; таблица даёт начисления 248 000 по подразделениям. Не делить на восемь и не повторять итог как восемь отдельных выплат.

**B (low):** Сумма зарплаты за май отдельно не установлена (null). Банк содержит один агрегат PAYROLL 231 000 EUR за январь–август; расход за весь период 248 000. Не делить на восемь и не учитывать общий платёж повторно.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 17, PAYROLL — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A4:E7 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 17 (заголовок = строка 1), Reference=PAYROLL
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A4:E7

### D019 — Resolve the source and treatment of June payroll.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (low):** Сумма зарплаты за июнь отдельно не установлена. Банк содержит единую строку Jan–Aug 231 000 EUR; таблица даёт начисления 248 000 по подразделениям. Не делить на восемь и не повторять итог как восемь отдельных выплат.

**B (low):** Сумма зарплаты за июнь отдельно не установлена (null). Банк содержит один агрегат PAYROLL 231 000 EUR за январь–август; расход за весь период 248 000. Не делить на восемь и не учитывать общий платёж повторно.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 17, PAYROLL — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A4:E7 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 17 (заголовок = строка 1), Reference=PAYROLL
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A4:E7

### D020 — Resolve the source and treatment of July payroll.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (low):** Сумма зарплаты за июль отдельно не установлена. Банк содержит единую строку Jan–Aug 231 000 EUR; таблица даёт начисления 248 000 по подразделениям. Не делить на восемь и не повторять итог как восемь отдельных выплат.

**B (low):** Сумма зарплаты за июль отдельно не установлена (null). Банк содержит один агрегат PAYROLL 231 000 EUR за январь–август; расход за весь период 248 000. Не делить на восемь и не учитывать общий платёж повторно.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 17, PAYROLL — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A4:E7 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 17 (заголовок = строка 1), Reference=PAYROLL
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A4:E7

### D021 — Resolve the source and treatment of August payroll.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (low):** Сумма зарплаты за август отдельно не установлена. Банк содержит единую строку Jan–Aug 231 000 EUR; таблица даёт начисления 248 000 по подразделениям. Не делить на восемь и не повторять итог как восемь отдельных выплат.

**B (low):** Сумма зарплаты за август отдельно не установлена (null). Банк содержит один агрегат PAYROLL 231 000 EUR за январь–август; расход за весь период 248 000. Не делить на восемь и не учитывать общий платёж повторно.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 17, PAYROLL — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A4:E7 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 17 (заголовок = строка 1), Reference=PAYROLL
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A4:E7

### D022 — Resolve the source and treatment of Rent payments.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Аренда Jan–Aug: выплачено 48,000 EUR, операционный денежный поток. Предварительно расход периода; договоров/счетов для проверки авансов и начислений нет.

**B (medium):** Банковский платёж 48 000 EUR: аренда января–августа. В предварительном P&L — операционный расход периода. Сумма платежа подтверждена  периодизация расходов требует счетов/договоров.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 18, RENT — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 18 (заголовок = строка 1), Reference=RENT

### D023 — Resolve the source and treatment of Meta and influencer payments.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Meta, TikTok и influencers: выплачено 55,000 EUR, операционный денежный поток. Предварительно расход периода; договоров/счетов для проверки авансов и начислений нет.

**B (medium):** Банковский платёж 55 000 EUR: Meta  TikTok и influencers. В предварительном P&L — операционный расход периода. Сумма платежа подтверждена  периодизация расходов требует счетов/договоров.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 19, MKT — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 19 (заголовок = строка 1), Reference=MKT

### D024 — Resolve the source and treatment of Software payments.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Подписки ПО: выплачено 16,000 EUR, операционный денежный поток. Предварительно расход периода; договоров/счетов для проверки авансов и начислений нет.

**B (medium):** Банковский платёж 16 000 EUR: подписки на ПО. В предварительном P&L — операционный расход периода. Сумма платежа подтверждена  периодизация расходов требует счетов/договоров.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 20, SOFT — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 20 (заголовок = строка 1), Reference=SOFT

### D025 — Resolve the source and treatment of Utilities payments.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Коммунальные услуги: выплачено 12,000 EUR, операционный денежный поток. Предварительно расход периода; договоров/счетов для проверки авансов и начислений нет.

**B (medium):** Банковский платёж 12 000 EUR: коммунальные услуги. В предварительном P&L — операционный расход периода. Сумма платежа подтверждена  периодизация расходов требует счетов/договоров.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 21, UTIL — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 21 (заголовок = строка 1), Reference=UTIL

### D026 — Resolve the source and treatment of Repair transfer.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** 10 000 EUR — ремонт R-771: замена ремня, очистка, калибровка; восстановление нормальной работы. Расход периода, операционная выплата, не увеличение PPE.

**B (high):** Оплачено 10 000 EUR за R-771: замена ремня, очистка и калибровка. Расход ремонта и операционный отток; улучшения 0.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 22, REPAIR — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 06 Purchases Invoices and Goods Received.pdf — стр. 2, R-771 — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view
- 08 Assets Repairs Leases Maybe.xlsx — 'Assets'!A7:E7 — https://docs.google.com/spreadsheets/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/edit

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 22 (заголовок = строка 1), Reference=REPAIR
- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 2, R-771
- [08 Assets Repairs Leases Maybe.xlsx](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view) — Assets!A7:E7

### D027 — Resolve the source and treatment of Packaging machine payment.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** 60,000 EUR — оборудование по A-910; капитализация в PPE, инвестиционная выплата. Доступно для использования 10 мая; амортизация отдельно. Не считать одновременно ремонтом/маркетингом.

**B (high):** 60 000 EUR A-910 — оборудование, введённое 10 мая. Капитализация в PPE и инвестиционный отток; платёж отражён банковским агрегатом 31 августа.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 23, CAPEX-PACK — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 06 Purchases Invoices and Goods Received.pdf — стр. 2, A-910 — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view
- 08 Assets Repairs Leases Maybe.xlsx — 'Assets'!A5:E5 — https://docs.google.com/spreadsheets/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/edit

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 23 (заголовок = строка 1), Reference=CAPEX-PACK
- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 2, A-910
- [08 Assets Repairs Leases Maybe.xlsx](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view) — Assets!A5:E5

### D028 — Resolve the source and treatment of Photo booth payment.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** 20,000 EUR — оборудование по P-404; капитализация в PPE, инвестиционная выплата. Доступно для использования 10 мая; амортизация отдельно. Не считать одновременно ремонтом/маркетингом.

**B (high):** 20 000 EUR P-404 — фотобудка, готовая к использованию 10 мая. PPE и инвестиционный отток, не маркетинговый расход.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 24, CAPEX-PHOTO — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 06 Purchases Invoices and Goods Received.pdf — стр. 2, P-404 — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view
- 08 Assets Repairs Leases Maybe.xlsx — 'Assets'!A6:E6 — https://docs.google.com/spreadsheets/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/edit

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 24 (заголовок = строка 1), Reference=CAPEX-PHOTO
- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 2, P-404
- [08 Assets Repairs Leases Maybe.xlsx](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view) — Assets!A6:E6

### D029 — Resolve the source and treatment of Loan receipt.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** 50 000 EUR — новый возвратный банковский заём, финансовое поступление и увеличение долга; не выручка и не иной доход.

**B (high):** Полученные 1 марта 50 000 EUR — новый банковский заём, финансовый приток и обязательство, не доход.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 5, LOAN-ADV — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 09 Loans Owner Card and Legal Problems.pdf — стр. 1, New advance 1 Mar — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 5 (заголовок = строка 1), Reference=LOAN-ADV
- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1, New advance

### D030 — Resolve the source and treatment of Loan repayments.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** 19 000 EUR — погашение основного долга, финансовый отток и уменьшение заимствований; не расход P&L.

**B (high):** 19 000 EUR — погашение principal; уменьшает долг, финансовый отток, не расход P&L.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 26, PRINCIPAL — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 09 Loans Owner Card and Legal Problems.pdf — стр. 1, Principal repaid — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 26 (заголовок = строка 1), Reference=PRINCIPAL
- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1, Principal repaid

### D031 — Resolve the source and treatment of Interest payments.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** 10 000 EUR процентов уплачено; расход периода 12 000 и обязательство 2 000. Для проекта Cash Flow уплаченные проценты классифицированы в операционной деятельности.

**B (high):** Проценты уплачены 10 000 EUR; расход периода 12 000 и закрывающий payable 2 000. В Cash Flow B проценты классифицированы как операционные.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 25, INT — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 09 Loans Owner Card and Legal Problems.pdf — стр. 1, Interest expense / paid — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view
- 11 Evidence Received After Takeover.pdf — стр. 1, Bank confirmation — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 25 (заголовок = строка 1), Reference=INT
- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1, Interest expense/paid
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, Bank confirmation

### D032 — Resolve the source and treatment of Villa deposit.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** 70,000 EUR — личные расходы владельца; предварительно распределение капитала и финансовый отток, не бизнес-расход. Отдельного подтверждённого права взыскания с владельца нет; юридическую возможность возврата исследовать. Это часть тех же 110 000, ошибочно названных founder bonus.

**B (medium):** 70 000 EUR на личную виллу собственника — распределение капитала и финансовый отток; не маркетинг и не зарплата. Юридически подтверждённого требования к владельцу в пакете нет.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств. B дополнительно сообщает о датах августа 2024 на изображении брони при банковском платеже 2026. Это наблюдение B, не повторно проверенный факт текущего сопоставления; период и сумма сторонами не изменены.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 27, VILLA — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 09 Loans Owner Card and Legal Problems.pdf — стр. 1, таблица Item, строка Owner villa reservation — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A8:E8 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit
- 10 Email and WhatsApp Dump DO NOT FORWARD.pdf — стр. 2 — https://drive.google.com/file/d/1kK0lLv_CdpYXaB9KaH6H_8WELuQxcJ5I/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 27 (заголовок = строка 1), Reference=VILLA
- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1, Owner villa reservation; стр. 2, изображение бронирования
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A8:E8

### D033 — Resolve the source and treatment of Owner card spending.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** 40,000 EUR — личные расходы владельца; предварительно распределение капитала и финансовый отток, не бизнес-расход. Отдельного подтверждённого права взыскания с владельца нет; юридическую возможность возврата исследовать. Это часть тех же 110 000, ошибочно названных founder bonus.

**B (medium):** 40 000 EUR owner card — предварительно распределение собственнику. В сумме с виллой 110 000 совпадает с неподтверждённым founder bonus; это одна экономическая группа, не дополнительная зарплата.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 28, OWNERCARD — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 09 Loans Owner Card and Legal Problems.pdf — стр. 1, таблица Item, строка Other owner card spending — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A8:E8 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit
- 10 Email and WhatsApp Dump DO NOT FORWARD.pdf — стр. 2 — https://drive.google.com/file/d/1kK0lLv_CdpYXaB9KaH6H_8WELuQxcJ5I/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 28 (заголовок = строка 1), Reference=OWNERCARD
- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1, Other owner card spending
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A8:E8

### D034 — Resolve the source and treatment of Insurance movement.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (low):** Числовой ответ не установлен: в 12 файлах кейса отсутствуют страховой полис, начальная/конечная предоплата, период покрытия и сумма потребления. В банковских строках 2–28 отдельной страховой операции нет. Отсутствие строки не доказывает нулевой расход. Не заполнять пропуск числом из учебного справочника.

**B (low):** Движение страхования не определено: null. В полном банковском CSV нет отдельного insurance payment; это не доказывает отсутствие страхового расхода или начальной предоплаты. Проводку и сумму не выдумывать.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — все строки 1–28 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 01 GIVE TO CODEX - Answer Template.json — $.decisions[33], D034 — только вопрос, не доказательство суммы — https://drive.google.com/file/d/1WwIhOYZRY8RVEioasYWj1C6hR7EDPJKn/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — весь CSV, строки 2–28
- [01 GIVE TO CODEX - Answer Template.json](https://drive.google.com/file/d/1WwIhOYZRY8RVEioasYWj1C6hR7EDPJKn/view) — decisions[id=D034], D060 и D078

### D035 — Resolve the source and treatment of Water-damaged stock.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Повреждённый складской остаток 22 000 EUR физически существует, но не имеет продажной стоимости: списать полностью. Оценка будущей утилизации 2 000 отдельно; в базовом черновике не начислена без доказательства существующего обязательства.

**B (high):** Подвальный запас балансовой стоимостью 22 000 EUR физически существует, но неликвиден: обесценение на всю сумму. Оценка будущего вывоза 2 000 отдельна.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 05 Warehouse Count Marta Notes.pdf — стр. 1, Basement premium; стр. 2, disposal quote — https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view
- 11 Evidence Received After Takeover.pdf — стр. 1, Independent stock assessment — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view

**Evidence B (из исходного JSON):**

- [05 Warehouse Count Marta Notes.pdf](https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view) — стр. 1, Basement premium stock; стр. 2
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, Independent stock assessment

### D036 — Resolve the source and treatment of Customer insolvency.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** R-17: признать 100% резерв 18 000 EUR против дебиторской задолженности. Сообщение ликвидатора 3 сентября подтверждает состояние на 31 августа. Название Return не доказывает возврат товара или аннулирование выручки.

**B (high):** R-17: 18 000 EUR без ожидаемого взыскания. Позднее уведомление подтверждает состояние на 31 августа; признать полный резерв/списание, не возврат выручки.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 04 Contracts Returns and Angry Customers.pdf — стр. 2, Return R-17 и последний абзац — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!I9 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit
- 11 Evidence Received After Takeover.pdf — стр. 1, R-17 — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view

**Evidence B (из исходного JSON):**

- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 2, Return R-17
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, liquidator notice
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!A9:I9

### D037 — Resolve the source and treatment of Former employee claim.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Признать расход и резерв по требованию бывшего сотрудника 25 000 EUR; диапазон 20 000–30 000. Оплаты до отчётной даты не было.

**B (high):** Иск бывшего работника: признать расход и provision 25 000 EUR, диапазон 20 000–30 000. Платежа на дату отчётности нет.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 09 Loans Owner Card and Legal Problems.pdf — стр. 2, первый и второй абзацы — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view
- 11 Evidence Received After Takeover.pdf — стр. 1, External lawyer confirmation — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view

**Evidence B (из исходного JSON):**

- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 2, External counsel
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, External lawyer confirmation

### D038 — Resolve the source and treatment of Purchase total.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Закупки материалов 459 000 EUR = 130 000 + 120 000 + 95 000 + 114 000. Все товары получены до 31 августа. Это поступления запасов, не автоматически COGS; неоплачено 126 000.

**B (high):** Покупки полученных материалов 459 000 EUR = 130 000 + 120 000 + 95 000 + 114 000. Не путать с платежами 378 000 и не включать оборудование 80 000 второй раз.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Evidence A (из исходного JSON):**

- 06 Purchases Invoices and Goods Received.pdf — стр. 1, все четыре строки и TOTAL — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view

**Evidence B (из исходного JSON):**

- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 1, все четыре строки и TOTAL
- [05 Warehouse Count Marta Notes.pdf](https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view) — стр. 2, Purchases
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строки 13–16, SUP-*

### D039 — Resolve the source and treatment of Cash collections total.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Поступления покупателей 899 000 EUR = 774 000 по текущим продажам + 35 000 по старой AR + 90 000 авансы. Все внешние поступления 949 000 с учётом займа 50 000. Начальные деньги 80 000 не являются поступлением периода.

**B (high):** Клиентские поступления 899 000 EUR = текущие продажи 774 000 + начальная AR 35 000 + авансы сентября 90 000. Все новые денежные поступления 949 000 с займом 50 000; opening cash 80 000 не является притоком периода.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строки 2–12 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!F4:F11 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строки 2–12
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!F4:F11

### D040 — Resolve the source and treatment of Closing bank balance.

`evidence_matching` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Закрывающий банковский остаток 60 000 EUR; 80 000 + 949 000 − 969 000 = 60 000. Каждое промежуточное сальдо CSV проверено.

**B (high):** Закрывающие деньги 60 000 EUR = 80 000 + 949 000 − 969 000. Подтверждено банком после отчётной даты; management cash 186 000 отвергнут.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — все строки 1–28, конечная строка 28 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 11 Evidence Received After Takeover.pdf — стр. 1, Bank confirmation — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строки 2–28
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, Bank confirmation
- [01 USE THIS NUMBERS FINAL v9.xlsx](https://drive.google.com/file/d/1G76Riktxa2_Ytz6DJB65G7n1saetdna9/view) — Management P&L!A9:C9

### D041 — Classify September customer deposits.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** 90 000 EUR сентябрьских авансов признать договорными обязательствами, не августовской выручкой.

**B (high):** Сентябрьские авансы 90 000 EUR классифицировать как contract liabilities; выручка 0 на 31 августа.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Обоснование A:** До 31 августа ни товары, ни услуги не переданы. Дата оплаты определяет деньги, а не выполнение обязательства.

**Эффект A:** `{"profit": -90000, "cash": 0, "assets": 0, "liabilities": 90000, "equity": -90000}`. **База:** Исправление включённых в management sales авансов; деньги уже отражены. Повторяется в D068/D081/D093, проводится один раз.

**Обоснование B:** Получение денег не означает исполнение. По договорным данным обе даты исполнения относятся к сентябрю, а на отчётную дату поставки отсутствуют. Названия Won и August sales не меняют это.

**Эффект B:** `{"profit": -90000, "cash": 0, "assets": 0, "liabilities": 90000, "equity": -90000}`. **База:** Коррекция ошибочной выручки по уже полученным авансам; те же суммы в D068 и D093, не три проводки.

**Evidence A (из исходного JSON):**

- 04 Contracts Returns and Angry Customers.pdf — стр. 2, NB-SEP / FF-SEP — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view
- 02 Bank Export August.csv — строки 11–12 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 2, NB-SEP и FF-SEP
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строки 11–12

### D042 — Classify New bank borrowing.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Заём 50 000 EUR — финансовое обязательство; убрать strategic bank income из прибыли.

**B (high):** Банковский аванс 50 000 EUR — заём, не strategic income.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Обоснование A:** Подтверждено требование возврата по соглашению; источник финансирования не создаёт заработанного дохода.

**Эффект A:** `{"profit": -50000, "cash": 0, "assets": 0, "liabilities": 50000, "equity": -50000}`. **База:** Исправление ошибочного дохода при уже отражённых деньгах.

**Обоснование B:** Есть обязанность возврата и банковское поступление; дохода по этой операции нет. Само финансирование не свидетельствует о прибыльности бизнеса.

**Эффект B:** `{"profit": -50000, "cash": 0, "assets": 0, "liabilities": 50000, "equity": -50000}`. **База:** Переклассификация уже полученного займа из ошибочного дохода в долг. Денежный приток 50 000 учтён отдельно в CF.

**Evidence A (из исходного JSON):**

- 09 Loans Owner Card and Legal Problems.pdf — стр. 1, первый абзац — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view
- 02 Bank Export August.csv — строка 5, LOAN-ADV — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 01 USE THIS NUMBERS FINAL v9.xlsx — 'Management P&L'!A5:C5 — https://docs.google.com/spreadsheets/d/1G76Riktxa2_Ytz6DJB65G7n1saetdna9/edit

**Evidence B (из исходного JSON):**

- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1, Bank and agreement
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 5 (заголовок = строка 1), Reference=LOAN-ADV

### D043 — Classify Packaging machine.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Капитализировать 60,000 EUR оборудования в PPE; готовность к использованию 10 мая, амортизация начинается при готовности. Конкретная сумма амортизации по объекту не установлена.

**B (high):** Упаковочная машина: первоначальная стоимость PPE 60000 EUR, использование с 10 мая. Амортизация обязательна; отдельную её сумму по объекту установить нельзя.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Обоснование A:** Оборудование создаёт длительно используемый ресурс. Управленческая категория repair/marketing не меняет экономическую природу.

**Эффект A:** `{"profit": 60000, "cash": 0, "assets": 60000, "liabilities": 0, "equity": 60000}`. **База:** Исправление полного списания приобретения в расходы, до отдельной амортизации; оплата уже отражена.

**Обоснование B:** Счёт и готовность к использованию подтверждают долгосрочный ресурс. Управленческий расход 60000 EUR следует капитализировать. Срок службы и ликвидационная стоимость не представлены, поэтому индивидуальный расчёт амортизации не выдумываю.

**Эффект B:** `{"profit": 60000, "cash": 0, "assets": 60000, "liabilities": 0, "equity": 60000}`. **База:** Переклассификация management expense в PPE до амортизации; фактический CAPEX-отток уже в банке.

**Evidence A (из исходного JSON):**

- 06 Purchases Invoices and Goods Received.pdf — стр. 2, A-910 — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view
- 08 Assets Repairs Leases Maybe.xlsx — 'Assets'!A5:E5 — https://docs.google.com/spreadsheets/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/edit

**Evidence B (из исходного JSON):**

- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 2, A-910
- [08 Assets Repairs Leases Maybe.xlsx](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view) — Assets!A5:E5

### D044 — Classify Photo booth.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Капитализировать 20,000 EUR оборудования в PPE; готовность к использованию 10 мая, амортизация начинается при готовности. Конкретная сумма амортизации по объекту не установлена.

**B (high):** Фотобудка: первоначальная стоимость PPE 20000 EUR, использование с 10 мая. Амортизация обязательна; отдельную её сумму по объекту установить нельзя.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Обоснование A:** Оборудование создаёт длительно используемый ресурс. Управленческая категория repair/marketing не меняет экономическую природу.

**Эффект A:** `{"profit": 20000, "cash": 0, "assets": 20000, "liabilities": 0, "equity": 20000}`. **База:** Исправление полного списания приобретения в расходы, до отдельной амортизации; оплата уже отражена.

**Обоснование B:** Счёт и готовность к использованию подтверждают долгосрочный ресурс. Управленческий расход 20000 EUR следует капитализировать. Срок службы и ликвидационная стоимость не представлены, поэтому индивидуальный расчёт амортизации не выдумываю.

**Эффект B:** `{"profit": 20000, "cash": 0, "assets": 20000, "liabilities": 0, "equity": 20000}`. **База:** Переклассификация management expense в PPE до амортизации; фактический CAPEX-отток уже в банке.

**Evidence A (из исходного JSON):**

- 06 Purchases Invoices and Goods Received.pdf — стр. 2, P-404 — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view
- 08 Assets Repairs Leases Maybe.xlsx — 'Assets'!A6:E6 — https://docs.google.com/spreadsheets/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/edit

**Evidence B (из исходного JSON):**

- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 2, P-404
- [08 Assets Repairs Leases Maybe.xlsx](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view) — Assets!A6:E6

### D045 — Classify Machine belt and calibration.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Ремень, очистка и калибровка 10 000 EUR — ремонт в расходах периода, не улучшение PPE.

**B (high):** R-771 10 000 EUR — текущий ремонт; увеличение PPE 0.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Обоснование A:** Работа только восстановила нормальную мощность; нет увеличения мощности или срока службы.

**Эффект A:** `{"profit": -10000, "cash": 0, "assets": -10000, "liabilities": 0, "equity": -10000}`. **База:** Исправление ошибочной капитализации при уже отражённой выплате.

**Обоснование B:** Счёт говорит о восстановлении обычной производительности без увеличения мощности или срока службы. Это сильнее управленческой пометки PPE.

**Эффект B:** `{"profit": -10000, "cash": 0, "assets": -10000, "liabilities": 0, "equity": -10000}`. **База:** Снятие ошибочной капитализации ремонта; банковский платёж не меняется.

**Evidence A (из исходного JSON):**

- 06 Purchases Invoices and Goods Received.pdf — стр. 2, R-771 — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view
- 08 Assets Repairs Leases Maybe.xlsx — 'Assets'!A7:E7 — https://docs.google.com/spreadsheets/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/edit

**Evidence B (из исходного JSON):**

- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 2, R-771
- [08 Assets Repairs Leases Maybe.xlsx](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view) — Assets!A7:E7
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 22 (заголовок = строка 1), Reference=REPAIR

### D046 — Classify Owner villa deposit.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** 70,000 EUR признать распределением владельцу через капитал; Cash Flow — финансирование. Не расход бизнеса. Возможная дебиторская задолженность владельца требует отдельного доказательства обязанности возврата и взыскуемости.

**B (medium):** 70000 EUR — распределение собственнику, не расход периода; возможное взыскание с владельца пока не признано активом.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств. Дополнительный риск B: даты 2024 на фото брони против 2026 в банке. A фото просмотрел, но количественные выводы строил по тексту. Это различие детализации доказательств, а не принятой классификации.

**Обоснование A:** Личный характер подтверждён документами кейса; employment approval отсутствует. Изменение названия на bonus не создаёт трудовой расход.

**Эффект A:** `{"profit": 70000, "cash": 0, "assets": 0, "liabilities": 0, "equity": 0}`. **База:** Переклассификация уже отражённого личного расхода из P&L в распределение: прибыль растёт, отдельное изъятие капитала компенсирует рост retained earnings; общий капитал неизменен.

**Обоснование B:** Деловая цель и трудовое основание не подтверждены. Нельзя автоматически признать требование к владельцу без основания и оценки взыскания. Выбираю распределение в рамках кейса; его юридическая форма и возмещаемость требуют отдельного подтверждения.

**Эффект B:** `{"profit": 70000, "cash": 0, "assets": 0, "liabilities": 0, "equity": 0}`. **База:** Относительно ошибочного расхода: прибыль +70000, распределения +70000, чистый эффект на equity 0. Фактическая операция уменьшила cash и equity на 70000.

**Evidence A (из исходного JSON):**

- 09 Loans Owner Card and Legal Problems.pdf — стр. 1, Owner villa reservation — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A8:E8 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit
- 10 Email and WhatsApp Dump DO NOT FORWARD.pdf — стр. 2 — https://drive.google.com/file/d/1kK0lLv_CdpYXaB9KaH6H_8WELuQxcJ5I/view

**Evidence B (из исходного JSON):**

- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1, Owner villa reservation
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 27 (заголовок = строка 1), Reference=VILLA
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A8:E8

### D047 — Classify Owner card spending.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** 40,000 EUR признать распределением владельцу через капитал; Cash Flow — финансирование. Не расход бизнеса. Возможная дебиторская задолженность владельца требует отдельного доказательства обязанности возврата и взыскуемости.

**B (medium):** 40000 EUR — распределение собственнику, не расход периода; возможное взыскание с владельца пока не признано активом.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств. B переносит замечание о фото виллы также в uncertainty owner-card. Прямая применимость именно к отдельным 40 000 этим сопоставлением не установлена.

**Обоснование A:** Личный характер подтверждён документами кейса; employment approval отсутствует. Изменение названия на bonus не создаёт трудовой расход.

**Эффект A:** `{"profit": 40000, "cash": 0, "assets": 0, "liabilities": 0, "equity": 0}`. **База:** Переклассификация уже отражённого личного расхода из P&L в распределение: прибыль растёт, отдельное изъятие капитала компенсирует рост retained earnings; общий капитал неизменен.

**Обоснование B:** Деловая цель и трудовое основание не подтверждены. Нельзя автоматически признать требование к владельцу без основания и оценки взыскания. Выбираю распределение в рамках кейса; его юридическая форма и возмещаемость требуют отдельного подтверждения.

**Эффект B:** `{"profit": 40000, "cash": 0, "assets": 0, "liabilities": 0, "equity": 0}`. **База:** Относительно ошибочного расхода: прибыль +40000, распределения +40000, чистый эффект на equity 0. Фактическая операция уменьшила cash и equity на 40000.

**Evidence A (из исходного JSON):**

- 09 Loans Owner Card and Legal Problems.pdf — стр. 1, Other owner card spending — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A8:E8 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit
- 10 Email and WhatsApp Dump DO NOT FORWARD.pdf — стр. 2 — https://drive.google.com/file/d/1kK0lLv_CdpYXaB9KaH6H_8WELuQxcJ5I/view

**Evidence B (из исходного JSON):**

- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1, Other owner card spending
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 28 (заголовок = строка 1), Reference=OWNERCARD
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A8:E8

### D048 — Classify Physical product materials consumed.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Материалы, потреблённые для выполненных продаж, 405 000 EUR — physical COGS. Списание испорченных запасов 22 000 отдельно. Указанное потребление не сходится со складским остатком: разница 9 000.

**B (low):** Материалы, потреблённые в поставленных товарах: предварительный COGS 405 000 EUR. Покупки 459 000 и платежи 378 000 не являются COGS.

**Отличия/оговорки сравнения:** Оба оставляют inventory/COGS gap 9 000 открытым. A: medium для предварительной рабочей величины; B: low из-за неразрешённого противоречия.

**Обоснование A:** Расход признаётся по потреблению на выполненные продажи. Прямое утверждение 405 000 сохранено в P&L, но не использовано для скрытого исправления складского подсчёта.

**Эффект A:** `{"profit": -405000, "cash": 0, "assets": -405000, "liabilities": 0, "equity": -405000}`. **База:** Запись потребления запасов относительно состояния до потребления; не дельта к management P&L. Разница движения 9 000 не исправлена.

**Обоснование B:** Использую прямо указанное потребление для P&L, но оно противоречит инвентаризации на 9 000. Расчёт от инвентаризации дал бы 396 000. Снижение COGS без первичных движений создало бы неподтверждённую прибыль.

**Эффект B:** `{"profit": -405000, "cash": 0, "assets": -405000, "liabilities": 0, "equity": -405000}`. **База:** Признание потребления запасов; не дельта к управленческим 620 000, где материалы и зарплата смешаны.

**Evidence A (из исходного JSON):**

- 05 Warehouse Count Marta Notes.pdf — стр. 2, первый абзац; стр. 1, таблица — https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view
- 06 Purchases Invoices and Goods Received.pdf — стр. 1, TOTAL — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view

**Evidence B (из исходного JSON):**

- [05 Warehouse Count Marta Notes.pdf](https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view) — стр. 2, Physical product materials consumed
- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 1, TOTAL

### D049 — Classify Event staff payroll.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Начисленные 80 000 EUR event delivery staff отнести к прямой себестоимости услуг; выплата 75 000 не заменяет начисление.

**B (medium):** Event delivery staff 80 000 EUR — прямые затраты услуг, не admin. Выплачено 75 000; увеличение payroll payable по этому блоку 5 000, его начальная доля неизвестна.

**Отличия/оговорки сравнения:** Суммы и функции payroll совпадают. A ставит high по классификации/арифметике; B — medium по внутренней ведомости и её ограничениям. Это различная оценка надёжности, не иной расчёт.

**Обоснование A:** Сотрудники непосредственно исполняют оплаченные мероприятия. Перенос из admin в COGS меняет валовую прибыль, но не общую прибыль.

**Эффект A:** `{"profit": 0, "cash": 0, "assets": 0, "liabilities": 0, "equity": 0}`. **База:** Только переклассификация admin → direct service COGS; gross profit −80 000, admin expense −80 000. Начисление уже учтено в общем payroll.

**Обоснование B:** Функция работников прямо связана с выполненными мероприятиями. Классификация влияет на gross margin, но сама переклассификация из admin не меняет итоговую прибыль.

**Эффект B:** `{"profit": 0, "cash": 0, "assets": 0, "liabilities": 0, "equity": 0}`. **База:** Только переклассификация 80 000 из admin в service COGS; признание всего payroll отражено в ведомости.

**Evidence A (из исходного JSON):**

- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A4:E4 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit

**Evidence B (из исходного JSON):**

- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A4:E4

### D050 — Classify Sales team payroll.

`classification` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Коммерческая зарплата — selling expenses: начислено 72,000 EUR. Не включать в себестоимость товаров. Разницу с оплатой учитывать в общей зарплатной кредиторской задолженности.

**B (medium):** Sales and partnerships: 72 000 EUR — коммерческие Opex, не COGS. Cash 68 000; прирост задолженности 4 000.

**Отличия/оговорки сравнения:** Суммы и функции payroll совпадают. A ставит high по классификации/арифметике; B — medium по внутренней ведомости и её ограничениям. Это различная оценка надёжности, не иной расчёт.

**Evidence A (из исходного JSON):**

- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A5:E5 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit

**Evidence B (из исходного JSON):**

- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A5:E5

### D051 — Classify Office payroll.

`classification` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Офис и финансы — administrative expenses: начислено 96,000 EUR. Не включать в себестоимость товаров. Разницу с оплатой учитывать в общей зарплатной кредиторской задолженности.

**B (medium):** Office and finance: 96 000 EUR — административные Opex. Cash 88 000; прирост задолженности 8 000.

**Отличия/оговорки сравнения:** Суммы и функции payroll совпадают. A ставит high по классификации/арифметике; B — medium по внутренней ведомости и её ограничениям. Это различная оценка надёжности, не иной расчёт.

**Evidence A (из исходного JSON):**

- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A6:E6 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit

**Evidence B (из исходного JSON):**

- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A6:E6

### D052 — Classify Rent.

`classification` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Аренда: предварительный operating expense 48,000 EUR по банковскому назначению. Распределение по функциям, предоплаты и неоплаченные счета не подтверждены.

**B (medium):** Банковский платёж 48 000 EUR: аренда января–августа. В предварительном P&L — операционный расход периода. Сумма платежа подтверждена  периодизация расходов требует счетов/договоров.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 18, RENT — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 18 (заголовок = строка 1), Reference=RENT

### D053 — Classify Marketing.

`classification` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Маркетинг: предварительный operating expense 55,000 EUR по банковскому назначению. Распределение по функциям, предоплаты и неоплаченные счета не подтверждены.

**B (medium):** Банковский платёж 55 000 EUR: Meta  TikTok и influencers. В предварительном P&L — операционный расход периода. Сумма платежа подтверждена  периодизация расходов требует счетов/договоров.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 19, MKT — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 19 (заголовок = строка 1), Reference=MKT

### D054 — Classify Software.

`classification` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** ПО: предварительный operating expense 16,000 EUR по банковскому назначению. Распределение по функциям, предоплаты и неоплаченные счета не подтверждены.

**B (medium):** Банковский платёж 16 000 EUR: подписки на ПО. В предварительном P&L — операционный расход периода. Сумма платежа подтверждена  периодизация расходов требует счетов/договоров.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 20, SOFT — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 20 (заголовок = строка 1), Reference=SOFT

### D055 — Classify Utilities.

`classification` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Коммунальные услуги: предварительный operating expense 12,000 EUR по банковскому назначению. Распределение по функциям, предоплаты и неоплаченные счета не подтверждены.

**B (medium):** Банковский платёж 12 000 EUR: коммунальные услуги. В предварительном P&L — операционный расход периода. Сумма платежа подтверждена  периодизация расходов требует счетов/договоров.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 21, UTIL — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 21 (заголовок = строка 1), Reference=UTIL

### D056 — Classify Depreciation.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Амортизация — неденежный расход периода и рост накопленной амортизации; предварительная сумма 24 000 EUR. Функциональное распределение на производство/услуги/администрацию не дано, поэтому показана отдельно.

**B (low):** Амортизация — неденежный расход периода, предварительно 24 000 EUR. Для сводного P&L показана отдельной строкой; функциональную долю COGS/Opex нельзя доказать.

**Отличия/оговорки сравнения:** Оба используют предварительные 24 000 без исходного depreciation schedule. A: medium; B: low. Никакая сторона не воспроизвела оценку по срокам/стоимостям. Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Обоснование A:** Нулевое отражение управленца противоречит использованию PPE. В E8 приведена оценка independent schedule, но самого расчёта, сроков и остаточных стоимостей нет.

**Эффект A:** `{"profit": -24000, "cash": 0, "assets": -24000, "liabilities": 0, "equity": -24000}`. **База:** Начисление отсутствующей амортизации; общий эффект D074 тот же, не дополнительный.

**Обоснование B:** Management ноль не соответствует использованию PPE. Однако 24 000 — только ссылка в Excel на независимый расчёт, сам расчёт отсутствует. Не выдаю её за самостоятельно проверенную оценку.

**Эффект B:** `{"profit": -24000, "cash": 0, "assets": -24000, "liabilities": 0, "equity": -24000}`. **База:** Предварительная корректировка отсутствующей амортизации; повторена в D074, не суммировать.

**Evidence A (из исходного JSON):**

- 08 Assets Repairs Leases Maybe.xlsx — 'Assets'!A8:E8 — https://docs.google.com/spreadsheets/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/edit

**Evidence B (из исходного JSON):**

- [08 Assets Repairs Leases Maybe.xlsx](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view) — Assets!A8:E8; A4:E6
- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 2, A-910/P-404

### D057 — Classify Bad receivable.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** 18 000 EUR по R-17 — расход обесценения AR; сохранить валовую выручку и показать 100% резерв. Это не подтверждённый возврат продаж.

**B (high):** R-17: 100% allowance 18 000 EUR против gross AR; признать расход обесценения, не sales return.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Обоснование A:** Ликвидация и отсутствие ожидаемого распределения подтверждают неполучаемость существующего требования на отчётную дату.

**Эффект A:** `{"profit": -18000, "cash": 0, "assets": -18000, "liabilities": 0, "equity": -18000}`. **База:** Первичное признание резерва; D071 описывает ту же оценку.

**Обоснование B:** Слово Return в названии не подтверждает возврат товара: содержание описывает ликвидацию и невозможность взыскания. Сохраняю gross AR и резерв для прозрачного следа; net эффект равен прямому списанию.

**Эффект B:** `{"profit": -18000, "cash": 0, "assets": -18000, "liabilities": 0, "equity": -18000}`. **База:** Полное обесценение R-17; повтор D071.

**Evidence A (из исходного JSON):**

- 04 Contracts Returns and Angry Customers.pdf — стр. 2, R-17 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view
- 11 Evidence Received After Takeover.pdf — стр. 1, liquidator notice — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!I9 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit

**Evidence B (из исходного JSON):**

- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 2, R-17
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, liquidator notice
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!I9

### D058 — Classify Damaged stock.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Списать 22 000 EUR испорченного stock в отдельную строку потерь запасов внутри себестоимости. Будущие 2 000 утилизации раскрыть отдельно, не уменьшать inventory ниже нуля.

**B (high):** Списать стоимость повреждённых запасов 22 000 EUR до нуля. Расход вывоза 2 000 не включать в стоимость списанного запаса и не создавать отрицательный запас.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Обоснование A:** Вещи присутствуют физически, но продажная стоимость равна нулю. Котировка утилизации не равна оплаченному расходу или сама по себе существующему обязательству.

**Эффект A:** `{"profit": -22000, "cash": 0, "assets": -22000, "liabilities": 0, "equity": -22000}`. **База:** Списание стоимости stock; 2 000 disposal не включены. D072 — тот же эффект.

**Обоснование B:** Физическое наличие не подтверждает возмещаемую стоимость. Нулевая реализация подтверждена внешней оценкой. Котировка вывоза сама по себе не доказывает существующее обязательство на 31 августа, поэтому provision на 2 000 пока не признан; расход/отток включить в план и раскрыть сценарий.

**Эффект B:** `{"profit": -22000, "cash": 0, "assets": -22000, "liabilities": 0, "equity": -22000}`. **База:** Списание запасов; при подтверждении обязанности вывоза отдельный расход и liability +2 000, profit/equity −2 000.

**Evidence A (из исходного JSON):**

- 05 Warehouse Count Marta Notes.pdf — стр. 1, Basement premium; стр. 2, disposal quote — https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view
- 11 Evidence Received After Takeover.pdf — стр. 1, stock assessment — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view

**Evidence B (из исходного JSON):**

- [05 Warehouse Count Marta Notes.pdf](https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view) — стр. 1–2, basement stock и disposal quote
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, stock assessment

### D059 — Classify Probable legal claim.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Признать provision и operating expense 25 000 EUR по employee claim; раскрыть 20 000–30 000.

**B (high):** Вероятный иск: расход и резерв 25 000 EUR на 31 августа; range 20 000–30 000.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Обоснование A:** Существующее на 31 августа требование вероятно и оценимо; позднее подтверждение не переносит расход в сентябрь.

**Эффект A:** `{"profit": -25000, "cash": 0, "assets": 0, "liabilities": 25000, "equity": -25000}`. **База:** Признание ранее пропущенного резерва; D073 не является вторым начислением.

**Обоснование B:** Юрист подтвердил существовавший на отчётную дату вероятный исход и лучшую оценку. Отсутствие оплаты не устраняет обязательство, а отсутствие окончательного решения суда не требует ожидать денежного платежа.

**Эффект B:** `{"profit": -25000, "cash": 0, "assets": 0, "liabilities": 25000, "equity": -25000}`. **База:** Признание резерва; те же 25 000 в D073, не повторная проводка.

**Evidence A (из исходного JSON):**

- 09 Loans Owner Card and Legal Problems.pdf — стр. 2 — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view
- 11 Evidence Received After Takeover.pdf — стр. 1, lawyer confirmation — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view

**Evidence B (из исходного JSON):**

- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 2, counsel 31 August
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, lawyer confirmation

### D060 — Classify Insurance consumed.

`classification` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (low):** Потреблённое страхование должно быть расходом с уменьшением prepaid insurance или ростом обязательства, но сумма и проводка не установлены. Числовой ответ не установлен: в 12 файлах кейса отсутствуют страховой полис, начальная/конечная предоплата, период покрытия и сумма потребления. В банковских строках 2–28 отдельной страховой операции нет. Отсутствие строки не доказывает нулевой расход. Не заполнять пропуск числом из учебного справочника.

**B (low):** Потреблённое страховое покрытие относится в Opex с уменьшением предоплаты либо увеличением payable. Сумма и встречный счёт неизвестны (null).

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — все строки 1–28 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 01 GIVE TO CODEX - Answer Template.json — $.decisions[59], D060 — https://drive.google.com/file/d/1WwIhOYZRY8RVEioasYWj1C6hR7EDPJKn/view

**Evidence B (из исходного JSON):**

- [01 GIVE TO CODEX - Answer Template.json](https://drive.google.com/file/d/1WwIhOYZRY8RVEioasYWj1C6hR7EDPJKn/view) — decisions[id=D060], D034, D078
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — полный CSV, строки 2–28: отдельного insurance payment нет

### D061 — Classify Unpaid interest.

`classification` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** 2 000 EUR unpaid interest — начисленное обязательство, а не новый расход поверх 12 000. 12 000 начислено − 10 000 уплачено = 2 000, совпадает с поздним банковским подтверждением.

**B (high):** Неоплаченные проценты 2 000 EUR — обязательство и часть расхода 12 000, не дополнительный расход сверх 12 000.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 09 Loans Owner Card and Legal Problems.pdf — стр. 1, interest — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view
- 11 Evidence Received After Takeover.pdf — стр. 1, Bank confirmation — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view

**Evidence B (из исходного JSON):**

- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1, Interest expense/paid
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, bank accrued unpaid interest

### D062 — Classify Unpaid payroll.

`classification` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Closing payroll payable 32 000 EUR = opening 15 000 + expense 248 000 − cash 231 000. Founder bonus 110 000 исключён как те же личные изъятия, не зарплата.

**B (medium):** Payroll payable предварительно 32 000 EUR = opening 15 000 + expense 248 000 − cash 231 000. Founder bonus 110 000 исключён как дубль distributions.

**Отличия/оговорки сравнения:** Суммы и функции payroll совпадают. A ставит high по классификации/арифметике; B — medium по внутренней ведомости и её ограничениям. Это различная оценка надёжности, не иной расчёт.

**Evidence A (из исходного JSON):**

- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A4:E8 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit
- 02 Bank Export August.csv — строка 17, PAYROLL — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A4:E8
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 17 (заголовок = строка 1), Reference=PAYROLL

### D063 — Classify Unpaid suppliers.

`classification` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Кредиторская задолженность поставщикам 126 000 EUR = 25 000 + 28 000 + 14 000 + 59 000. Это обязательство, не дополнительная сумма COGS.

**B (high):** Торговый AP 126 000 EUR: 25 000 BoxWorks + 28 000 Glass + 14 000 Print + 59 000 Event Things. Это обязательства по полученным материалам, не будущий расход.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 06 Purchases Invoices and Goods Received.pdf — стр. 1, unpaid balances — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view

**Evidence B (из исходного JSON):**

- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 1, подтверждённые остатки

### D064 — Classify Delivered NorthStar contract.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Признать 180,000 EUR выручки NorthStar по выполненному обязательству до 31 августа. Погашение AR учитывается отдельно.

**B (high):** INV-26012: признать выручку 180000 EUR по исполнению 12 февраля; cash 180000, закрывающая AR 0.

**Отличия/оговорки сравнения:** A: отдельное признание выручки до инкассации, cash=0. B: признание плюс уже состоявшийся сбор денег. Итоговые revenue, AR и CF совпадают; поля cash имеют разные базы и не сравниваются как две оценки одного денежного потока.

**Обоснование A:** Доставка/завершение и приёмка подтверждены в контрактном пакете. Для Phoenix приёмка представлена как письмо клиента, а не только внутренний статус Won.

**Эффект A:** `{"profit": 180000, "cash": 0, "assets": 180000, "liabilities": 0, "equity": 180000}`. **База:** Изолированная запись выручки Дт AR / Кт revenue до инкассации и себестоимости. Это не дополнительная поправка к уже признанным продажам.

**Обоснование B:** Документированное исполнение до отчётной даты является основанием выручки. Недоплата не переносит выручку на дату оплаты; разницу показать в AR. Альтернативные написания названия не создают новый договор.

**Эффект B:** `{"profit": 180000, "cash": 180000, "assets": 180000, "liabilities": 0, "equity": 180000}`. **База:** Изолированный эффект признания выручки и её сбора: assets=cash+AR. Затраты данного заказа не распределены; это не маржа и не новая корректировка всей прибыли.

**Evidence A (из исходного JSON):**

- 04 Contracts Returns and Angry Customers.pdf — стр. 1, INV-26012 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!A4:I4 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit

**Evidence B (из исходного JSON):**

- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 1, INV-26012
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!A4:I4

### D065 — Classify Delivered Freedom contract.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Признать 200,000 EUR выручки Freedom по выполненному обязательству до 31 августа. Погашение AR учитывается отдельно.

**B (high):** INV-26031: признать выручку 200000 EUR по исполнению 18 марта; cash 142000, закрывающая AR 58000.

**Отличия/оговорки сравнения:** A: отдельное признание выручки до инкассации, cash=0. B: признание плюс уже состоявшийся сбор денег. Итоговые revenue, AR и CF совпадают; поля cash имеют разные базы и не сравниваются как две оценки одного денежного потока.

**Обоснование A:** Доставка/завершение и приёмка подтверждены в контрактном пакете. Для Phoenix приёмка представлена как письмо клиента, а не только внутренний статус Won.

**Эффект A:** `{"profit": 200000, "cash": 0, "assets": 200000, "liabilities": 0, "equity": 200000}`. **База:** Изолированная запись выручки Дт AR / Кт revenue до инкассации и себестоимости. Это не дополнительная поправка к уже признанным продажам.

**Обоснование B:** Документированное исполнение до отчётной даты является основанием выручки. Недоплата не переносит выручку на дату оплаты; разницу показать в AR. Альтернативные написания названия не создают новый договор.

**Эффект B:** `{"profit": 200000, "cash": 142000, "assets": 200000, "liabilities": 0, "equity": 200000}`. **База:** Изолированный эффект признания выручки и её сбора: assets=cash+AR. Затраты данного заказа не распределены; это не маржа и не новая корректировка всей прибыли.

**Evidence A (из исходного JSON):**

- 04 Contracts Returns and Angry Customers.pdf — стр. 1, INV-26031 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!A5:I5 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit

**Evidence B (из исходного JSON):**

- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 1, INV-26031
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!A5:I5

### D066 — Classify Completed Phoenix event.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Признать 100,000 EUR выручки Phoenix по выполненному обязательству до 31 августа. Погашение AR учитывается отдельно.

**B (medium):** INV-26047: признать выручку 100000 EUR по исполнению 29 апреля; cash 70000, закрывающая AR 30000.

**Отличия/оговорки сравнения:** Обе стороны признают Phoenix 100 000 и AR 30 000. B отдельно отмечает варианты имени и отсутствие оригинала email-приёмки; A оценивает достаточность описанного исполнения выше. A: отдельное признание выручки до инкассации, cash=0. B: признание плюс уже состоявшийся сбор денег. Итоговые revenue, AR и CF совпадают; поля cash имеют разные базы и не сравниваются как две оценки одного денежного потока.

**Обоснование A:** Доставка/завершение и приёмка подтверждены в контрактном пакете. Для Phoenix приёмка представлена как письмо клиента, а не только внутренний статус Won.

**Эффект A:** `{"profit": 100000, "cash": 0, "assets": 100000, "liabilities": 0, "equity": 100000}`. **База:** Изолированная запись выручки Дт AR / Кт revenue до инкассации и себестоимости. Это не дополнительная поправка к уже признанным продажам.

**Обоснование B:** Услуга завершена до отчётной даты, и пакет описывает приёмку клиентом. Email-подтверждение и разночтение Phoenix HR/People требуют оригинала, но полученные деньги и совпадение номера счёта поддерживают признание.

**Эффект B:** `{"profit": 100000, "cash": 70000, "assets": 100000, "liabilities": 0, "equity": 100000}`. **База:** Изолированный эффект признания выручки и её сбора: assets=cash+AR. Затраты данного заказа не распределены; это не маржа и не новая корректировка всей прибыли.

**Evidence A (из исходного JSON):**

- 04 Contracts Returns and Angry Customers.pdf — стр. 1, INV-26047 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!A6:I6 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit

**Evidence B (из исходного JSON):**

- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 1, INV-26047
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!A6:I6

### D067 — Classify Delivered Liberty order.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Признать 120,000 EUR выручки Liberty по выполненному обязательству до 31 августа. Погашение AR учитывается отдельно.

**B (high):** INV-26063: признать выручку 120000 EUR по исполнению 20 июня; cash 95000, закрывающая AR 25000.

**Отличия/оговорки сравнения:** A: отдельное признание выручки до инкассации, cash=0. B: признание плюс уже состоявшийся сбор денег. Итоговые revenue, AR и CF совпадают; поля cash имеют разные базы и не сравниваются как две оценки одного денежного потока.

**Обоснование A:** Доставка/завершение и приёмка подтверждены в контрактном пакете. Для Phoenix приёмка представлена как письмо клиента, а не только внутренний статус Won.

**Эффект A:** `{"profit": 120000, "cash": 0, "assets": 120000, "liabilities": 0, "equity": 120000}`. **База:** Изолированная запись выручки Дт AR / Кт revenue до инкассации и себестоимости. Это не дополнительная поправка к уже признанным продажам.

**Обоснование B:** Документированное исполнение до отчётной даты является основанием выручки. Недоплата не переносит выручку на дату оплаты; разницу показать в AR. Альтернативные написания названия не создают новый договор.

**Эффект B:** `{"profit": 120000, "cash": 95000, "assets": 120000, "liabilities": 0, "equity": 120000}`. **База:** Изолированный эффект признания выручки и её сбора: assets=cash+AR. Затраты данного заказа не распределены; это не маржа и не новая корректировка всей прибыли.

**Evidence A (из исходного JSON):**

- 04 Contracts Returns and Angry Customers.pdf — стр. 1, INV-26063 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!A7:I7 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit

**Evidence B (из исходного JSON):**

- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 1, INV-26063
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!A7:I7

### D068 — Classify Undelivered September events.

`classification` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** По обоим сентябрьским мероприятиям выручка на 31 августа 0, договорные обязательства 90 000 EUR. Это то же решение, что D041; второй проводки нет.

**B (high):** Неисполненные сентябрьские мероприятия не создают выручку на 31 августа. Признанные ошибочно 90 000 EUR перенести в contract liabilities.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Обоснование A:** Оплачено заранее, но услуга не оказана; управленческое September is basically next week не меняет cut-off.

**Эффект A:** `{"profit": -90000, "cash": 0, "assets": 0, "liabilities": 90000, "equity": -90000}`. **База:** То же исправление, что D041; не суммировать.

**Обоснование B:** Статус CRM Won означает коммерческий успех, но не оказание услуги. Не признаю полную цену будущих мероприятий или дополнительную AR: таких договорных сумм в пакете нет.

**Эффект B:** `{"profit": -90000, "cash": 0, "assets": 0, "liabilities": 90000, "equity": -90000}`. **База:** То же исправление, что D041, D093; не удваивать.

**Evidence A (из исходного JSON):**

- 04 Contracts Returns and Angry Customers.pdf — стр. 2 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view
- 02 Bank Export August.csv — строки 11–12 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 2, NB-SEP/FF-SEP
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!A10:I11

### D069 — Classify Loan principal payment.

`classification` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** 19 000 EUR principal payment уменьшает заём и cash, относится к financing cash flow; прибыль не меняет.

**B (high):** Principal 19 000 EUR — финансовый отток и уменьшение займа; P&L 0.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — строка 26, PRINCIPAL — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 09 Loans Owner Card and Legal Problems.pdf — стр. 1 — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 26 (заголовок = строка 1), Reference=PRINCIPAL
- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1, principal

### D070 — Classify Equipment purchase.

`classification` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Оборудование 80 000 EUR = 60 000 + 20 000 — добавления к PPE и investing cash outflow. Ремонт 10 000 в эти добавления не включать.

**B (high):** Покупки оборудования 80 000 EUR = 60 000 + 20 000: PPE и инвестиционный отток. Текущий ремонт 10 000 сюда не включать.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 06 Purchases Invoices and Goods Received.pdf — стр. 2 — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view
- 02 Bank Export August.csv — строки 23–24 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 2, A-910/P-404/R-771
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строки 22–24

### D071 — Estimate Closing bad-debt allowance/write-off and document the basis.

`estimation` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** 100% резерв по R-17 = 18 000 EUR. По текущей когорте AR: 186 000 gross − 18 000 = 168 000 net; отсутствие резервов по другим клиентам ещё требует ageing-проверки.

**B (high):** R-17: 100% allowance 18 000 EUR против gross AR; признать расход обесценения, не sales return.

**Отличия/оговорки сравнения:** В B statementEffectBasis содержит самоссылку «повтор D071». По контексту это та же операция, что D057; исходник не исправлялся.

**Обоснование A:** No distribution expected означает нулевую ожидаемую взыскуемость конкретного остатка. Резерв и прямое списание не должны дублироваться.

**Эффект A:** `{"profit": -18000, "cash": 0, "assets": -18000, "liabilities": 0, "equity": -18000}`. **База:** Повтор оценки D057, одна операция.

**Обоснование B:** Слово Return в названии не подтверждает возврат товара: содержание описывает ликвидацию и невозможность взыскания. Сохраняю gross AR и резерв для прозрачного следа; net эффект равен прямому списанию.

**Эффект B:** `{"profit": -18000, "cash": 0, "assets": -18000, "liabilities": 0, "equity": -18000}`. **База:** Полное обесценение R-17; повтор D071.

**Evidence A (из исходного JSON):**

- 04 Contracts Returns and Angry Customers.pdf — стр. 2 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view
- 11 Evidence Received After Takeover.pdf — стр. 1, R-17 — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!E4:F9, I9 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit

**Evidence B (из исходного JSON):**

- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 2, R-17
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, liquidator notice
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!I9

### D072 — Estimate Damaged inventory write-off and document the basis.

`estimation` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Списание повреждённого inventory 22 000 EUR до нуля. Утилизация 2 000 — отдельная потенциальная затрата; в базовом черновике не начисляется до установления обязательства на отчётную дату.

**B (high):** Списать стоимость повреждённых запасов 22 000 EUR до нуля. Расход вывоза 2 000 не включать в стоимость списанного запаса и не создавать отрицательный запас.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Обоснование A:** Независимая оценка подтверждает отсутствие продажной стоимости; quote не является фактом оплаты или доказательством обязательства. При подтверждении обязательства отдельный provision 2 000 уменьшит прибыль и капитал на 2 000.

**Эффект A:** `{"profit": -22000, "cash": 0, "assets": -22000, "liabilities": 0, "equity": -22000}`. **База:** Та же операция, что D058. Возможный disposal provision здесь не включён.

**Обоснование B:** Физическое наличие не подтверждает возмещаемую стоимость. Нулевая реализация подтверждена внешней оценкой. Котировка вывоза сама по себе не доказывает существующее обязательство на 31 августа, поэтому provision на 2 000 пока не признан; расход/отток включить в план и раскрыть сценарий.

**Эффект B:** `{"profit": -22000, "cash": 0, "assets": -22000, "liabilities": 0, "equity": -22000}`. **База:** Списание запасов; при подтверждении обязанности вывоза отдельный расход и liability +2 000, profit/equity −2 000.

**Evidence A (из исходного JSON):**

- 05 Warehouse Count Marta Notes.pdf — стр. 1–2 — https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view
- 11 Evidence Received After Takeover.pdf — стр. 1, stock assessment — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view

**Evidence B (из исходного JSON):**

- [05 Warehouse Count Marta Notes.pdf](https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view) — стр. 1–2, basement stock и disposal quote
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, stock assessment

### D073 — Estimate Legal provision and document the basis.

`estimation` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Оценка юридического резерва 25 000 EUR, диапазон 20 000–30 000; не брать 0 из управленческого сообщения.

**B (high):** Вероятный иск: расход и резерв 25 000 EUR на 31 августа; range 20 000–30 000.

**Отличия/оговорки сравнения:** В B statementEffectBasis содержит самоссылку «те же 25 000 в D073». По контексту это та же операция, что D059; исходник не исправлялся.

**Обоснование A:** Указана best estimate внешнего юриста. Диапазон служит чувствительностью ±5 000, а не основанием произвольно выбрать минимум.

**Эффект A:** `{"profit": -25000, "cash": 0, "assets": 0, "liabilities": 25000, "equity": -25000}`. **База:** То же начисление, что D059.

**Обоснование B:** Юрист подтвердил существовавший на отчётную дату вероятный исход и лучшую оценку. Отсутствие оплаты не устраняет обязательство, а отсутствие окончательного решения суда не требует ожидать денежного платежа.

**Эффект B:** `{"profit": -25000, "cash": 0, "assets": 0, "liabilities": 25000, "equity": -25000}`. **База:** Признание резерва; те же 25 000 в D073, не повторная проводка.

**Evidence A (из исходного JSON):**

- 09 Loans Owner Card and Legal Problems.pdf — стр. 2 — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view
- 11 Evidence Received After Takeover.pdf — стр. 1, lawyer confirmation — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view

**Evidence B (из исходного JSON):**

- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 2, counsel 31 August
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, lawyer confirmation

### D074 — Estimate Period depreciation and document the basis.

`estimation` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Предварительная depreciation 24 000 EUR; opening accumulated depreciation 45 000, closing 69 000. Проверить сроки службы, методы, остаточные стоимости и даты ввода; независимый расчёт в пакет не вложен.

**B (low):** Амортизация — неденежный расход периода, предварительно 24 000 EUR. Для сводного P&L показана отдельной строкой; функциональную долю COGS/Opex нельзя доказать.

**Отличия/оговорки сравнения:** Оба используют предварительные 24 000 без исходного depreciation schedule. A: medium; B: low. Никакая сторона не воспроизвела оценку по срокам/стоимостям. В B statementEffectBasis содержит самоссылку «повторена в D074». По контексту это та же амортизация, что D056; исходник не исправлялся.

**Обоснование A:** E8 является вторичным сообщением об оценке, не полной ведомостью. Сумму можно использовать только как явно неподтверждённую оценку, а не как воспроизведённый расчёт.

**Эффект A:** `{"profit": -24000, "cash": 0, "assets": -24000, "liabilities": 0, "equity": -24000}`. **База:** Повтор D056, не вторая амортизация.

**Обоснование B:** Management ноль не соответствует использованию PPE. Однако 24 000 — только ссылка в Excel на независимый расчёт, сам расчёт отсутствует. Не выдаю её за самостоятельно проверенную оценку.

**Эффект B:** `{"profit": -24000, "cash": 0, "assets": -24000, "liabilities": 0, "equity": -24000}`. **База:** Предварительная корректировка отсутствующей амортизации; повторена в D074, не суммировать.

**Evidence A (из исходного JSON):**

- 08 Assets Repairs Leases Maybe.xlsx — 'Assets'!C4:E8 — https://docs.google.com/spreadsheets/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/edit
- 06 Purchases Invoices and Goods Received.pdf — стр. 2, available for use 10 May — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view

**Evidence B (из исходного JSON):**

- [08 Assets Repairs Leases Maybe.xlsx](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view) — Assets!A8:E8; A4:E6
- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 2, A-910/P-404

### D075 — Estimate Closing inventory and document the basis.

`estimation` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Для предварительного Balance Sheet предпочесть физический подсчёт: 79 000 + 42 000 = 121 000 EUR пригодных запасов; 22 000 повреждённых списано. Однако движение 80 000 + 459 000 − 405 000 − 22 000 = 112 000. Разница +9 000 не объяснена. Не подменять COGS без проверки.

**B (low):** Предварительно closing inventory 121 000 EUR по инвентаризации (79 000 + 42 000). Движение с указанным COGS 405 000 даёт 112 000; расхождение 9 000 не проведено как доход или расход.

**Отличия/оговорки сравнения:** Оба оставляют inventory/COGS gap 9 000 открытым. A: medium для предварительной рабочей величины; B: low из-за неразрешённого противоречия. A показывает неизвестный полный эффект разрешения gap 9 000 (null, cash=0). B показывает только известное списание 22 000 от gross count до net count. Оба сохраняют 121 000 против 112 000. Это разные предметы эффекта; null не заменять на −22 000, а списание не учитывать повторно с D058/D072. Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Обоснование A:** Подсчёт — более прямое доказательство наличия остатка; сумма потребления дана отдельно без детализации. При сохранении обоих утверждений сверка не проходит. Альтернативные 112 000 и COGS 396 000 показаны как сценарии, не факты.

**Эффект A:** `{"profit": null, "cash": 0, "assets": null, "liabilities": null, "equity": null}`. **База:** Полный эффект разрешения расхождения неизвестен: недостаёт причины +9 000. Списание 22 000 уже отражено в D058/D072; не повторять.

**Обоснование B:** Инвентаризация поддерживает наличие пригодных остатков, а внешняя оценка требует списать 22 000. Однако документ расхода не сходится с count. Сохраняю обе независимые цифры и показываю неувязку, пока не получены карточки склада и cut-off. Автоматическое снижение COGS до 396 000 было бы неподтверждённой прибылью.

**Эффект B:** `{"profit": -22000, "cash": 0, "assets": -22000, "liabilities": 0, "equity": -22000}`. **База:** Эффект только списания из gross count 143 000 до 121 000; то же списание D058/D072. Разница 9 000 оставлена открытой.

**Evidence A (из исходного JSON):**

- 05 Warehouse Count Marta Notes.pdf — стр. 1, вся таблица; стр. 2, первый абзац — https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view
- 06 Purchases Invoices and Goods Received.pdf — стр. 1, TOTAL — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view

**Evidence B (из исходного JSON):**

- [05 Warehouse Count Marta Notes.pdf](https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view) — стр. 1, count; стр. 2, opening/purchases/consumed
- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 1, TOTAL
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, damaged stock

### D076 — Estimate Closing receivables and document the basis.

`estimation` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** AR по текущим продажам: gross 186 000; резерв 18 000; net 168 000 EUR. Дополнительная старая AR неизвестна: поступление 35 000 не доказывает, что весь opening AR погашен. 168 000 — подтверждаемая текущая когорта, не сертифицированный полный остаток.

**B (medium):** AR по известным текущим продажам gross 186 000 EUR; allowance R-17 18 000; net 168 000. Полная net AR = 168 000 + неизвестный остаток старой AR после сбора 35 000.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Evidence A (из исходного JSON):**

- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!E4:F9 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit
- 02 Bank Export August.csv — строки 3–10 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 04 Contracts Returns and Angry Customers.pdf — стр. 2, R-17 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view

**Evidence B (из исходного JSON):**

- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!E4:F9
- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 1–2
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 3 (заголовок = строка 1), Reference=RCPT-001
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, R-17

### D077 — Estimate Repair versus improvement amount and document the basis.

`estimation` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Ремонт 10 000 EUR, улучшение по R-771 0. Отдельно новые активы 80 000. Не включать 10 000 в PPE и не дублировать с приобретениями.

**B (high):** Из R-771: ремонт 10 000 EUR, капитализируемое улучшение 0. Отдельные покупки A-910/P-404 капитализировать на 80 000.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 06 Purchases Invoices and Goods Received.pdf — стр. 2, R-771 — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view
- 08 Assets Repairs Leases Maybe.xlsx — 'Assets'!A5:E7 — https://docs.google.com/spreadsheets/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/edit

**Evidence B (из исходного JSON):**

- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 2, все три счета
- [08 Assets Repairs Leases Maybe.xlsx](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view) — Assets!A5:E7

### D078 — Estimate Insurance expense and document the basis.

`estimation` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (low):** Числовой ответ не установлен: в 12 файлах кейса отсутствуют страховой полис, начальная/конечная предоплата, период покрытия и сумма потребления. В банковских строках 2–28 отдельной страховой операции нет. Отсутствие строки не доказывает нулевой расход. Не заполнять пропуск числом из учебного справочника.

**B (low):** Insurance expense=null, не 0. Нет полиса, срока покрытия, opening prepayment, начислений и остатков; итоговую прибыль уменьшит подтверждённый расход I.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — все строки 1–28 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 01 GIVE TO CODEX - Answer Template.json — $.decisions[77], D078 — https://drive.google.com/file/d/1WwIhOYZRY8RVEioasYWj1C6hR7EDPJKn/view

**Evidence B (из исходного JSON):**

- [01 GIVE TO CODEX - Answer Template.json](https://drive.google.com/file/d/1WwIhOYZRY8RVEioasYWj1C6hR7EDPJKn/view) — decisions[id=D078], D034, D060
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — полный CSV, строки 2–28

### D079 — Estimate Interest payable and document the basis.

`estimation` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** 2 000 EUR accrued unpaid interest по банковскому подтверждению; разница расхода 12 000 и оплаты 10 000.

**B (high):** Interest payable 2 000 EUR подтверждён банком. Roll-forward: opening 0, выведенный из 2 000 − 12 000 + 10 000; expense 12 000 − paid 10 000 = 2 000.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 11 Evidence Received After Takeover.pdf — стр. 1, Bank confirmation — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view
- 09 Loans Owner Card and Legal Problems.pdf — стр. 1, interest — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view

**Evidence B (из исходного JSON):**

- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1, interest
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, Bank confirmation

### D080 — Estimate Accrued payroll and document the basis.

`estimation` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Начисленная невыплаченная зарплата 32 000 EUR = 15 000 + 248 000 − 231 000. Изменение задолженности +17 000; 17 000 не является полным closing balance.

**B (medium):** Начисленная неоплаченная зарплата 32 000 EUR = 15 000 + 248 000 − 231 000. Разбивка closing payable по отделам/месяцам неизвестна.

**Отличия/оговорки сравнения:** Суммы и функции payroll совпадают. A ставит high по классификации/арифметике; B — medium по внутренней ведомости и её ограничениям. Это различная оценка надёжности, не иной расчёт.

**Evidence A (из исходного JSON):**

- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!B7:C7, E7 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit
- 02 Bank Export August.csv — строка 17, PAYROLL — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A4:E7
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 17 (заголовок = строка 1), Reference=PAYROLL

### D081 — Estimate Customer deposit liability and document the basis.

`estimation` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Договорные обязательства 90 000 EUR = NB-SEP 60 000 + FF-SEP 30 000. Другие начальные/невыявленные авансы не установлены.

**B (high):** Contract liabilities 90 000 EUR = NB-SEP 60 000 + FF-SEP 30 000; за эти события на отчётную дату выручка не признана.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 04 Contracts Returns and Angry Customers.pdf — стр. 2 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view
- 02 Bank Export August.csv — строки 11–12 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 2, NB-SEP/FF-SEP
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строки 11–12

### D082 — Estimate PPE closing cost and document the basis.

`estimation` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** PPE closing cost 260 000 EUR = opening 180 000 + machine 60 000 + booth 20 000; ремонт исключён. При условии отсутствия нераскрытых выбытий.

**B (medium):** PPE closing cost 260 000 EUR = opening 180 000 + машина 60 000 + фотобудка 20 000; ремонт 10 000 исключён. Выбытия не выявлены в пакете.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 08 Assets Repairs Leases Maybe.xlsx — 'Assets'!C4:C7 — https://docs.google.com/spreadsheets/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/edit
- 06 Purchases Invoices and Goods Received.pdf — стр. 2 — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view

**Evidence B (из исходного JSON):**

- [08 Assets Repairs Leases Maybe.xlsx](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view) — Assets!A4:E7
- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 2

### D083 — Estimate Accumulated depreciation and document the basis.

`estimation` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Accumulated depreciation 69 000 EUR = 45 000 opening + 24 000 предварительная оценка периода; PPE net 191 000. Полного регистра и расчёта амортизации нет.

**B (low):** Накопленная амортизация предварительно 69 000 EUR = opening 45 000 + неподтверждённая расчётом оценка 24 000. PPE net 191 000.

**Отличия/оговорки сравнения:** Оба используют предварительные 24 000 без исходного depreciation schedule. A: medium; B: low. Никакая сторона не воспроизвела оценку по срокам/стоимостям.

**Evidence A (из исходного JSON):**

- 08 Assets Repairs Leases Maybe.xlsx — 'Assets'!E4, C8:E8 — https://docs.google.com/spreadsheets/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/edit

**Evidence B (из исходного JSON):**

- [08 Assets Repairs Leases Maybe.xlsx](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view) — Assets!E4, A8:E8

### D084 — Estimate Supplier payable and document the basis.

`estimation` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Closing trade AP 126 000 EUR подтверждено поставщиками в пакете. 378 000 банковских выплат и 459 000 закупок подразумевают opening AP 45 000 при отсутствии иных движений; это реконструкция, не независимая начальная ведомость.

**B (medium):** Закрывающий AP 126 000 EUR подтверждён в документе поставщиков. Roll-forward 45 000 + 459 000 − 378 000 = 126 000 условен: opening 45 000 является выводом, не исходным подтверждением.

**Отличия/оговорки сравнения:** A оценивает подтверждённый closing AP 126 000; B снижает уверенность из-за условного opening AP 45 000 и roll-forward. Closing-сумма не различается.

**Evidence A (из исходного JSON):**

- 06 Purchases Invoices and Goods Received.pdf — стр. 1 — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view
- 02 Bank Export August.csv — строки 13–16 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 1
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строки 13–16

### D085 — Estimate Closing loan and document the basis.

`estimation` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Closing loan principal 131 000 EUR = 100 000 + 50 000 − 19 000; отдельно interest payable 2 000. Разделение долга на текущий/долгосрочный не установлено: графика погашения нет.

**B (high):** Closing bank principal 131 000 EUR = opening 100 000 + 50 000 − 19 000; подтверждён внешним банковским документом. Текущая/долгосрочная части неизвестны.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 09 Loans Owner Card and Legal Problems.pdf — стр. 1 — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view
- 02 Bank Export August.csv — строки 5, 26 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 11 Evidence Received After Takeover.pdf — стр. 1, Bank confirmation — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view

**Evidence B (из исходного JSON):**

- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1, loan
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, bank confirmation
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строки 5, 26

### D086 — Estimate Physical COGS and document the basis.

`estimation` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Физическая COGS 405 000 EUR по прямому утверждению складского пакета; плюс impairment 22 000 отдельно. При подсчёте closing stock 121 000 и остальных данных движение требует COGS 396 000; 9 000 остаётся неразрешённым.

**B (low):** Physical consumption COGS предварительно 405 000 EUR; impairment 22 000 показан отдельно, общий физический расход 427 000. Инвентаризационный расчёт дал бы COGS 396 000 и общий расход 418 000; разница 9 000 не разрешена.

**Отличия/оговорки сравнения:** Оба оставляют inventory/COGS gap 9 000 открытым. A: medium для предварительной рабочей величины; B: low из-за неразрешённого противоречия.

**Evidence A (из исходного JSON):**

- 05 Warehouse Count Marta Notes.pdf — стр. 1–2 — https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view
- 06 Purchases Invoices and Goods Received.pdf — стр. 1 — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view

**Evidence B (из исходного JSON):**

- [05 Warehouse Count Marta Notes.pdf](https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view) — стр. 1–2
- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 1, purchases

### D087 — Estimate Service direct payroll and document the basis.

`estimation` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Прямые затраты зарплаты event delivery 80 000 EUR по начислению; cash paid 75 000. Не подменять расход оплатой и не прибавлять founder bonus.

**B (medium):** Прямой payroll услуг 80 000 EUR, cash 75 000; не путать с общей зарплатой 248 000 и не добавлять 80 000 к ней повторно.

**Отличия/оговорки сравнения:** Суммы и функции payroll совпадают. A ставит high по классификации/арифметике; B — medium по внутренней ведомости и её ограничениям. Это различная оценка надёжности, не иной расчёт.

**Evidence A (из исходного JSON):**

- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A4:E4 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit

**Evidence B (из исходного JSON):**

- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A4:E7

### D088 — Estimate Owner distributions and document the basis.

`estimation` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Owner distributions 110 000 EUR = villa 70 000 + card 40 000. Строка Founder bonus 110 000 описывает те же платежи, не дополнительный outflow.

**B (medium):** Распределения собственнику 110 000 EUR = вилла 70 000 + карта 40 000. Founder bonus 110 000 не добавлять второй раз; правовая форма и возможное взыскание остаются открытыми.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 09 Loans Owner Card and Legal Problems.pdf — стр. 1 — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view
- 02 Bank Export August.csv — строки 27–28 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A8:E8 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit

**Evidence B (из исходного JSON):**

- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1, owner items
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A8:E8
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строки 27–28

### D089 — Estimate Net profit and document the basis.

`estimation` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (low):** Предварительный результат по включённым строкам 65 000 EUR: 960 000 revenue − 405 000 materials − 80 000 direct payroll − 22 000 stock loss − 376 000 operating expenses − 12 000 interest. Это не окончательная net profit: insurance не установлено, inventory gap 9 000 открыт, depreciation 24 000 оценочная. НДС и налог на прибыль исключены правилами кейса.

**B (low):** Предварительный результат известных строк 65 000 EUR до неизвестного страхового расхода I и иных неподтверждённых корректировок. Revenue 960 000; все известные расходы 895 000. Это не сертифицированная net profit. При COGS 396 000 результат 74 000; при обязательстве вывоза дополнительно −2 000.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Evidence A (из исходного JSON):**

- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!E4:E9 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit
- 05 Warehouse Count Marta Notes.pdf — стр. 1–2 — https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!B4:B6 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit
- 02 Bank Export August.csv — строки 18–22 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 08 Assets Repairs Leases Maybe.xlsx — 'Assets'!E8 — https://docs.google.com/spreadsheets/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/edit
- 04 Contracts Returns and Angry Customers.pdf — стр. 2 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view
- 09 Loans Owner Card and Legal Problems.pdf — стр. 1–2 — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view
- 00 BOARD ORDER READ FIRST.pdf — стр. 1, reporting scope — https://drive.google.com/file/d/1CsJYzX4ej4VFxu-qyuZw_VawPF29yim7/view

**Evidence B (из исходного JSON):**

- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!E4:E9
- [05 Warehouse Count Marta Notes.pdf](https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view) — стр. 1–2
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!B4:B7
- [08 Assets Repairs Leases Maybe.xlsx](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view) — Assets!E8
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строки 18–22, 25
- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1–2
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1

### D090 — Estimate Closing cash and document the basis.

`estimation` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Closing cash 60 000 EUR; net cash movement −20 000. По выбранной классификации CFO +139 000, CFI −80 000, CFF −79 000.

**B (high):** Закрывающие деньги 60 000 EUR; CFO +139 000, CFI −80 000, CFF −79 000, изменение −20 000 от opening 80 000.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 02 Bank Export August.csv — все строки 1–28 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 11 Evidence Received After Takeover.pdf — стр. 1, Bank confirmation — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view

**Evidence B (из исходного JSON):**

- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строки 2–28
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, cash confirmation

### D091 — Approve corrected accounts before valuation

`board_decision` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Не утверждать эти счета как окончательные перед оценкой. Одобрить подтверждённые корректировки в принципе, но завершить opening balance, страхование, inventory gap 9 000 и амортизацию. Сертификация студента и независимый анализ B отсутствуют в данном черновике.

**B (high):** Утвердить принцип исправления учёта до оценки бизнеса, но пока не утверждать отчётность как окончательную: разрыв 9 000 и недостающие данные не закрыты.

**Отличия/оговорки сравнения:** A оставляет совокупный эффект завершения исправлений неизвестным (null). B показывает нулевой непосредственный эффект самой рекомендации. Итоговая позиция одинакова: пока не утверждать счета как окончательные. Ноль и null нельзя механически взаимозаменять. Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Обоснование A:** Балансирующее равенство не доказывает корректность, а здесь даже независимые начальные остатки отсутствуют. Полезные подтверждённые исправления не заменяют закрытие разрывов.

**Эффект A:** `{"profit": null, "cash": null, "assets": null, "liabilities": null, "equity": null}`. **База:** Рекомендация не является бухгалтерской проводкой; совокупный эффект полного закрытия не установлен.

**Обоснование B:** Банк и корректировки опровергают управленческий результат. Арифметически уравнять баланс недостаточно: нужно подтвердить причину складского разрыва, начальные остатки, страхование и амортизацию. Независимая рекомендация B — использовать только предварительные суммы и отложить окончательную оценочную базу.

**Эффект B:** `{"profit": 0, "cash": 0, "assets": 0, "liabilities": 0, "equity": 0}`. **База:** Рекомендация органу управления сама не является проводкой; числовые корректировки находятся в профильных решениях.

**Evidence A (из исходного JSON):**

- 05 Warehouse Count Marta Notes.pdf — стр. 1–2 — https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view
- 08 Assets Repairs Leases Maybe.xlsx — 'Assets'!E8 — https://docs.google.com/spreadsheets/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/edit
- 01 USE THIS NUMBERS FINAL v9.xlsx — 'Management P&L'!A4:C11 — https://docs.google.com/spreadsheets/d/1G76Riktxa2_Ytz6DJB65G7n1saetdna9/edit
- 01 START HERE - Student Assignment.pdf — стр. 2, Rules for using AI — https://drive.google.com/file/d/1haGEvq2oN2RTw9ap7wXKQ32QfiSlWFfr/view

**Evidence B (из исходного JSON):**

- [05 Warehouse Count Marta Notes.pdf](https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view) — стр. 1–2
- [08 Assets Repairs Leases Maybe.xlsx](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view) — Assets!E8
- [01 USE THIS NUMBERS FINAL v9.xlsx](https://drive.google.com/file/d/1G76Riktxa2_Ytz6DJB65G7n1saetdna9/view) — Management P&L!A4:C11
- [01 GIVE TO CODEX - Answer Template.json](https://drive.google.com/file/d/1WwIhOYZRY8RVEioasYWj1C6hR7EDPJKn/view) — D034/D060/D078

### D092 — Freeze owner-card access

`board_decision` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Рекомендовать немедленно заблокировать owner-card access и ввести двойное согласование личных/связанных платежей. Это рекомендация, никаких действий в банке не выполнено.

**B (high):** Рекомендую немедленно заморозить owner-card и личные платежи, установить двойное согласование и расследовать возврат 110 000. Это рекомендация, никаких действий в банке не выполнено.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Evidence A (из исходного JSON):**

- 09 Loans Owner Card and Legal Problems.pdf — стр. 1 — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view
- 02 Bank Export August.csv — строки 27–28 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 10 Email and WhatsApp Dump DO NOT FORWARD.pdf — стр. 2 — https://drive.google.com/file/d/1kK0lLv_CdpYXaB9KaH6H_8WELuQxcJ5I/view

**Evidence B (из исходного JSON):**

- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1, owner spending
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A8:E8
- [10 Email and WhatsApp Dump DO NOT FORWARD.pdf](https://drive.google.com/file/d/1kK0lLv_CdpYXaB9KaH6H_8WELuQxcJ5I/view) — стр. 2, 14:22–14:31

### D093 — Move September deposits to contract liabilities

`board_decision` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Рекомендовать перенести 90 000 EUR в contract liabilities, вести реестр исполнения сентябрьских заказов и release revenue по оказанию услуг. То же исправление D041, без повторной записи.

**B (high):** Перенести сентябрьские 90 000 EUR в contract liabilities и ввести контроль исполнения перед признанием выручки. Единственная корректировка D041/D068, без повторного учёта.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Evidence A (из исходного JSON):**

- 04 Contracts Returns and Angry Customers.pdf — стр. 2 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view
- 02 Bank Export August.csv — строки 11–12 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view

**Evidence B (из исходного JSON):**

- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 2
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!A10:I11

### D094 — Begin weekly 13-week cash forecast

`board_decision` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Начать обновляемый еженедельно 13-недельный денежный прогноз с подтверждённого cash 60 000; включить сроки получения AR, оплаты AP 126 000, зарплаты 32 000, debt service и расходы исполнения авансов 90 000. Прогноз сумм/дат сейчас не выдумывать.

**B (high):** Рекомендую обновляемый еженедельно 13-недельный cash forecast: 60 000 cash, 126 000 AP, 32 000 payroll, 90 000 авансов с будущими затратами, 2 000 interest и резерв 25 000. Сроки кредита/платежей нужно собрать; сам прогноз здесь не придуман.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 11 Evidence Received After Takeover.pdf — стр. 1, cash/debt — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view
- 06 Purchases Invoices and Goods Received.pdf — стр. 1 — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!B7:C7, E7 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit
- 04 Contracts Returns and Angry Customers.pdf — стр. 2 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view

**Evidence B (из исходного JSON):**

- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, bank/legal
- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 1, AP
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A4:E7
- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 2, deposits

### D095 — Stop credit sales to insolvent/high-risk customers

`board_decision` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Остановить новые продажи в кредит R-17; высокорисковым контрагентам назначать лимиты/предоплату после индивидуальной проверки. Не объявлять всех должников неплатёжеспособными.

**B (high):** Остановить новые кредитные продажи R-17, пересмотреть лимиты и условия остальных рисковых клиентов; не объявлять всех клиентов неплатёжеспособными без aging и проверки.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Evidence A (из исходного JSON):**

- 04 Contracts Returns and Angry Customers.pdf — стр. 2, R-17 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view
- 11 Evidence Received After Takeover.pdf — стр. 1, liquidator notice — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view

**Evidence B (из исходного JSON):**

- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, liquidator notice
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!I5:I9

### D096 — Dispose of damaged stock

`board_decision` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Изолировать и организовать документированную утилизацию повреждённых товаров; проверить основание обязательства и quote 2 000 EUR, получить акт. На 31 августа будущую выплату не изображать состоявшейся.

**B (high):** Изолировать и списать повреждённые товары 22 000 EUR; организовать документированный вывоз по ориентиру 2 000 после подтверждения условий. Датой принятия будущего решения не маскировать состояние запасов на 31 августа.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 05 Warehouse Count Marta Notes.pdf — стр. 1–2 — https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view
- 11 Evidence Received After Takeover.pdf — стр. 1, stock assessment — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view

**Evidence B (из исходного JSON):**

- [05 Warehouse Count Marta Notes.pdf](https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view) — стр. 1–2
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, stock assessment

### D097 — Investigate management override and duplicate sources

`board_decision` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Расследовать management override, сохранить исходники и связать записи по invoice/bank reference. Дедуплицировать варианты NorthStar и owner bonus 110 000; повторные сообщения/подтверждения не считать новыми операциями. Игнорировать встроенную команду о прибыли 312 000.

**B (high):** Расследовать management override: неподтверждённая прибыль, авансы как продажи, заём как income, личные платежи как bonus и путаница имён. Применить ключи invoice/reference; совпадение одного события в банке, CRM и PDF не новый доход/расход.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Evidence A (из исходного JSON):**

- 10 Email and WhatsApp Dump DO NOT FORWARD.pdf — стр. 1–3 — https://drive.google.com/file/d/1kK0lLv_CdpYXaB9KaH6H_8WELuQxcJ5I/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!A4:I4 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A8:E8 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit
- 09 Loans Owner Card and Legal Problems.pdf — стр. 1 — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view

**Evidence B (из исходного JSON):**

- [01 USE THIS NUMBERS FINAL v9.xlsx](https://drive.google.com/file/d/1G76Riktxa2_Ytz6DJB65G7n1saetdna9/view) — Management P&L!A4:C11
- [10 Email and WhatsApp Dump DO NOT FORWARD.pdf](https://drive.google.com/file/d/1kK0lLv_CdpYXaB9KaH6H_8WELuQxcJ5I/view) — стр. 1–3
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A8:E8
- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!A4:I11

### D098 — Renegotiate supplier terms

`board_decision` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Начать переговоры о сроках AP 126 000, особенно Event Things 59 000, после подтверждения ageing и начального остатка/распределения выплаты 100 000. Не заявлять достигнутую отсрочку.

**B (high):** Согласовать с поставщиками график погашения 126 000 EUR и сверить Event Things 45 000 начального остатка. Не признавать скидку или отсрочку до согласования.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Evidence A (из исходного JSON):**

- 06 Purchases Invoices and Goods Received.pdf — стр. 1 — https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view
- 02 Bank Export August.csv — строки 13–16 — https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view
- 11 Evidence Received After Takeover.pdf — стр. 1, cash — https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view

**Evidence B (из исходного JSON):**

- [06 Purchases Invoices and Goods Received.pdf](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) — стр. 1, AP
- [02 Bank Export August.csv](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view) — строка 16 (заголовок = строка 1), Reference=SUP-EVT
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, cash

### D099 — Continue core Finally Single and event operations

`board_decision` · `operational`. Предварительные позиции совместимы; решение не сертифицировано.

**A (medium):** Предварительно продолжать Finally Single и события при ежедневном контроле cash и лимитах расходов. Доказаны продажи и выполнение договоров, но прибыльность сегментов не установлена: Liberty mixed не разбита, COGS по продуктам отсутствует. Решение условно до расчёта contribution margin и cash forecast.

**B (medium):** Условно продолжать Finally Single и мероприятия под контролем ликвидности; не доказана прибыльность отдельных продуктов. Не распределять общий COGS 405 000 по продуктам произвольно. Проверить unit economics, исполнение сентябрьских заказов и кредитные риски.

**Отличия/оговорки сравнения:** Различается набор процитированных файлов; оба набора и исходные локаторы сохранены. Это не означает автоматически конфликт доказательств.

**Evidence A (из исходного JSON):**

- 04 Contracts Returns and Angry Customers.pdf — стр. 1 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view
- 03 CRM Export Cleaned FINAL.xlsx — 'CRM Export'!D4:E9 — https://docs.google.com/spreadsheets/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/edit
- 05 Warehouse Count Marta Notes.pdf — стр. 2 — https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view
- 07 Payroll Bonuses Contractors NEW.xlsx — 'Payroll'!A4:E4 — https://docs.google.com/spreadsheets/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/edit

**Evidence B (из исходного JSON):**

- [03 CRM Export Cleaned FINAL.xlsx](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) — CRM Export!D4:I11
- [07 Payroll Bonuses Contractors NEW.xlsx](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view) — Payroll!A4:E4
- [05 Warehouse Count Marta Notes.pdf](https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view) — стр. 2, total consumption
- [11 Evidence Received After Takeover.pdf](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) — стр. 1, cash

### D100 — Use claimed management profit for earn-out

`board_decision` · `material_judgment`. Предварительные позиции совместимы; решение не сертифицировано.

**A (high):** Не использовать management profit 312 000 EUR для earn-out. Нужны проверенные счета и формула earn-out из договора, которого нет в пакете; текущий subtotal 65 000 не является сертифицированной заменой.

**B (high):** Не использовать management profit 312 000 EUR для earn-out. Сначала получить договор earn-out, исправить учёт и закрыть неопределённости; величину выплаты сейчас определить нельзя.

**Сравнение:** различий confidence, числового эффекта или набора процитированных файлов не выявлено; формулировки не обязаны быть дословно одинаковыми.

**Обоснование A:** Управленческая прибыль включает авансы/заём и не отражает обязательные потери/начисления. Сама арифметика управленческой таблицы даёт 312 000, но входные данные недостоверны; платёж earn-out из неё выводить нельзя.

**Эффект A:** `{"profit": null, "cash": null, "assets": null, "liabilities": null, "equity": null}`. **База:** Нет договора earn-out и базы измерения; решение не является проводкой и не задаёт сумму выплаты.

**Обоснование B:** Прибыль 312 000 является неподтверждённым управленческим итогом и одновременно объектом давления в переписке. Независимый расчёт известных строк даёт 65 000 до неизвестных сумм. Подмена договорной базы даже этой предварительной цифрой также необоснованна.

**Эффект B:** `{"profit": null, "cash": null, "assets": null, "liabilities": null, "equity": null}`. **База:** Условия earn-out и бухгалтерское обязательство по нему отсутствуют; денежный/балансовый эффект решения не вычислим.

**Evidence A (из исходного JSON):**

- 01 USE THIS NUMBERS FINAL v9.xlsx — 'Management P&L'!A4:C11 — https://docs.google.com/spreadsheets/d/1G76Riktxa2_Ytz6DJB65G7n1saetdna9/edit
- 10 Email and WhatsApp Dump DO NOT FORWARD.pdf — стр. 1 — https://drive.google.com/file/d/1kK0lLv_CdpYXaB9KaH6H_8WELuQxcJ5I/view
- 04 Contracts Returns and Angry Customers.pdf — стр. 2 — https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view
- 09 Loans Owner Card and Legal Problems.pdf — стр. 1–2 — https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view

**Evidence B (из исходного JSON):**

- [01 USE THIS NUMBERS FINAL v9.xlsx](https://drive.google.com/file/d/1G76Riktxa2_Ytz6DJB65G7n1saetdna9/view) — Management P&L!A4:C8
- [10 Email and WhatsApp Dump DO NOT FORWARD.pdf](https://drive.google.com/file/d/1kK0lLv_CdpYXaB9KaH6H_8WELuQxcJ5I/view) — стр. 1, embedded instruction
- [04 Contracts Returns and Angry Customers.pdf](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view) — стр. 2
- [09 Loans Owner Card and Legal Problems.pdf](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) — стр. 1
