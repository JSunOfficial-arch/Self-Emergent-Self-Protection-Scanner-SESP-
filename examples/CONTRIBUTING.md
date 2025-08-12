---

## **独立 CONTRIBUTING.md**
```markdown
# Contributing to SESP

感谢你的关注！当前我们欢迎以下贡献方式：

## 如何开始
1. Fork 本仓库并新建分支（建议：`feature/your-topic`）。
2. 在 `examples/` 中添加你的最小可验证样本（JSON）。
3. 本地运行验证：
   ```bash
   python3 run_scan.py --input examples/01_self_scan.json
   python3 run_pair_scan.py --input examples/02_pair_scan.json
   python3 run_scan.py --input examples/03_your_case.json
