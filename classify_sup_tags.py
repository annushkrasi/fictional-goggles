#!/usr/bin/env python3
"""Classify SUP pages into category labels."""
import csv
import re

TAGS = [
    "поставщики/партнёры",
    "регламенты_поддержки",
    "инструменты_поддержки",
    "описания_продукта",
    "правила_авиа",
    "hub_page",
    "sup-hr",
    "sup-qa",
    "sup-night",
]

# page_id -> title from confluence_categorization.csv
rows = []
with open("/tmp/confluence_categorization.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="|")
    for r in reader:
        rows.append((r["page_id"], r["title"]))

HUB_EXACT = {
    "7091650642",  # CA
    "6777274644",  # SoS table
    "6855066210",  # Временные политики
    "6796411450",  # Работа в ЛК GDS - actually supplier tool hub? check - it's GDS LK hub -> hub_page
    "7019397291",  # 3 lite 1
    "6972342303",  # 3 Light 2
    "6972145755",  # 3 Light 1
    "6972112974",  # 3 Hard
    "6991544339",  # 3 Hard CP
    "6971981910",  # 2 OTA
    "7355170998",  # CP Hard
    "7311425683",  # CP duties
    "7233372250", "7233273920", "7232225532", "7233241221",
    "7233601564", "7233503252", "7233601572", "7232913536",  # SoS sub-hubs
    "6977814860",  # meta partners hub-ish
}

SUP_QA = {
    "7319814187", "6884655393", "6804733972", "7348519320",
    "7241924627", "7170556002", "6899728546", "6677004347",
}

SUP_HR = {
    "6984827004", "6783435164", "6844842020", "6988824878",
    "6992855083", "5970624707", "6693257364", "7122485463",
    "7112982627", "7112884337", "7113015392", "6780289026",
    "6973948018", "7276265804", "6809616466",
}

PRODUCT = {
    "7255130389",  # eSIM
    "6977847758",  # hotels
    "7261880404",  # Explore
    "7328464930",  # loyalty points
}

TOOLS = {
    "7118487592", "6989840472", "6834389417", "7171375131",
    "6904610990", "7251525782", "6843400441", "6997345059",
    "7348683027", "7305265282", "7295533223", "6590464037",
    "6809452643", "6809452632",
}

# All Sirena instruction pages
SIRENA = {
    "5970952469", "5970362594", "5970624698", "5973705079", "5970985176",
    "5979177111", "5970362615", "5970657445", "5970362657", "5978554653",
    "5970362648", "6021611866", "6021611857", "6047564111", "6047465860",
    "6047170787", "6047400147", "6055461352", "6055068145", "6055068155",
    "6054838951", "5973279125", "5973639451", "7325058132", "7348322406",
    "7300317205", "7289701278",
}

MANUAL = {
    "7304380537": "регламенты_поддержки",
    "6776881486": "регламенты_поддержки",
    "6800736257": "поставщики/партнёры",
    "6809485418": "регламенты_поддержки",
    "6797328387": "инструменты_поддержки",
    "7151517922": "регламенты_поддержки",
    "6971752957": "поставщики/партнёры",
    "7068680299": "регламенты_поддержки",
    "6977814860": "регламенты_поддержки",
    "6496715526": "описания_продукта",
    "6809616466": "инструменты_поддержки",
    "6776848738": "описания_продукта",
}

AVIA_RULES = {
    "7352483902", "7352090688", "7274791741", "6924633965",
    "6825542197", "6751354992", "5618434354", "6967885866",
}

def is_temp_policy(title: str) -> bool:
    t = title.lower()
    return "временная политика" in t or "временные политики" in t

def is_airline_card(title: str) -> bool:
    t = title
    # Commission card format: "Airline / XX / 123" or "Name (XX)" or airline names with //
    if re.search(r"\b[A-Z]{2}\b.*\/\s*\d{2,3}\b", t):
        return True
    if re.search(r"\([A-Z0-9]{2,3}\)", t):
        return True
    if "//" in t and any(x in t.lower() for x in ["air", "airlines", "pobeda", "pegasus", "utair", "s7", "aeroflot", "turkish", "emirates", "qatar", "fly", "ajet", "belavia", "condor", "ryanair", "smartwings", "egypt", "ethiopian", "gulf", "lufthansa", "japan", "hainan", "el al", "srilankan", "sunexpress", "myanmar", "philippine", "royal jordanian", "oman", "uzbekistan", "virgin", "airindia", "air arabia", "armenian", "azerbaijan", "flydubai", "flyarystan", "rusline", "fly one"]):
        return True
    airline_only = [
        "Turkish Airlines", "Pegasus", "Flydubai", "FlyOne", "S7 Smart",
        "Аэрофлот", "Азимут", "Condor", "Ryanair", "Smartwings", "AJet",
    ]
    return any(a.lower() in t.lower() for a in airline_only)

def is_supplier_partner(title: str) -> bool:
    t = title.lower()
    keys = [
        "pk fare", "bingtrip", "kiwitaxi", "berlogic", "baosheng", "crane pax",
        "salo lk", "travelfusion", "ручная выписка", "мониторинга: лк",
        "отправка отчёта поставщикам", "поставщикам 2", "процесс работы с тикетами баошенга",
        "flyone", "таблицы по срокам",
    ]
    return any(k in t for k in keys)

def is_reglament(title: str) -> bool:
    t = title.lower()
    keys = [
        "алгоритм", "обработк", "передач", "онбординг", "обучение", "взаимодействие",
        "support_processes", "support_processes", "фрод", "оспариван", "эскалац",
        "памятка — 3 линия", "общее о команде", "технические проблемы с доступами",
        "приоритетная поддержка", "ota tech support", "дежурств", "адаптеры 3",
        "обновить статью", "прописать флоу", "дополнить статью", "добавить про",
        "изменение алгоритмов", "client automation", "работа с on-call",
        "прямые инструкции", "loyalty", "лояльный возврат", "после возврата",
        "обновить статьи по вв", "0 линия", "доп. услуги оta",
    ]
    return any(k in t for k in keys)

def classify(pid: str, title: str) -> tuple[str, str]:
    if pid in MANUAL:
        return MANUAL[pid], "ручная разметка"
    if pid in HUB_EXACT:
        return "hub_page", "хаб / оглавление раздела"
    if pid in SUP_QA or re.search(r"\bqa\b", title.lower()) or "контроль качества" in title.lower() or "проверок qa" in title.lower():
        return "sup-qa", ""
    if pid in SUP_HR or any(x in title.lower() for x in ["карьер", "hibob", "дайджест", "слёт", "списки команд", "эталон страницы"]):
        return "sup-hr", ""
    if "sup-night" in title.lower() or "ночн" in title.lower():
        return "sup-night", ""
    if pid in PRODUCT or "esim" in title.lower() or "отели" in title.lower():
        return "описания_продукта", ""
    if pid in TOOLS or "freshdesk" in title.lower() or "саммаризатор" in title.lower() or "user platform" in title.lower() or "angry.space" in title.lower():
        return "инструменты_поддержки", ""
    if pid in SIRENA or title.startswith("Сирена"):
        return "инструменты_поддержки", "инструкции по GDS/Сирене"
    if pid in AVIA_RULES or is_temp_policy(title):
        return "правила_авиа", ""
    if is_airline_card(title) or is_supplier_partner(title) or pid in {"6905856170", "6905790657", "6796411470", "7116914888", "6797296012", "6796804561", "6797263282", "6796837187", "6940590277", "6940262547", "7290880011", "7198048517", "7350386840", "7260438549", "7260471368", "7276920884"}:
        return "поставщики/партнёры", ""
    if is_reglament(title) or pid == "7068680299":
        return "регламенты_поддержки", ""
    if any(x in title.lower() for x in ["воркшоп", "команд"]):
        if "сирен" in title.lower():
            return "инструменты_поддержки", ""
        return "регламенты_поддержки", ""
    if "мета" in title.lower() or "serp" in title.lower() or "компенсации в мете" in title.lower():
        return "регламенты_поддержки", ""
    if "missing" in title.lower():
        return "?", "страница не найдена"
    return "?", f"уточнить вручную"

results = []
counts = {t: 0 for t in TAGS}
counts["?"] = 0
for pid, title in rows:
    tag, note = classify(pid, title)
    results.append((pid, title, tag, note))
    if tag in counts:
        counts[tag] += 1
    else:
        counts["?"] += 1

out = "/workspace/sup_tag_mapping.csv"
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["page_id", "title", "tag", "note"])
    w.writerows(results)

print("COUNTS:")
for t in TAGS + ["?"]:
    print(f"  {t}: {counts.get(t, 0)}")
print(f"\nUncertain ({counts['?']}):")
for r in results:
    if r[2] == "?":
        print(f"  {r[0]} | {r[1]} | {r[3]}")
print(f"\nWritten {out}")
