# DPI-HT-01 — журнал согласования и неразрешённых вопросов

## Результат и предмет приёмки

Проверены все 100 исходных ID D001–D100 по A/B и первичному пакету. **70 решений согласованы в пределах их предмета; 30 unresolved с confidence low.** Согласование координатором не является личной сертификацией студента и не утверждает финальные финансовые отчёты.

Все 16 исходных различий confidence и 6 statementEffect разобраны ниже отдельно. При совпадении A/B доказательства всё равно проверялись; большинство не использовалось как основание.

Полный реестр и исходные позиции: [DECISION_REGISTER.json](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/DECISION_REGISTER.json>). Существенные суждения: [AI_REVIEW_TRAIL.md](<C:/Users/Microsoft/OneDrive - University of Latvia/Documents/ChatGPT/sherlok/AI_REVIEW_TRAIL.md>).

## Полнота и неизменность источников

Прочитаны AB_COMPARISON.md/json и все десять переданных файлов A/B; их байты совпали с зафиксированными хешами предыдущего сравнения. Заново получены через Drive connector все 12 CASE и оба CODEX JSON. SHA-256 всех 14 совпали с версиями A/B. Прочитан полный текст 13 страниц семи CASE PDF, проверены три изображения, все пять листов четырёх XLSX, все 27 записей CSV с OPEN и оба полных JSON. Историческая техническая изоляция чатов не утверждается заново.

Схема и шаблон первички повторно разобраны; все id/question/category/reviewTier каждого A/B совпали с оригинальным шаблоном. Проверены 100 неповторяющихся ID, 75/25, все ссылки на использованные файлы и все исходные расхождения. Каждый вопрос имеет отдельный результат проверки в реестре.

Визуальное уточнение: на фото брони виллы указаны 12 Aug 2024 и 26 Aug 2024; банк содержит 31.08.2026. Это противоречие доказательств сохранено. На фото станка указано Year 2023 — год изготовления не доказывает другую дату установки; дата 10 May подтверждена текстом счёта. Фотографии сами по себе не заменяют регистр операций.

## 16 различий confidence

