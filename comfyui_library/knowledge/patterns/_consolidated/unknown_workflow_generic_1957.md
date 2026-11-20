---
name: unknown_workflow_generic_1957
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8265
common_nodes: [AudioCrop, LoadAudio, PrimitiveStringMultiline, SaveAudio, SaveAudioMP3]
problems: []
missing: []
members: [平台全量/带情感的声音克隆 电商带货配音_2056634761728323586.json, 音频生成/音频生成/DMOSpeech2声音极速克隆_1955416782771294210.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1957

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/带情感的声音克隆 电商带货配音_2056634761728323586.json、音频生成/音频生成/DMOSpeech2声音极速克隆_1955416782771294210.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `SaveAudio`
- `SaveAudioMP3`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `RunningHub DMOSpeech2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
