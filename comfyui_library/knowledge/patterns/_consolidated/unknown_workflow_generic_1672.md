---
name: unknown_workflow_generic_1672
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8605
common_nodes: [CR Text, LoadAudio, RH_IndexTTS25_Loader, RH_IndexTTS25_Synthesize, SaveAudioMP3, Text Multiline, easy seed]
problems: []
missing: []
members: [数字人/数字人/音频-单人文本克隆配音-Index TTS 2.5_2090801620899680258.json, 音频生成/音频生成/音频-单人文本克隆配音(情绪)-Index TTS 2.5_2103750269099139073.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1672

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/音频-单人文本克隆配音-Index TTS 2.5_2090801620899680258.json、音频生成/音频生成/音频-单人文本克隆配音(情绪)-Index TTS 2.5_2103750269099139073.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `LoadAudio`
- `RH_IndexTTS25_Loader`
- `RH_IndexTTS25_Synthesize`
- `SaveAudioMP3`
- `Text Multiline`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_NODE` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
