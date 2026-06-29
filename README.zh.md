# done-gate

![done-gate demo](assets/demo.gif)

<sub>流程的腳本重現，非真實畫面錄影。</sub>

![type](https://img.shields.io/badge/Claude%20Code-Skill-7C3AED)
![invoke](https://img.shields.io/badge/slash-%2Fdone--gate-blue)
![lang](https://img.shields.io/badge/輸出-中%20%2F%20英-success)

一個給 Claude Code 用的**驗收型收尾 skill**。

> 痛點：Claude Code 會寫程式、也會自測，但「自測通過」不等於「使用者要的東西做好了」。
> done-gate 把收尾的決定權交還使用者——**沒有你親自勾選，這一輪就不算完成。**

[English](README.md) ｜ 繁體中文

## 目錄

- [核心理念](#核心理念)
- [為何需要](#為何需要)
- [範例對話](#範例對話)
- [安裝](#安裝)
- [使用](#使用)
- [特色](#特色)

## 核心理念

每一輪工作收尾前，Claude 必須：

1. 用**白話、零技術名詞**說明這輪做了什麼功能、功能在哪裡、怎麼操作；
2. 把功能列成**可勾選清單**，由你逐項驗收——**勾選的才通過**；
3. 未勾的項目**先問原因**（有 bug／想優化／自訂）再對症修，**迴圈到你勾選全部完成才收尾**。

Claude 不得自行宣告完成、不得代你勾選、不得用「應該沒問題」帶過。

## 為何需要

| | 沒有 done-gate | 有 done-gate |
|---|---|---|
| 完成的定義 | Claude 自評「測過了，應該好了」 | **你親自勾選**才算完成 |
| 收尾時機 | Claude 自行宣告就結束 | 你勾選全部前**不會收尾** |
| 成果說明 | 一堆檔名、函式、技術術語 | 白話：**做什麼／在哪裡／怎麼操作** |
| 沒做好怎麼辦 | 要自己重新描述需求 | 系統**主動問原因**並對症續修 |
| 交付留底 | 散落在對話裡 | 自動寫入 `ACCEPTANCE.md` 可追溯 |

## 範例對話

```
你：幫我在設定頁加一個「匯出報表」按鈕

Claude：（寫完程式、自測後，收尾前自動觸發 done-gate）

  這輪做了什麼（白話）
  匯出報表
  - 在做什麼：讓你把畫面上的資料一鍵存成檔案，方便寄出或留底。
  - 在哪裡：設定頁右上角那排按鈕裡，標著「匯出」的那一顆。
  - 怎麼操作：1) 選好月份 → 2) 按右上角「匯出」→ 3) 選存檔位置。

  [可勾選清單] 請勾選你已確認完成的項目：
  ☐ 匯出報表

你：（不勾，因為想改）

Claude：「匯出報表」未勾選，原因是？
  ○ 有 bug  ○ 想優化  ○ 自訂

你：想優化 → 希望多一個「選欄位」的選項

Claude：（修正後只重驗這項）… 直到你勾選 ✅ 才收尾，並寫入 ACCEPTANCE.md。
```

## 安裝

本 repo 是一個 **Claude Code plugin**。兩種用法：

**A — 當 plugin（建議）：** 在 Claude Code 把本 repo 加為 plugin 來源，
即可在任何地方使用 skill 與 `/done-gate-status`、`/done-gate-log` 命令。

**B — 當專案 skill：** 把 `skills/done-gate/` 複製到專案的 `.claude/skills/`，
並加上 `CLAUDE.md` 那條常駐規則，開啟該專案時就會自動載入。

```
.
├── .claude-plugin/plugin.json   # plugin 清單
├── skills/done-gate/SKILL.md  # skill 核心邏輯
├── commands/                    # /done-gate-status, /done-gate-log
├── references/                  # 深度文件，按需載入
├── examples/                    # ACCEPTANCE.md 範本
└── CLAUDE.md                    # 常駐規則：每輪收尾前先跑 done-gate
```

## 使用

自動觸發（每輪收尾），或手動呼叫：

```
/done-gate                       # 執行驗收流程
/done-gate log:off as:elder lang:both
/done-gate-status                # 本輪驗收進度快照（已過／待修）
/done-gate-log                   # 摘要 ACCEPTANCE.md 歷史紀錄
/done-gate-config as:client      # 檢視／設定專案預設（.done-gate.json）
/done-gate-handoff               # 產生白話交付說明書
/done-gate-explain <功能>        # 用白話重新解釋某個功能
```

| 參數 | 值 | 預設 | 作用 |
|------|----|------|------|
| `log:` | `on` / `off` | `on` | 是否把驗收寫入 `ACCEPTANCE.md` 交付紀錄 |
| `as:`  | `user` / `elder` / `pm` / `client` | `user` | 白話說明的對象與語氣 |
| `lang:`| `en` / `zh` / `both` | `en` | 輸出語言 |

## 特色

- 🛡️ **防作弊**：通過與否只由你勾選決定，Claude 不能自評過關。
- 🗣️ **白話交付**：只講「做什麼／在哪裡／怎麼操作」，不丟程式碼與術語。
- ✅ **可勾選驗收 + 續修迴圈**：未過項目自動轉新需求繼續修。
- ❓ **未過診斷**：未勾選的項目會主動問你原因（有 bug／想優化／自訂）再對症修正。
- 📋 **交付紀錄 `ACCEPTANCE.md`**：每輪自動留底，可追溯（可開關）。
- 👥 **對象切換**：講給長輩 / PM / 客戶聽，語氣自動調整。
- 🌐 **中英雙語輸出**。
- 📸 **操作截圖標註**（web，搭配 playwright；無則自動略過）。
