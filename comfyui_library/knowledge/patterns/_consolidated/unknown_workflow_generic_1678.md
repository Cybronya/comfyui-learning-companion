---
name: unknown_workflow_generic_1678
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [AnySwitch, FB_Qwen3TTSVoiceClone, Label (rgthree), LoadAudio, SaveAudio, Text Multiline, VHS_LoadAudio, WhisperSTT]
problems: []
missing: []
members: ["音频生成/音频生成/Qwen3-TTS语音克隆,设计_2016159449999740930.json", "音频生成/音频生成/Qwen3-TTS语音克隆,设计_2016181702023974914.json"]
source: knowledge_consolidation
---

# unknown_workflow_generic_1678

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Qwen3-TTS语音克隆,设计_2016159449999740930.json、音频生成/音频生成/Qwen3-TTS语音克隆,设计_2016181702023974914.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `AnySwitch`
- `FB_Qwen3TTSVoiceClone`
- `Label (rgthree)`
- `LoadAudio`
- `SaveAudio`
- `Text Multiline`
- `VHS_LoadAudio`
- `WhisperSTT`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
