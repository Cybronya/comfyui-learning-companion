---
name: unknown_workflow_generic_260
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9556
common_nodes: [LoadAudio, MultiLinePromptIndex]
problems: []
missing: []
members: [音频生成/音频生成/IndexTTS 单人语音克隆_1954805801275801602.json, 音频生成/音频生成/IndexTTS声音克隆_1956254605715886082.json, 音频生成/音频生成/Index双人会话_1961897925611864065.json, 音频生成/音频生成/index-TTS2.0-双人会话_1967134000714223618.json, 音频生成/音频生成/提取音频+文案配音_1978984944171126785.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_260

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/IndexTTS 单人语音克隆_1954805801275801602.json、音频生成/音频生成/IndexTTS声音克隆_1956254605715886082.json、音频生成/音频生成/Index双人会话_1961897925611864065.json、音频生成/音频生成/index-TTS2.0-双人会话_1967134000714223618.json、音频生成/音频生成/提取音频+文案配音_1978984944171126785.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadAudio`
- `MultiLinePromptIndex`

**可变部分**（部分 workflow 才有）：
- `IndexTTSRun` —— 4/5 个有
- `SaveAudio` —— 4/5 个有
- `SaveAudioMP3` —— 4/5 个有
- `PreviewAudio` —— 2/5 个有
- `IndexTTS2Run` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
