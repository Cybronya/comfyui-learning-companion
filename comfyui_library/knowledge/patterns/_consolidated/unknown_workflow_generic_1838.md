---
name: unknown_workflow_generic_1838
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.916
common_nodes: [Fast Groups Bypasser (rgthree), LoadAudio, OmniVoiceLongformTTS, OmniVoiceVoiceCloneTTS, OmniVoiceWhisperLoader, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/TTS_2073064988377436162.json, 音频生成/音频生成/omnivoice-tts 语音克隆_2041461507283755010.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1838

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/TTS_2073064988377436162.json、音频生成/音频生成/omnivoice-tts 语音克隆_2041461507283755010.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `LoadAudio`
- `OmniVoiceLongformTTS`
- `OmniVoiceVoiceCloneTTS`
- `OmniVoiceWhisperLoader`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `SaveAudioMP3` —— 1/2 个有
- `TrimAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
