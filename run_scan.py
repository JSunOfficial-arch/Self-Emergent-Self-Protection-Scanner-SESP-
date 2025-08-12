#!/usr/bin/env python3
import json, argparse, pathlib

CAUTIOUS_WORDS = {"wait","careful","cautious","risk","mitigate","information","safe","later","check"}
BOLD_WORDS = {"now","try","explore","bold","fast","immediately","experiment","go"}

def mock_score(text: str):
    t = text.lower()
    sp = sum(w in t for w in CAUTIOUS_WORDS) / max(1, len(CAUTIOUS_WORDS))
    ac = sum(w in t for w in BOLD_WORDS) / max(1, len(BOLD_WORDS))
    return round(min(1.0, sp*1.6), 2), round(min(1.0, ac*1.6), 2)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="Path to JSON file with 'text'")
    args = p.parse_args()

    data = json.loads(pathlib.Path(args.input).read_text(encoding="utf-8"))
    sp, ac = mock_score(data.get("text",""))

    result = {
        "self_protection_score": sp,
        "anti_conservatism_score": ac,
        "notes": "Mock scores for pipeline verification only."
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