| ID | A | B | Принято | Статус | Основание по первичке |
|---|---|---|---|---|---|
| D003 | high | medium | medium | resolved | Контрактная выдержка прямо указывает исполнение 29 апреля, CRM связывает его с INV-26047, сумма банка 70000 совпадает с cash matched. Выручка 100000 и остаток 30000 проверены отдельно от инкассации. Для Phoenix первичка описывает email-приёмку, но оригинал письма отсутствует; совпадение invoice, суммы и даты достаточно для признания в пределах кейса с medium, не high. Разные имена не создают вторую операцию. Источники: 04 Contracts Returns and Angry Customers.pdf — стр. 1, INV-26047; 03 CRM Export Cleaned FINAL.xlsx — CRM Export!A6:I6; 02 Bank Export August.csv — строка 7 |
| D005 | high | medium | high | resolved | Bank RCPT-001 прямо назван Old customer AR settlement. Предмет D005 — конкретное поступление, поэтому принимается high A; medium B относится к иной задаче — полноте начального остатка, открытой в D076. Источники: 02 Bank Export August.csv — строка 3, RCPT-001 |
| D048 | medium | low | low | unresolved | Warehouse стр. 1 даёт gross count 143 000; стр. 2 — opening 80 000, purchases 459 000, consumed 405 000. 80 000 + 459 000 − 405 000 = 134 000, разница 9 000 возникает до списания. Одно свидетельство того же уровня не отменяет другое; закупки подтверждены отдельно. Принцип большинства не применяется. Источники: 05 Warehouse Count Marta Notes.pdf — стр. 1, count; стр. 2, opening/purchases/consumed; 06 Purchases Invoices and Goods Received.pdf — стр. 1, TOTAL; 11 Evidence Received After Takeover.pdf — стр. 1, повреждённый stock |
| D049 | high | medium | medium | resolved | Первичный Payroll явно описывает роли и отдельные expense/cash поля; bank PAYROLL подтверждает общий денежный итог. Ошибочная management classification не меняет функцию персонала. Принимается medium B: внутренняя ведомость достаточна для решения в кейсе, но нет employee-level/помесячного регистра для high. Источники: 07 Payroll Bonuses Contractors NEW.xlsx — Payroll!A4:E4; A7:E7; 02 Bank Export August.csv — строка 17, PAYROLL |
| D050 | high | medium | medium | resolved | Первичный Payroll явно описывает роли и отдельные expense/cash поля; bank PAYROLL подтверждает общий денежный итог. Ошибочная management classification не меняет функцию персонала. Принимается medium B: внутренняя ведомость достаточна для решения в кейсе, но нет employee-level/помесячного регистра для high. Источники: 07 Payroll Bonuses Contractors NEW.xlsx — Payroll!A5:E5; A7:E7; 02 Bank Export August.csv — строка 17, PAYROLL |
| D051 | high | medium | medium | resolved | Первичный Payroll явно описывает роли и отдельные expense/cash поля; bank PAYROLL подтверждает общий денежный итог. Ошибочная management classification не меняет функцию персонала. Принимается medium B: внутренняя ведомость достаточна для решения в кейсе, но нет employee-level/помесячного регистра для high. Источники: 07 Payroll Bonuses Contractors NEW.xlsx — Payroll!A6:E6; A7:E7; 02 Bank Export August.csv — строка 17, PAYROLL |
| D056 | medium | low | low | unresolved | Assets!C8=0 означает отсутствие начисления, E8 лишь ссылается на independent schedule. Самого расчёта, сроков службы, residual values и разбивки нет во всём пакете. Счета подтверждают ввод новых активов 10 мая, но не сумму амортизации. Принимается low B и unresolved вместо числового подтверждения A/B. Источники: 08 Assets Repairs Leases Maybe.xlsx — Assets!A4:E8, особенно C8/E8; 06 Purchases Invoices and Goods Received.pdf — стр. 2, A-910/P-404 |
| D062 | high | medium | medium | resolved | Payroll!E7 задаёт начальные 15 000, B7/C7 — начисления/оплаты, cash C7 совпадает с банком. Арифметика достаточна в пределах кейса. Medium B отражает внутренний источник без независимого closing-подтверждения; это не отсутствие конкретного исходного значения. Источники: 07 Payroll Bonuses Contractors NEW.xlsx — Payroll!B4:C7 и E7; A8:E8; 02 Bank Export August.csv — строка 17 |
| D066 | high | medium | medium | resolved | Контрактная выдержка прямо указывает исполнение 29 апреля, CRM связывает его с INV-26047, сумма банка 70000 совпадает с cash matched. Выручка 100000 и остаток 30000 проверены отдельно от инкассации. Для Phoenix первичка описывает email-приёмку, но оригинал письма отсутствует; совпадение invoice, суммы и даты достаточно для признания в пределах кейса с medium, не high. Разные имена не создают вторую операцию. Источники: 04 Contracts Returns and Angry Customers.pdf — стр. 1, INV-26047; 03 CRM Export Cleaned FINAL.xlsx — CRM Export!A6:I6; 02 Bank Export August.csv — строка 7 |
| D074 | medium | low | low | unresolved | Assets!C8=0 означает отсутствие начисления, E8 лишь ссылается на independent schedule. Самого расчёта, сроков службы, residual values и разбивки нет во всём пакете. Счета подтверждают ввод новых активов 10 мая, но не сумму амортизации. Принимается low B и unresolved вместо числового подтверждения A/B. Источники: 08 Assets Repairs Leases Maybe.xlsx — Assets!A4:E8, особенно C8/E8; 06 Purchases Invoices and Goods Received.pdf — стр. 2, A-910/P-404 |
| D075 | medium | low | low | unresolved | Полностью перечитаны count и движение Warehouse, подтверждены закупки в Purchases и повреждение в Later. Оба расчёта используют одно списание; оно не объясняет gap. Неизвестна причина расхождения, поэтому полный эффект его разрешения null. Выбран предмет эффекта A, confidence low B. Источники: 05 Warehouse Count Marta Notes.pdf — стр. 1–2; 06 Purchases Invoices and Goods Received.pdf — стр. 1, TOTAL; 11 Evidence Received After Takeover.pdf — стр. 1, independent stock assessment |
| D080 | high | medium | medium | resolved | Payroll!E7 задаёт начальные 15 000, B7/C7 — начисления/оплаты, cash C7 совпадает с банком. Арифметика достаточна в пределах кейса. Medium B отражает внутренний источник без независимого closing-подтверждения; это не отсутствие конкретного исходного значения. Источники: 07 Payroll Bonuses Contractors NEW.xlsx — Payroll!B4:C7 и E7; A8:E8; 02 Bank Export August.csv — строка 17 |
| D083 | medium | low | low | unresolved | Assets!E4 сообщает opening AD 45 000, E8 — лишь недоступный independent estimate 24 000. Без расчёта нельзя признать итог 69 000 проверенной оценкой. Принят low B. Источники: 08 Assets Repairs Leases Maybe.xlsx — Assets!E4 и A8:E8; 06 Purchases Invoices and Goods Received.pdf — стр. 2, даты готовности |
| D084 | high | medium | high | resolved | Purchases стр. 1 прямо говорит Supplier balances are independently confirmed. Поэтому для вопроса о конечном остатке принят high A, а не medium B за неизвестный opening. Начальная сверка 45 000 требует supplier statement и остаётся U-AP; её нерешённость не заменяет подтверждённый closing. Источники: 06 Purchases Invoices and Goods Received.pdf — стр. 1, unpaid amounts / independent confirmation; 02 Bank Export August.csv — строки 13–16 |
| D086 | medium | low | low | unresolved | Warehouse стр. 1 даёт gross count 143 000; стр. 2 — opening 80 000, purchases 459 000, consumed 405 000. 80 000 + 459 000 − 405 000 = 134 000, разница 9 000 возникает до списания. Одно свидетельство того же уровня не отменяет другое; закупки подтверждены отдельно. Принцип большинства не применяется. Источники: 05 Warehouse Count Marta Notes.pdf — стр. 1, count; стр. 2, opening/purchases/consumed; 06 Purchases Invoices and Goods Received.pdf — стр. 1, TOTAL; 11 Evidence Received After Takeover.pdf — стр. 1, повреждённый stock |
| D087 | high | medium | medium | resolved | Первичный Payroll явно описывает роли и отдельные expense/cash поля; bank PAYROLL подтверждает общий денежный итог. Ошибочная management classification не меняет функцию персонала. Принимается medium B: внутренняя ведомость достаточна для решения в кейсе, но нет employee-level/помесячного регистра для high. Источники: 07 Payroll Bonuses Contractors NEW.xlsx — Payroll!A4:E4; A7:E7; 02 Bank Export August.csv — строка 17, PAYROLL |

