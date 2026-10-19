---
name: unknown_workflow_generic_824
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8335
common_nodes: [CR Prompt Text, FB_Qwen3TTSVoiceClone, LoadAudio, SaveAudio, WhisperSTT]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3 TTS声音克隆-smile版_2017123397238530050.json, 音频生成/音频生成/（smile版）Qwen3 TTS语音克隆V2_2015076620398239746.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_824

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Qwen3 TTS声音克隆-smile版_2017123397238530050.json、音频生成/音频生成/（smile版）Qwen3 TTS语音克隆V2_2015076620398239746.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `FB_Qwen3TTSVoiceClone`
- `LoadAudio`
- `SaveAudio`
- `WhisperSTT`

**可变部分**（部分 workflow 才有）：
- `TrimAudioDuration` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
