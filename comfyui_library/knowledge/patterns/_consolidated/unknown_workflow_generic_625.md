---
name: unknown_workflow_generic_625
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.814
common_nodes: [IndexTTS2Run, LoadAudio, PrimitiveStringMultiline, SaveAudioMP3]
problems: []
missing: []
members: [音频生成/音频生成/IndexTTS2 配音 _ 音色克隆_1983772949016682498.json, 音频生成/音频生成/IndexTTS2 音色克隆 + 情绪克隆_2083536527476486145.json, 音频生成/音频生成/IndexTTS2 音色克隆 + 情绪克隆_2085463412989063169.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_625

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/IndexTTS2 配音 _ 音色克隆_1983772949016682498.json、音频生成/音频生成/IndexTTS2 音色克隆 + 情绪克隆_2083536527476486145.json、音频生成/音频生成/IndexTTS2 音色克隆 + 情绪克隆_2085463412989063169.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `IndexTTS2Run`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `SaveAudioMP3`

**可变部分**（部分 workflow 才有）：
- `XB_CanvasLabel` —— 2/3 个有
- `NormalizeAudioLoudness` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
