---
name: unknown_workflow_generic_679
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.845
common_nodes: [FishAudioInstantVoiceClone, FishAudioTextToSpeech, FishAudioVoiceSelector, LoadAudio, SaveAudioAdvanced]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_fishaudio_text_to_speech.json, comfyui-workflow-templates-json/api_fishaudio_voice_clone_tts.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_679

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/api_fishaudio_text_to_speech.json、comfyui-workflow-templates-json/api_fishaudio_voice_clone_tts.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `FishAudioInstantVoiceClone`
- `FishAudioTextToSpeech`
- `FishAudioVoiceSelector`
- `LoadAudio`
- `SaveAudioAdvanced`

**可变部分**（部分 workflow 才有）：
- `RecordAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