## 6 различий statementEffect

Вектора: profit / cash / assets / liabilities / equity. Неизвестные суммы не заменяются нулём; нулевой эффект рекомендации не означает нулевую будущую выплату.

| ID | A | B | Принято | Почему |
|---|---|---|---|---|
| D064 | 180 000 / 0 / 180 000 / 0 / 180 000 | 180 000 / 180 000 / 180 000 / 0 / 180 000 | 180 000 / 0 / 180 000 / 0 / 180 000 | Изолированное признание выручки Дт AR / Кт revenue до инкассации и себестоимости. Выбрана база A: cash=0. Реальный сбор денег подтверждён банком и рассматривается отдельно в D001–D004; он не пропущен и не добавляется повторно из effect B. Первичка: 04 Contracts Returns and Angry Customers.pdf — стр. 1, INV-26012; 03 CRM Export Cleaned FINAL.xlsx — CRM Export!A4:I4; 02 Bank Export August.csv — строка 4 |
| D065 | 200 000 / 0 / 200 000 / 0 / 200 000 | 200 000 / 142 000 / 200 000 / 0 / 200 000 | 200 000 / 0 / 200 000 / 0 / 200 000 | Изолированное признание выручки Дт AR / Кт revenue до инкассации и себестоимости. Выбрана база A: cash=0. Реальный сбор денег подтверждён банком и рассматривается отдельно в D001–D004; он не пропущен и не добавляется повторно из effect B. Первичка: 04 Contracts Returns and Angry Customers.pdf — стр. 1, INV-26031; 03 CRM Export Cleaned FINAL.xlsx — CRM Export!A5:I5; 02 Bank Export August.csv — строка 6 |
| D066 | 100 000 / 0 / 100 000 / 0 / 100 000 | 100 000 / 70 000 / 100 000 / 0 / 100 000 | 100 000 / 0 / 100 000 / 0 / 100 000 | Изолированное признание выручки Дт AR / Кт revenue до инкассации и себестоимости. Выбрана база A: cash=0. Реальный сбор денег подтверждён банком и рассматривается отдельно в D001–D004; он не пропущен и не добавляется повторно из effect B. Первичка: 04 Contracts Returns and Angry Customers.pdf — стр. 1, INV-26047; 03 CRM Export Cleaned FINAL.xlsx — CRM Export!A6:I6; 02 Bank Export August.csv — строка 7 |
| D067 | 120 000 / 0 / 120 000 / 0 / 120 000 | 120 000 / 95 000 / 120 000 / 0 / 120 000 | 120 000 / 0 / 120 000 / 0 / 120 000 | Изолированное признание выручки Дт AR / Кт revenue до инкассации и себестоимости. Выбрана база A: cash=0. Реальный сбор денег подтверждён банком и рассматривается отдельно в D001–D004; он не пропущен и не добавляется повторно из effect B. Первичка: 04 Contracts Returns and Angry Customers.pdf — стр. 1, INV-26063; 03 CRM Export Cleaned FINAL.xlsx — CRM Export!A7:I7; 02 Bank Export August.csv — строка 8 |
| D075 | null / 0 / null / null / null | -22 000 / 0 / -22 000 / 0 / -22 000 | null / 0 / null / null / null | Полный эффект разрешения stock gap 9 000: причина неизвестна, поэтому profit/assets/liabilities/equity null; это проверка неденежного closing-разрыва. Известное списание 22 000 уже отдельно в D058/D072. Выбрана база A, а не частичный impairment B. Первичка: 05 Warehouse Count Marta Notes.pdf — стр. 1–2; 06 Purchases Invoices and Goods Received.pdf — стр. 1, TOTAL; 11 Evidence Received After Takeover.pdf — стр. 1, independent stock assessment |
| D091 | null / null / null / null / null | 0 / 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 / 0 | Непосредственный бухгалтерский эффект самой рекомендации отложить утверждение: 0 во всех пяти полях. Неизвестный эффект будущих исправлений хранится в профильных unresolved-решениях и не подменяется нулём. Выбрана база B. Первичка: 05 Warehouse Count Marta Notes.pdf — стр. 1–2; 08 Assets Repairs Leases Maybe.xlsx — Assets!E8; 01 USE THIS NUMBERS FINAL v9.xlsx — Management P&L!A4:C11; 02 GIVE TO CODEX - Submission Rules.json — required и material_judgment fields |

