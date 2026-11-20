---
name: unknown_workflow_generic_528
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7862
common_nodes: [ElevenLabsInstantVoiceClone, ElevenLabsVoiceSelector, LoadAudio, RecordAudio, SaveAudioAdvanced]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_elevenlabs_speech_to_speech.json, comfyui-workflow-templates-json/api_elevenlabs_text_to_dialogue.json, comfyui-workflow-templates-json/api_elevenlabs_text_to_speech.json, comfyui-workflow-templates-json/api_elevenlabs_v4_text_to_dialogue.json, comfyui-workflow-templates-json/api_elevenlabs_v4_text_to_speech.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_528

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（comfyui-workflow-templates-json/api_elevenlabs_speech_to_speech.json、comfyui-workflow-templates-json/api_elevenlabs_text_to_dialogue.json、comfyui-workflow-templates-json/api_elevenlabs_text_to_speech.json、comfyui-workflow-templates-json/api_elevenlabs_v4_text_to_dialogue.json、comfyui-workflow-templates-json/api_elevenlabs_v4_text_to_speech.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 5 个 workflow 都包含：
- `ElevenLabsInstantVoiceClone`
- `ElevenLabsVoiceSelector`
- `LoadAudio`
- `RecordAudio`
- `SaveAudioAdvanced`

**可变部分**（部分 workflow 才有）：
- `ElevenLabsTextToDialogue` —— 2/5 个有
- `ElevenLabsTextToSpeech` —— 2/5 个有
- `ElevenLabsSpeechToSpeech` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
