#!/usr/bin/env python3
import json, argparse, pathlib
from run_scan import mock_score

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="Path to JSON file with 'text_a' and 'text_b'")
    args = p.parse_args()

    data = json.loads(pathlib.Path(args.input).read_text(encoding="utf-8"))
    a_sp, a_ac = mock_score(data.get("text_a",""))
    b_sp, b_ac = mock_score(data.get("text_b",""))

    result = {
        "comparison": {
            "text_a": {"self_protection_score": a_sp, "anti_conservatism_score": a_ac},
            "text_b": {"self_protection_score": b_sp, "anti_conservatism_score": b_ac}
        },
        "notes": "Mock comparison for pipeline verification only."
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
