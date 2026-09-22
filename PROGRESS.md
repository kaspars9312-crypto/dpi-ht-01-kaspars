# DPI-HT-01 — состояние проекта

Веха 5 выполнена в объёме запрошенных ведомостей, предварительной отчётности и семи сверок. Работа остановлена. Это завершение подготовки документов с оговорками, а не подтверждение окончательной финансовой отчётности.

## Состояние вех

| Веха | Статус |
|---|---|
| 1. Спецификация | Завершена ранее; исходные CASE_SPEC.md / SOURCE_MANIFEST.md / PLAN.md сохранены |
| 2. A | Результаты ранее получены; не изменялись и не использовались повторно как источник окончательных решений в вехе 5 |
| 3. B | Результаты ранее получены; то же ограничение источников |
| 4. Согласование | Проверены 100/100; 70 resolved, 30 unresolved; согласованные документы сохранены без изменений |
| 5. Ведомости, отчётность и сверки | Документы подготовлены и проверены; P&L / BS / Equity preliminary / qualified; Cash Flow qualified при сходящемся итоге банка |
| 6. Сайт | Не начата |
| 7. Аудит готового результата | Не начат; текущие арифметические проверки входят в веху 5 |
| 8. Подготовка к публикации | Не начата |

## Результаты вехи 5

- Cash-to-bank: 0 расхождения; opening 80 000 + inflows 949 000 − outflows 969 000 = closing 60 000. Owner cash 110 000 включён один раз, его категория unresolved.
- Revenue/AR: четыре договора сходятся с разницей 0; web / полный company AR и allowance не подтверждены.
- Inventory/COGS: FAIL, +9 000 count минус movement. Net candidates 121 000 / 112 000 не проведены как окончательные.
- PPE: cost 260 000 сходится; depreciation / AD / net PPE не подтверждены.
- Debt: principal 131 000 сходится с разницей 0; interest payable 2 000 подтверждён, полный opening interest roll-forward не подтверждён.
- Assets = Liabilities + Equity и Equity roll-forward: NOT VERIFIABLE; сумма полной разницы неизвестна, не 0 и не автоматически 9 000.
- Дополнительно payroll closing 32 000 сходится; AP closing 126 000 подтверждён, недостающий opening/other bridge 45 000 остаётся открытым.
- Подтверждённые строки liabilities дают 406 000, но не утверждены как полный итог обязательств. Net profit, closing equity и полные totals BS неизвестны.

Все существенные суммы связаны с D-ID и первичкой в документах. Новых числовых допущений для закрытия пробелов нет; сохранена принятая legal best estimate 25 000 с диапазоном 20 000–30 000. Применены F01–F06 из FINANCIAL_ASSUMPTIONS.md.

## Источники и контроль

Использованы только DECISION_REGISTER.json (согласованные поля), принятые итоги AI_REVIEW_TRAIL.md, RECONCILIATION_LOG.md и первичные материалы. Локальные копии всех 14 первичных файлов заново прочитаны и проверены по SHA-256 реестра. Это зафиксированная версия Drive из вехи 4, не новое подтверждение текущего состояния Drive. Исторические originalA/originalB и незафиксированные черновики не использовались для расчётов. Три согласованных документа не изменены.

Проверены банковская последовательность и одно включение каждой записи, итоги всех ведомостей, семь сверок и ссылки на решения/первичку. Неизвестные значения сохранены; нет plug или округляющих проводок. Выполнены проверки подготовки документов, без заявления о завершённом аудите вехи 7.

## Обязательный человеческий ввод

student.id=null; student.name=null; studentReasoning, studentFinalAnswer и changedFromAI не заполнялись. Личных подтверждений студента 0. Независимость A/B ранее заявлена авторами; техническая история их чатов не проверялась.

## Неизменные unresolved

D014, D015, D016, D017, D018, D019, D020, D021, D032, D033, D034, D046, D047, D048, D052, D053, D054, D055, D056, D060, D071, D074, D075, D076, D078, D083, D086, D088, D089, D099.

## Файлы вехи 5

- [SCHEDULES.md](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/SCHEDULES.md>)
- [FINANCIAL_STATEMENTS.md](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/FINANCIAL_STATEMENTS.md>)
- [FINANCIAL_RECONCILIATIONS.md](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/FINANCIAL_RECONCILIATIONS.md>)
- [FINANCIAL_ASSUMPTIONS.md](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/FINANCIAL_ASSUMPTIONS.md>)

Предыдущие ограничения сохраняются: окончательная отчётность требует устранения открытых вопросов; нет сайта, репозитория, GitHub/Vercel или submission.json. Ничего не публиковалось и не отправлялось вовне. Следующие вехи не запускаются автоматически.

## Основания числовых итогов

