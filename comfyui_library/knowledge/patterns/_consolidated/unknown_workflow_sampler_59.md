---
name: unknown_workflow_sampler_59
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8795
common_nodes: [LoadAudio, OmniVoiceLongformTTS, OmniVoiceMultiSpeakerTTS, OmniVoiceVoiceCloneTTS, OmniVoiceVoiceDesignTTS, OmniVoiceWhisperLoader, SaveAudio, TrimAudio, YC_SingleTextNode, YC_textReplaceNode]
problems: []
missing: []
members: [音频生成/音频生成/【遇见AI】OmniVoice-TTS语音模型，声音克隆，长语音，声音设计，多人对话，支持方言_2043639883255783425.json, 音频生成/音频生成/超绝音色克隆 OmniVoice-TTS_2041735213079859201.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_59

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/【遇见AI】OmniVoice-TTS语音模型，声音克隆，长语音，声音设计，多人对话，支持方言_2043639883255783425.json、音频生成/音频生成/超绝音色克隆 OmniVoice-TTS_2041735213079859201.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadAudio`
- `OmniVoiceLongformTTS`
- `OmniVoiceMultiSpeakerTTS`
- `OmniVoiceVoiceCloneTTS`
- `OmniVoiceVoiceDesignTTS`
- `OmniVoiceWhisperLoader`
- `SaveAudio`
- `TrimAudio`
- `YC_SingleTextNode`
- `YC_textReplaceNode`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
