---
name: unknown_workflow_generic_973
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.596
common_nodes: [FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceDesign, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImpactSwitch, Label (rgthree), LoadAudio, SaveAudioMP3, SetNode, TextInput_, WhisperSTT, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3-TTS 2人_单人对话音频生成(支持上传音色克隆或 文字描述生成音色)_2018391521661292545.json, 音频生成/音频生成/Qwen3-TTS 8人及以下对话音频生成(支持上传音色克隆或 文字描述生成音色)_2017578327875264513.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_973

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Qwen3-TTS 2人_单人对话音频生成(支持上传音色克隆或 文字描述生成音色)_2018391521661292545.json、音频生成/音频生成/Qwen3-TTS 8人及以下对话音频生成(支持上传音色克隆或 文字描述生成音色)_2017578327875264513.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceDesign`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `ImpactSwitch`
- `Label (rgthree)`
- `LoadAudio`
- `SaveAudioMP3`
- `SetNode`
- `TextInput_`
- `WhisperSTT`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
