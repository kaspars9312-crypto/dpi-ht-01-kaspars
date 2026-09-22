"""Generate website-only English display data; canonical data is never modified."""
import copy, json, re
from pathlib import Path

ROOT = Path(__file__).parent
SOURCE = ROOT / "dist" / "site-data.json"
TARGET = ROOT / "dist" / "display-data-en.json"
CYR = re.compile(r"[\u0400-\u04ff]")
HTML_TEXT = re.compile(r"(?<=>)([^<]+)(?=<)")
SKIP_KEYS = {"sourceFile", "file", "name", "url", "sha256", "id", "filename", "validator"}

GLOSSARY = {
    "января": "January", "февраля": "February", "марта": "March", "апреля": "April", "мая": "May", "июня": "June", "июля": "July", "августа": "August", "сентября": "September", "октября": "October", "ноября": "November", "декабря": "December",
    "отчётность": "financial statements", "отчетность": "financial statements", "решение": "decision", "решения": "decisions", "решений": "decisions", "вопрос": "issue", "вопросы": "issues", "доказательства": "evidence", "первичка": "primary evidence", "источник": "source", "источники": "sources",
    "выручка": "revenue", "дебиторская задолженность": "accounts receivable", "кредиторская задолженность": "accounts payable", "запасы": "inventory", "себестоимость": "cost of sales", "прибыль": "profit", "убыток": "loss", "деньги": "cash", "активы": "assets", "обязательства": "liabilities", "капитал": "equity",
    "поступление": "receipt", "платёж": "payment", "оплата": "payment", "оплаты": "payments", "остаток": "balance", "списание": "write-down", "резерв": "allowance", "обесценение": "impairment", "амортизация": "depreciation", "начисление": "accrual", "предоплата": "prepayment", "проводка": "entry",
    "подтверждён": "confirmed", "подтверждена": "confirmed", "подтверждены": "confirmed", "не подтверждён": "not confirmed", "не подтверждена": "not confirmed", "не подтверждены": "not confirmed", "неизвестно": "unknown", "не установлено": "not established", "не доказано": "not evidenced", "не доказана": "not evidenced", "не доказаны": "not evidenced", "открытый": "open", "открытые": "open", "разница": "difference", "расхождение": "discrepancy", "разрыв": "gap",
    "требуется": "Required", "необходимо": "Required", "основание": "basis", "обоснование": "rationale", "уточнение": "clarification", "проверка": "review", "сверка": "reconciliation", "ведомость": "schedule", "движение": "movement", "начальный": "opening", "конечный": "closing", "текущий": "current", "полный": "complete", "итог": "total",
    "строка": "row", "строки": "rows", "стр.": "p.", "страница": "page", "страницы": "pages", "заголовок": "header", "договор": "contract", "счёт": "invoice", "банк": "bank", "банковский": "bank", "период": "period", "дата": "date", "сумма": "amount", "суммы": "amounts", "сумму": "amount",
    "принято": "adopted", "выбрана": "selected", "выбран": "selected", "остается": "remains", "остаётся": "remains", "отложить": "defer", "окончательное": "final", "рекомендация": "recommendation", "совету": "board", "учебный разбор": "educational review", "личный": "personal", "независимый": "independent", "совместный": "joint",
}
TRANSLIT = str.maketrans("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя", "ABVGDEEZZIYKLMNOPRSTUFHCSS_Y_EUYaabvgdeezziyklmnoprstufhcss_y_euya")

def translate(text):
    """Local display-only translation; no project text leaves this machine."""
    if not CYR.search(text): return text
    for ru, en in sorted(GLOSSARY.items(), key=lambda item: len(item[0]), reverse=True):
        text = re.sub(re.escape(ru), en, text, flags=re.IGNORECASE)
    # A safety fallback removes residual Cyrillic from user-visible display data only.
    return text.translate(TRANSLIT)

def translate_html(value, translations):
    return HTML_TEXT.sub(lambda match: translations.get(match.group(1), match.group(1)), value)

def gather(node, path=(), values=None):
    values = {} if values is None else values
    if isinstance(node, dict):
        for key, value in node.items():
            if key in SKIP_KEYS or key == "evidence":
                continue
            gather(value, path + (key,), values)
    elif isinstance(node, list):
        for index, value in enumerate(node):
            gather(value, path + (index,), values)
    elif isinstance(node, str) and CYR.search(node):
        if path[-1] == "html":
            for index, text in enumerate(HTML_TEXT.findall(node)):
                if CYR.search(text): values[path + ("html-text", index)] = text
        else:
            values[path] = node
    return values

def set_value(node, path, value):
    current = node
    for part in path[:-1]: current = current[part]
    current[path[-1]] = value

def main():
    raw = json.loads(SOURCE.read_text(encoding="utf-8"))
    display = copy.deepcopy(raw)
    strings = gather(raw)
    unique = list(dict.fromkeys(strings.values()))
    translations = {text: translate(text) for text in unique}
    html_paths = set()
    for path, text in strings.items():
        if len(path) >= 2 and path[-2] == "html-text":
            html_paths.add(path[:-2])
        else:
            set_value(display, path, translations[text])
    for path in html_paths:
        original = raw
        for part in path: original = original[part]
        set_value(display, path, translate_html(original, translations))
    # Retain raw locators alongside their English display equivalents.
    for raw_decision, decision in zip(raw.get("decisions", []), display.get("decisions", [])):
        for raw_evidence, evidence in zip(raw_decision.get("primaryEvidence", []), decision.get("primaryEvidence", [])):
            locator = raw_evidence.get("locator")
            if isinstance(locator, str) and CYR.search(locator):
                evidence["rawLocator"] = locator
                evidence["locator"] = translations.get(locator, translate(locator))
    display["displayLanguage"] = "en"
    TARGET.write_text(json.dumps(display, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
