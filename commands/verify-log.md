---
description: 摘要專案 ACCEPTANCE.md 的歷史交付紀錄（每輪做了什麼、驗收結果）。
allowed-tools: Read
---

讀取專案根目錄的 `ACCEPTANCE.md`，用白話摘要歷史交付紀錄：

- 依輪次列出：第 N 輪做了哪些功能、各功能最終驗收狀態（✅/❌）。
- 維持白話、非技術語氣（同 verify-done 流程 A 的規則）。
- 若 `ACCEPTANCE.md` 不存在，告知使用者尚無紀錄（可能 `log:off` 或還沒驗收過任何一輪）。

$ARGUMENTS（選填）：給輪次號（如 `3`）只摘要該輪；給 `last` 只摘要最新一輪。