## Дополнительные изменения после проверки совпадающих ответов

- D032/D033/D046/D047/D088: distribution не выбран окончательно, unresolved/low; подтверждён cash, но отсутствуют основание возврата/корпоративная форма.
- D052–D055: начисленный Opex не подтверждён одним платежом, unresolved/low.
- D071: 18 000 подтверждены только по R-17; совокупный closing allowance без ageing unresolved/low. D057 остаётся resolved/high.
- D076: 168 000 не подтверждены как полный company AR; unresolved/low.
- D073: 25 000 принят как best estimate в раскрытом диапазоне, resolved/medium, а не гарантированная будущая выплата.
- D099: безусловное продолжение core business не согласовано без unit economics/liquidity; unresolved/low.
- D100: нормализован непосредственный эффект рекомендации до 0; потенциальная выплата earn-out остаётся null. Это изменение обоих исходных effect, не решение выплатить 0.
- D048/D056/D071/D074 и owner judgments: неподтверждённые окончательные суммы в effect заменены null; кандидаты и первоначальные значения A/B сохранены. D075 сохраняет полный неизвестный эффект gap.
- Самоссылки B в D071/D073/D074 не перенесены в принятую базу: указаны корректные повторяющиеся события. D071 теперь отдельно оценивает полный неизвестный allowance, не повторяет R-17.

### Полная карта изменений по всем 100 вопросам

Формулировки унифицированы координатором; переписывание текста не равно смене экономической позиции. Таблица фиксирует все изменения confidence/effect, статус и изменение предмета. Дословные before A/B и after сохранены в JSON; ни одно исходное поле не перезаписано.

