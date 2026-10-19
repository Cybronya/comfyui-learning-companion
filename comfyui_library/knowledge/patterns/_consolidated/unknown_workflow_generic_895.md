---
name: unknown_workflow_generic_895
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.744
common_nodes: [CR Text, LoadAudio, SaveAudio, TDQwen3TTSModelLoader, TDQwen3TTSVoiceClone, TDQwen3TTSVoiceDesign, Text Multiline]
problems: []
missing: []
members: [音频生成/音频生成/音频-单人文本克隆音色设计配音-Qwen3+TTS_2064151132636794882.json, 音频生成/音频生成/音频-单人文本配音方言TD Qwen3 TTS_2064540877611163650.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_895

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/音频-单人文本克隆音色设计配音-Qwen3+TTS_2064151132636794882.json、音频生成/音频生成/音频-单人文本配音方言TD Qwen3 TTS_2064540877611163650.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `LoadAudio`
- `SaveAudio`
- `TDQwen3TTSModelLoader`
- `TDQwen3TTSVoiceClone`
- `TDQwen3TTSVoiceDesign`
- `Text Multiline`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `忽略多组孤海` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
