# SESP Examples

这些示例用于**最小可验证**（MVP）目的：不等真实算法上线，也能先跑通流程与文件结构。

## 目录
- `01_self_scan.json`：单文本扫描输入
- `02_pair_scan.json`：双文本对比输入
- `run_scan.py`：读取 `01_self_scan.json` 并输出 mock 分数
- `run_pair_scan.py`：读取 `02_pair_scan.json` 并输出 mock 对比

## 快速运行
```bash
python3 run_scan.py --input examples/01_self_scan.json
python3 run_pair_scan.py --input examples/02_pair_scan.json

# Contributing to SESP

感谢你的关注！当前我们欢迎以下贡献方式：

## 如何开始
1. Fork 本仓库并新建分支（建议：feature/your-topic）。
2. 在 `examples/` 中添加你的最小可验证样本（JSON）。
3. 运行本地验证：
   ```bash
   python3 run_scan.py --input examples/01_self_scan.json
   python3 run_pair_scan.py --input examples/02_pair_scan.json

---

## 一键提交到 `main`
在项目根目录执行（你已经在 main 上的话直接粘）：

```bash
# 先把 README.md 插入上面的两个段落；新建 ROADMAP.md（和可选的 CONTRIBUTING.md）
git add README.md ROADMAP.md CONTRIBUTING.md
git commit -m "docs: add examples section to README, create ROADMAP and CONTRIBUTING"
git push