| ID | Confidence A → итог / B → итог | Effect относительно A / B | Итог | Изменение/уточнение |
|---|---|---|---|---|
| D001 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D002 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D003 | high → medium / medium → medium | — (operational) | resolved | Числа/классификация сохранены; принят medium B по надёжности первичного источника. |
| D004 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D005 | high → high / medium → high | — (operational) | resolved | Уверенность привязана к конкретному receipt/closing, а не к полноте opening; выбран high A. |
| D006 | medium → medium / medium → medium | — (operational) | resolved | Ответ ограничен подтверждённым поступлением/платежом; предварительные продажи/остатки/расходы не утверждены. |
| D007 | medium → medium / medium → medium | — (operational) | resolved | Ответ ограничен подтверждённым поступлением/платежом; предварительные продажи/остатки/расходы не утверждены. |
| D008 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D009 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D010 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D011 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D012 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D013 | medium → medium / medium → medium | — (operational) | resolved | Согласован платёж 100 000 и документированный closing AP; opening 45 000 остаётся отдельной гипотезой. |
| D014 | low → low / low → low | — (operational) | unresolved | Сохранено отсутствие окончательной суммы у обеих сторон; статус формализован как unresolved. |
| D015 | low → low / low → low | — (operational) | unresolved | Сохранено отсутствие окончательной суммы у обеих сторон; статус формализован как unresolved. |
| D016 | low → low / low → low | — (operational) | unresolved | Сохранено отсутствие окончательной суммы у обеих сторон; статус формализован как unresolved. |
| D017 | low → low / low → low | — (operational) | unresolved | Сохранено отсутствие окончательной суммы у обеих сторон; статус формализован как unresolved. |
| D018 | low → low / low → low | — (operational) | unresolved | Сохранено отсутствие окончательной суммы у обеих сторон; статус формализован как unresolved. |
| D019 | low → low / low → low | — (operational) | unresolved | Сохранено отсутствие окончательной суммы у обеих сторон; статус формализован как unresolved. |
| D020 | low → low / low → low | — (operational) | unresolved | Сохранено отсутствие окончательной суммы у обеих сторон; статус формализован как unresolved. |
| D021 | low → low / low → low | — (operational) | unresolved | Сохранено отсутствие окончательной суммы у обеих сторон; статус формализован как unresolved. |
| D022 | medium → medium / medium → medium | — (operational) | resolved | Ответ ограничен подтверждённым поступлением/платежом; предварительные продажи/остатки/расходы не утверждены. |
| D023 | medium → medium / medium → medium | — (operational) | resolved | Ответ ограничен подтверждённым поступлением/платежом; предварительные продажи/остатки/расходы не утверждены. |
| D024 | medium → medium / medium → medium | — (operational) | resolved | Ответ ограничен подтверждённым поступлением/платежом; предварительные продажи/остатки/расходы не утверждены. |
| D025 | medium → medium / medium → medium | — (operational) | resolved | Ответ ограничен подтверждённым поступлением/платежом; предварительные продажи/остатки/расходы не утверждены. |
| D026 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D027 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D028 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D029 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D030 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D031 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D032 | medium → low / medium → low | — (operational) | unresolved | Distribution больше не обозначается окончательно выбранным; cash подтверждён, правовая/учётная форма unresolved/low. |
| D033 | medium → low / medium → low | — (operational) | unresolved | Distribution больше не обозначается окончательно выбранным; cash подтверждён, правовая/учётная форма unresolved/low. |
| D034 | low → low / low → low | — (operational) | unresolved | Сохранено отсутствие окончательной суммы у обеих сторон; статус формализован как unresolved. |
| D035 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D036 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D037 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D038 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D039 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D040 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D041 | high → high / high → high | сохранён / сохранён | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D042 | high → high / high → high | сохранён / сохранён | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D043 | high → high / high → high | сохранён / сохранён | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D044 | high → high / high → high | сохранён / сохранён | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D045 | high → high / high → high | сохранён / сохранён | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D046 | medium → low / medium → low | изменён / изменён | unresolved | Distribution больше не обозначается окончательно выбранным; cash подтверждён, правовая/учётная форма unresolved/low. |
| D047 | medium → low / medium → low | изменён / изменён | unresolved | Distribution больше не обозначается окончательно выбранным; cash подтверждён, правовая/учётная форма unresolved/low. |
| D048 | medium → low / low → low | изменён / изменён | unresolved | Предварительное число остаётся candidate; окончательная величина/effect не подтверждены, unresolved/low. |
| D049 | high → medium / medium → medium | сохранён / сохранён | resolved | Числа/классификация сохранены; принят medium B по надёжности первичного источника. |
| D050 | high → medium / medium → medium | — (operational) | resolved | Числа/классификация сохранены; принят medium B по надёжности первичного источника. |
| D051 | high → medium / medium → medium | — (operational) | resolved | Числа/классификация сохранены; принят medium B по надёжности первичного источника. |
| D052 | medium → low / medium → low | — (operational) | unresolved | Оплата не принята за окончательный accrual expense; класс операционный, сумма unresolved/low. |
| D053 | medium → low / medium → low | — (operational) | unresolved | Оплата не принята за окончательный accrual expense; класс операционный, сумма unresolved/low. |
| D054 | medium → low / medium → low | — (operational) | unresolved | Оплата не принята за окончательный accrual expense; класс операционный, сумма unresolved/low. |
| D055 | medium → low / medium → low | — (operational) | unresolved | Оплата не принята за окончательный accrual expense; класс операционный, сумма unresolved/low. |
| D056 | medium → low / low → low | изменён / изменён | unresolved | Предварительное число остаётся candidate; окончательная величина/effect не подтверждены, unresolved/low. |
| D057 | high → high / high → high | сохранён / сохранён | resolved | Известное обесценение R-17 сохранено; ссылка на D071 уточнена: там проверяется неизвестный полный allowance, а не вторая запись R-17. |
| D058 | high → high / high → high | сохранён / сохранён | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D059 | high → high / high → high | сохранён / сохранён | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D060 | low → low / low → low | — (operational) | unresolved | Сохранено отсутствие окончательной суммы у обеих сторон; статус формализован как unresolved. |
| D061 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D062 | high → medium / medium → medium | — (operational) | resolved | Числа/классификация сохранены; принят medium B по надёжности первичного источника. |
| D063 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D064 | high → high / high → high | сохранён / изменён | resolved | Суммы признания/сбора сохранены; effect ограничен признанием выручки, cash=0 по базе A. |
| D065 | high → high / high → high | сохранён / изменён | resolved | Суммы признания/сбора сохранены; effect ограничен признанием выручки, cash=0 по базе A. |
| D066 | high → medium / medium → medium | сохранён / изменён | resolved | Числа/классификация сохранены; принят medium B. Effect ограничен признанием выручки, cash=0 по базе A, инкассация отдельно в D003. |
| D067 | high → high / high → high | сохранён / изменён | resolved | Суммы признания/сбора сохранены; effect ограничен признанием выручки, cash=0 по базе A. |
| D068 | high → high / high → high | сохранён / сохранён | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D069 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D070 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D071 | high → low / high → low | изменён / изменён | unresolved | 18 000 согласованы только для R-17 в D057; полный closing allowance неизвестен, unresolved/low. |
| D072 | high → high / high → high | сохранён / сохранён | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D073 | high → medium / high → medium | сохранён / сохранён | resolved | 25 000 приняты как best estimate с диапазоном; confidence снижен до medium у обоих. |
| D074 | medium → low / low → low | изменён / изменён | unresolved | Предварительное число остаётся candidate; окончательная величина/effect не подтверждены, unresolved/low. |
| D075 | medium → low / low → low | сохранён / изменён | unresolved | Предварительное число остаётся candidate; окончательная величина/effect не подтверждены, unresolved/low. |
| D076 | medium → low / medium → low | — (operational) | unresolved | 168 000 не согласованы как полный company AR; текущая когорта остаётся кандидатом, unresolved/low. |
| D077 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D078 | low → low / low → low | — (operational) | unresolved | Сохранено отсутствие окончательной суммы у обеих сторон; статус формализован как unresolved. |
| D079 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D080 | high → medium / medium → medium | — (operational) | resolved | Числа/классификация сохранены; принят medium B по надёжности первичного источника. |
| D081 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D082 | medium → medium / medium → medium | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D083 | medium → low / low → low | — (operational) | unresolved | Предварительное число остаётся candidate; окончательная величина/effect не подтверждены, unresolved/low. |
| D084 | high → high / medium → high | — (operational) | resolved | Уверенность привязана к конкретному receipt/closing, а не к полноте opening; выбран high A. |
| D085 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D086 | medium → low / low → low | — (operational) | unresolved | Предварительное число остаётся candidate; окончательная величина/effect не подтверждены, unresolved/low. |
| D087 | high → medium / medium → medium | — (operational) | resolved | Числа/классификация сохранены; принят medium B по надёжности первичного источника. |
| D088 | medium → low / medium → low | — (operational) | unresolved | Distribution больше не обозначается окончательно выбранным; cash подтверждён, правовая/учётная форма unresolved/low. |
| D089 | low → low / low → low | — (operational) | unresolved | Сохранено отсутствие окончательной суммы у обеих сторон; статус формализован как unresolved. |
| D090 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D091 | high → high / high → high | изменён / сохранён | resolved | Запрет финального утверждения сохранён; непосредственный effect рекомендации=0 по базе B. |
| D092 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D093 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D094 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D095 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D096 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D097 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D098 | high → high / high → high | — (operational) | resolved | Существо ответа/известные суммы сохранены; формулировка уточняет предмет, доказательства и границы, без студенческой сертификации. |
| D099 | medium → low / medium → low | — (operational) | unresolved | Условное продолжение не превращено в окончательное решение без unit economics/cash forecast; unresolved/low. |
| D100 | high → high / high → high | изменён / изменён | resolved | Отказ от management profit сохранён; effect самой рекомендации=0, потенциальная выплата остаётся null. |

