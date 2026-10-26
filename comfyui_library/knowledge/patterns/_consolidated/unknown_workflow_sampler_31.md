---
name: unknown_workflow_sampler_31
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8906
common_nodes: [LoadAudio, OmniVoiceLongformTTS, OmniVoiceMultiSpeakerTTS, OmniVoiceVoiceCloneTTS, OmniVoiceVoiceDesignTTS, OmniVoiceWhisperLoader, SaveAudio]
problems: []
missing: []
members: [数字人/数字人/音色克隆_2064891468476669953.json, 音频生成/音频生成/600+语言支持 omnivoice-tts_2039996614458220545.json, 音频生成/音频生成/OmniVoice-TTS工作流_2042955678913925121.json, 音频生成/音频生成/【遇见AI】OmniVoice-TTS语音模型，声音克隆，长语音，声音设计，多人对话，支持方言_2043639883255783425.json, 音频生成/音频生成/超绝音色克隆 OmniVoice-TTS_2041735213079859201.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_31

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/音色克隆_2064891468476669953.json、音频生成/音频生成/600+语言支持 omnivoice-tts_2039996614458220545.json、音频生成/音频生成/OmniVoice-TTS工作流_2042955678913925121.json、音频生成/音频生成/【遇见AI】OmniVoice-TTS语音模型，声音克隆，长语音，声音设计，多人对话，支持方言_2043639883255783425.json、音频生成/音频生成/超绝音色克隆 OmniVoice-TTS_2041735213079859201.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadAudio`
- `OmniVoiceLongformTTS`
- `OmniVoiceMultiSpeakerTTS`
- `OmniVoiceVoiceCloneTTS`
- `OmniVoiceVoiceDesignTTS`
- `OmniVoiceWhisperLoader`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `PreviewAudio` —— 4/5 个有
- `TrimAudio` —— 3/5 个有
- `YC_SingleTextNode` —— 3/5 个有
- `YC_textReplaceNode` —— 3/5 个有
- `MelBandRoFormerModelLoader` —— 2/5 个有
- `MelBandRoFormerSampler` —— 2/5 个有
- `LoadImage` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
