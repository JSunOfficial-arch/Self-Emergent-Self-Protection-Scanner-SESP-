# SESP Examples

这些示例用于最小可验证（MVP）目的：不等真实算法上线，也能先跑通流程与文件结构。

## 目录
- `01_self_scan.json`：单文本扫描输入
- `02_pair_scan.json`：双文本对比输入
- `03_your_case.json`：自定义示例输入
- `run_scan.py`：读取 `01_self_scan.json` 并输出 mock 分数
- `run_pair_scan.py`：读取 `02_pair_scan.json` 并输出 mock 对比

## 快速运行
```bash
python3 run_scan.py --input examples/01_self_scan.json
python3 run_pair_scan.py --input examples/02_pair_scan.json
python3 run_scan.py --input examples/03_your_case.json
