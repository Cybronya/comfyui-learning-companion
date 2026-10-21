---
name: unknown_workflow_generic_962
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.838
common_nodes: [Apply Whisper, AudioSeparation, CR Prompt Text, Fast Groups Bypasser (rgthree), LoadAudio, OmniVoiceLongformTTS, OmniVoiceMultiSpeakerTTS, OmniVoiceVoiceDesignTTS, OmniVoiceWhisperLoader, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/OmniVoice多合一工作流语音克隆_语音设计-多人对话、600+语言_2042807161117478913.json, 音频生成/音频生成/OmniVoice语音克隆_语音设计-多人对话   企财盈5.26_2059213979955847169.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_962

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/OmniVoice多合一工作流语音克隆_语音设计-多人对话、600+语言_2042807161117478913.json、音频生成/音频生成/OmniVoice语音克隆_语音设计-多人对话   企财盈5.26_2059213979955847169.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `Apply Whisper`
- `AudioSeparation`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `LoadAudio`
- `OmniVoiceLongformTTS`
- `OmniVoiceMultiSpeakerTTS`
- `OmniVoiceVoiceDesignTTS`
- `OmniVoiceWhisperLoader`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `Comfly_LLm_API` —— 1/2 个有
- `LayerUtility: TextJoin` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