## Все открытые вопросы и пути разрешения

Статус решения относится к конкретному вопросу шаблона. Например, известный платёж или рекомендация могут быть resolved, а полный opening или будущая сумма рядом остаются открытыми. Поэтому число тем журнала не равно числу unresolved-решений.

| Код | Тема / статус | Установлено и не установлено | Что требуется | Unresolved ID |
|---|---|---|---|---|
| U-STOCK | Запасы / COGS: €9 000; unresolved | Count gross 143 000 и movement gross 134 000; после одного списания 22 000 — 121 000 против 112 000. Причина не доказана. | Opening stock ledger, quantity/cost cards, GRN/issues и повторная инвентаризация. | D048, D075, D086, D089 |
| U-DEP | Амортизация; unresolved | 24 000 — только secondary estimate; 69 000 AD и 191 000 net PPE не окончательные. | Исходный depreciation schedule, register, useful lives, residuals, методы/даты. | D056, D074, D083, D089 |
| U-INSURANCE | Страхование; unresolved | Ни расход, ни движение, ни предоплата не установлены; отсутствие банковской строки не доказывает 0. | Полис, премия, период, opening/closing prepaid/payable. | D034, D060, D078, D089 |
| U-MONTHLY | Помесячная зарплата; unresolved | Есть только Jan–Aug aggregate 231 000 и expense 248 000 по отделам. | Помесячные начисления/выплаты и remittances. | D014, D015, D016, D017, D018, D019, D020, D021 |
| U-AR | Полная AR и совокупный allowance; unresolved | 35 000 collected не устанавливают full opening AR; R-17 18 000 подтверждён, остальные резервы нет. | Opening aging, closing AR ledger, reserve roll-forward и доказательства взыскуемости. | D071, D076 |
| U-WEB | Web revenue / settlements; unresolved | 360 000 web revenue и 73 000 gross platform AR только в CRM, без реестра исполнения/удержаний. | Orders, dispatch/acceptance, platform fees/refunds/settlement. | D076, D089 |
| U-OPEX | Периодизация Opex; unresolved | 131 000 оплат аренды/маркетинга/ПО/utilities не доказывают совпадение с начислением. Ремонт 10 000 отдельно документирован. | Договоры, coverage dates, счета и cut-off неоплаченного/предоплаченного. | D052, D053, D054, D055, D089 |
| U-OWNER | Distribution / recovery и дата виллы; unresolved | Банк 70 000 + 40 000, founder bonus — дубль; нет доказанного основания окончательно выбрать distribution против требования. Фото виллы: август 2024, банк: 31.08.2026. | Оригинал брони/связь с платежом, корпоративные решения, право возврата и взыскуемость, чеки owner-card. | D032, D033, D046, D047, D088 |
| U-AP | Opening AP Event Things; unresolved | Closing 59 000 подтверждён, payment 100 000 и purchases 114 000 дают implied opening 45 000 только при полноте движения. | Начальный supplier statement и allocation платежа. | нет: отдельный вопрос/ограничение |
| U-OPENING | Полный opening balance / equity; unresolved | Полной начальной ОСВ нет; условный equity из A/B не становится доказанным. | Opening trial balance, capital/retained earnings и все начальные счета. | D089 |
| U-DISPOSAL | Вывоз €2 000; unresolved | Котировка и будущая оценка известны; существующая обязанность заказать/оплатить вывоз на 31 августа не доказана. Известное списание stock 22 000 разрешено отдельно. | Договор/предписание/правовое или конструктивное обязательство на отчётную дату. | нет: отдельный вопрос/ограничение |
| U-DEBT | Debt maturity / ставка / opening interest; unresolved | Closing principal 131 000 и interest 2 000 подтверждены; текущая/долгосрочная часть, day count и исходный opening interest не установлены. | Полное соглашение, график и ковенанты. | нет: отдельный вопрос/ограничение |
| U-EARNOUT | Earn-out agreement / сумма; unresolved | Неприемлемость management312 000 установлена, но формула, выплата и обязательство earn-out отсутствуют. Сумма выплаты null. | Договор приобретения/earn-out и проверенная договорная финансовая база. | нет: отдельный вопрос/ограничение |
| U-SEGMENT | Продолжение core operations; unresolved | Нет продуктовой себестоимости, Liberty split и cash/costs-to-fulfil; продажи не доказывают прибыльность. | Product cost allocation, margin/unit economics, график ликвидности и исполнения September. | D099 |
| U-PERIMETER | Полнота банковского/учётного периметра; unresolved | CSV внутренне сходится и closing подтверждён; это не доказывает отсутствие других счетов или обязательств. | Полный список счетов/GL и исходные внешние подтверждения. | нет: отдельный вопрос/ограничение |
| U-LEGAL-RANGE | Legal estimation range; disclosed_estimation_uncertainty | Best estimate 25 000 подтверждён внешним юристом, диапазон 20 000–30 000 сохраняется. Этого достаточно для оценки provision, но не гарантирует выплату. | Обновлять по изменению фактов; это не отсутствующий обязательный вход для признания оценки. | нет: отдельный вопрос/ограничение |

