# タスク管理

## カスタムドライバ開発

### サン電子 SE220

| タスク | 状態 | 備考 |
|-------|------|------|
| コアドライバ実装 | 完了 | BaseConnection継承、全必要メソッド実装 |
| ssh_dispatcher登録 | 完了 | device_type: sundenshi_se220 |
| PLATFORMS.md追加 | 完了 | |
| 単体テスト作成 | 完了 | 4件、全パス |
| 実機テスト実施 | 完了 | 接続/切断、showコマンド、設定表示 |
| 実機テスト修正反映 | 完了 | ESC[s/ESC[u対応、cmd_verify無効化 |
| 実機統合テスト (192.168.62.1) | 完了 | 16項目全パス (v2.1.1.0) |
| 品質チェック (black/pylama/mypy) | 完了 | 全パス |
| 統合テスト設定ファイル整備 | 完了 | tests/etc/ exampleファイルに追加 |
| .claude/rules ファイル作成 | 完了 | sundenshi-se220.md |
| 開発履歴メモ作成 | 完了 | memo/history/001 |
| developブランチへのPR作成 | 未着手 | |

### BUFFALO VR-U300W

| タスク | 状態 | 備考 |
|-------|------|------|
| コアドライバ実装 | 完了 | |
| ssh_dispatcher登録 | 完了 | |
| 単体テスト作成 | 完了 | |
| 実機テスト | 完了 | |
| PR作成 | 未着手 | |
