---
name: unknown_workflow_generic_1304
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.823667
common_nodes: [LoadAudio, OmniVoiceLongformTTS, OmniVoiceMultiSpeakerTTS, OmniVoiceVoiceCloneTTS, OmniVoiceVoiceDesignTTS, OmniVoiceWhisperLoader, Qwen3ASRLoader, Qwen3ASRTranscribe, SaveAudio]
problems: []
missing: []
members: [平台全量/omnivoice-TTS全家桶_2041811077431828481.json, 数字人/数字人/OmniVoice-TTS-支持600种语言_2041885496275640322.json, 音频生成/音频生成/OmniVoice 600+种语言_声音克隆_声音设计_多说话人对白_2041778769148518402.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1304

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/omnivoice-TTS全家桶_2041811077431828481.json、数字人/数字人/OmniVoice-TTS-支持600种语言_2041885496275640322.json、音频生成/音频生成/OmniVoice 600+种语言_声音克隆_声音设计_多说话人对白_2041778769148518402.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadAudio`
- `OmniVoiceLongformTTS`
- `OmniVoiceMultiSpeakerTTS`
- `OmniVoiceVoiceCloneTTS`
- `OmniVoiceVoiceDesignTTS`
- `OmniVoiceWhisperLoader`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
