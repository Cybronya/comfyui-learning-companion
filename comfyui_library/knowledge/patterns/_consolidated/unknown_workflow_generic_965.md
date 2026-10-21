---
name: unknown_workflow_generic_965
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7915
common_nodes: [Apply Whisper, AudioCrop, FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, Fast Groups Bypasser (rgthree), LayerUtility: PurgeVRAM V2, LoadAudio, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, SaveAudio, ShowText|pysssss, WhisperSTT]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3 TTS 多角色克隆配音 音色参考  Qwen3 TTS 声音克隆_2017873840382152706.json, 音频生成/音频生成/Qwen3 TTS全套-语音设计+克隆+多角配音_2015623768873373697.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_965

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Qwen3 TTS 多角色克隆配音 音色参考  Qwen3 TTS 声音克隆_2017873840382152706.json、音频生成/音频生成/Qwen3 TTS全套-语音设计+克隆+多角配音_2015623768873373697.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `Apply Whisper`
- `AudioCrop`
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `SaveAudio`
- `ShowText|pysssss`
- `WhisperSTT`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `Qwen3TTSVoiceDesign` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `Text` —— 1/2 个有
- `VRAMReserver` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