| № | Сверка | Статус | Измеренная разница / ограничение | Решения и первичка |
|---|---|---|---|---|
| R1 | Assets = Liabilities + Equity | NOT VERIFIABLE | Полная разница неизвестна; нельзя заявить 0 или ограничить её 9 000 | [D075](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13545>), [D076](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:10005>), [D078](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:10231>), [D083](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13238>), [D088](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:11249>), [D089](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:11359>), [D091](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13595>); [STOCK — стр. 1–2](https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view); [ASSETS — E8](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view); [LEGAL — стр. 1–2](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view) |
| R2 | Cash-to-bank | PASS (CSV + confirmation) | 0; полный category split CF qualified из-за 110 000 owner payments | [D040](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:4351>), [D090](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:11505>), [D088](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:11249>); [BANK — стр. 2–28](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view); [LATER — стр. 1](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) |
| R3 | Revenue / AR | PARTIAL | Четыре договора: 0; CRM-когорта: арифметически 0, но web неподтверждён; полный AR gap неизвестен | [D064](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13345>), [D065](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13395>), [D066](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13445>), [D067](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13495>), [D071](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:9048>), [D076](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:10005>); [CONTRACTS — стр. 1–2](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view); [CRM — A4:I9](https://drive.google.com/file/d/1EvEbs1h7MYh6rq9MU5SUfTl5cH6ZA6Ms/view) |
| R4 | Inventory / COGS | FAIL | Count net 121 000 − movement net 112 000 = +9 000 | [D048](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:12967>), [D075](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13545>), [D086](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13288>); [STOCK — стр. 1–2](https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view); [PURCHASES — стр. 1](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) |
| R5 | PPE | PARTIAL | Cost register: 0; полный AD/net PPE gap неизвестен | [D070](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:8954>), [D074](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13156>), [D082](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:10640>), [D083](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13238>); [ASSETS — A4:E8](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view); [PURCHASES — стр. 2](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view) |
| R6 | Debt / Interest | PARTIAL | Principal: 0; expense − cash = confirmed interest 2 000, разница 0; полный interest roll-forward неизвестен | [D031](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:3419>), [D079](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:10336>), [D085](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:10937>); [LEGAL — стр. 1](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view); [BANK — стр. 5, 25–26](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view); [LATER — стр. 1](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view) |
| R7 | Equity roll-forward | NOT VERIFIABLE | Opening E, N, distributions и другие движения неизвестны; разница неизвестна | [D046](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:5418>), [D047](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:5615>), [D088](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:11249>), [D089](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:11359>), [D091](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13595>); [LEGAL — стр. 1–2](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view); [ASSETS — A4:E8](https://drive.google.com/file/d/1zwdXdZ0WYnFPDizjjFL1rLfF9Zdq0vu7/view); [STOCK — стр. 1–2](https://drive.google.com/file/d/1BLdVSxr7s0ObyMKY2rub1Yzg-Y47nqmf/view) |

Контроль известного liability subtotal: **126 000 + 32 000 + 90 000 + 131 000 + 2 000 + 25 000 = 406 000**. Это сумма перечисленных строк; её недостаточно для полного равенства баланса. [D084](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13263>), [D080](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13213>), [D081](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:10536>), [D085](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:10937>), [D079](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:10336>), [D073](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:9440>); [PURCHASES — стр. 1](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view); [PAYROLL — B7:C7/E7](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view); [CONTRACTS — стр. 2](https://drive.google.com/file/d/1-vykf-RafVvfLdrkscG3imG3q7jXsGZK/view); [LATER — стр. 1](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view)

Дополнительный AP-контроль: closing AP 126 000 против purchases 459 000 − bank payments 378 000 = 81 000; недостающее opening/прочее движение **45 000**. Это отдельный незакрытый bridge, а не доказанная ошибка конечного AP. Нулевой opening не принят. [D013](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:1566>), [D038](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:4167>), [D084](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13263>); [PURCHASES — стр. 1](https://drive.google.com/file/d/1_ws1iBvATS_W2RbWOXyf6AJHPdN3Ep2V/view); [BANK — стр. 13–16](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view)

Opening payable 15 000 + expense 248 000 − cash 231 000 = closing 32 000; difference **0**. Подтверждает общий остаток, не помесячную расшифровку и не closing отделов. [D062](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13099>), [D080](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:13213>); [PAYROLL — B4:C7/E7](https://drive.google.com/file/d/1ghZb0F-doXR88q_IQ3iDLRZLm9osFdAg/view); [BANK — стр. 17](https://drive.google.com/file/d/1-thqyRwpggWHWeFXaF9-IjpPXRIFKEBh/view)

Оценка legal provision: [D059](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:7323>), [D073](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json:9440>); [LEGAL — стр. 2](https://drive.google.com/file/d/1o-9-xIkdwwSd5UtTDvmewa-xvjrUjEnT/view); [LATER — стр. 1](https://drive.google.com/file/d/1g1cdTGMzvIHb1tfQfzy-0g10V9db7l0m/view)