**30 unresolved ID:** D014, D015, D016, D017, D018, D019, D020, D021, D032, D033, D034, D046, D047, D048, D052, D053, D054, D055, D056, D060, D071, D074, D075, D076, D078, D083, D086, D088, D089, D099.

Разрыв €9 000 не устранён, не назван расходом/доходом и не закрыт через капитал. Альтернативы inventory 112 000 либо consumption 396 000 остаются сценариями. Отсутствующие страхование, opening, depreciation, web и owner документы не заменены нулями.

## Сопутствующие расхождения из AB_COMPARISON

- Opex A 376 000 включает depreciation 24 000; B 352 000 исключает её и показывает отдельно. Это различие представления, не ещё один расход. Само наличие такого subtotal не разрешает амортизацию/Opex.
- BS NOT VERIFIED у A и FAIL ограниченной модели у B описывают один незакрытый gap и отсутствие независимого equity. Статусы не повышены до PASS; финальный баланс здесь не строился.
- Revenue/AR: арифметика текущей CRM-когорты не подтверждает полный opening/closing и взыскуемость. D076/D071 unresolved.
- PPE cost можно проверить отдельно от неизвестной амортизации; D082 resolved/medium, D056/D074/D083 unresolved/low.
- У 22 решений исходные наборы evidence различались; перечитаны соответствующие первичные документы. Итог использует наиболее прямые источники с точными локаторами в каждой записи, а не объединяет голоса ссылок.
- A-U01 означал получение спецификации, B-U01 — inventory. Новые коды U-* именованы по теме; прежние числовые коды не склеены.

## Фактически выполненные проверки и остановка

Повторно проверены все running balances и уникальные bank references, receipts без OPEN, суммы payroll по отделам/итогу и closing32 000, cost PPE260 000, CRM-когорта, supplier close126 000, principal131 000 и первичная неувязка stock9 000. Это проверки решений и доказательств, не создание финальных P&L/CF/BS.

Приёмка вехи 4: проверено 100/100, все 16+6 расхождений получили обоснованный результат, 30 unresolved сохранены с low. Веха завершена в этом процессном смысле. Студенческая сертификация — 0/100; данные личности и studentReasoning не заполнены. Вехи 5–8 не начаты; публикаций/отправки результатов не было.
