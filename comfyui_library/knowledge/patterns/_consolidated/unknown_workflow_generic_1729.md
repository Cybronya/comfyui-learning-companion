---
name: unknown_workflow_generic_1729
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.834
common_nodes: [Label (rgthree), LayerUtility: TextBox, LoadAudioUI, LoadImage, NormalizeAudioLoudness, PreviewAudio, Qwen3ASRLoader, Qwen3ASRTranscribe, SaveAudioAdvanced, SaveImage, WhisperSTT, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/工作流系列18-LongCat-TTS音频设计与克隆_2066483001005010945.json, 音频生成/音频生成/工作流系列19-OmniVoice-TTS音频设计与克隆_2066885810921762818.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1729

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/工作流系列18-LongCat-TTS音频设计与克隆_2066483001005010945.json、音频生成/音频生成/工作流系列19-OmniVoice-TTS音频设计与克隆_2066885810921762818.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `Label (rgthree)`
- `LayerUtility: TextBox`
- `LoadAudioUI`
- `LoadImage`
- `NormalizeAudioLoudness`
- `PreviewAudio`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `SaveAudioAdvanced`
- `SaveImage`
- `WhisperSTT`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LongCatMultiSpeakerTTS` —— 1/2 个有
- `LongCatTTS` —— 1/2 个有
- `LongCatVoiceCloneTTS` —— 1/2 个有
- `OmniVoiceLongformTTS` —— 1/2 个有
- `OmniVoiceMultiSpeakerTTS` —— 1/2 个有
- `OmniVoiceVoiceCloneTTS` —— 1/2 个有
- `OmniVoiceVoiceDesignTTS` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
