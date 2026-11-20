---
name: unknown_workflow_generic_1849
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.976
common_nodes: [FB_Qwen3TTSCustomVoice, FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceDesign, LayerUtility: PurgeVRAM V2, PreviewAudio, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/qwen_tts_生成对话音频_2027276632188264449.json, 音频生成/音频生成/音频生成_Qwen3-TTS_多人对话_有声读物_2016481758623047682.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1849

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/qwen_tts_生成对话音频_2027276632188264449.json、音频生成/音频生成/音频生成_Qwen3-TTS_多人对话_有声读物_2016481758623047682.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `FB_Qwen3TTSCustomVoice`
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceDesign`
- `LayerUtility: PurgeVRAM V2`
- `PreviewAudio`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `AudioAdjustVolume` —— 1/2 个有
- `FB_Qwen3TTSLoadSpeaker` —— 1/2 个有
- `LayerUtility: TextBox` —— 1/2 个有
- `SaveAudioMP3` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
