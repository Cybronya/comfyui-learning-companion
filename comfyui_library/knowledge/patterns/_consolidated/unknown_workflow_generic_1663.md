---
name: unknown_workflow_generic_1663
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.837
common_nodes: [CR Prompt Text, FB_Qwen3TTSCustomVoice, FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClone, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceDesign, LayerUtility: PurgeVRAM V2, LoadAudio, PreviewAny, PreviewAudio, Qwen2.5, SaveAudio, VRAMReserver, WhisperSTT, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/【合集】Qwen3 TTS 声音_2015689634474369026.json, 音频生成/音频生成/【阿良绘】Qwen语音设计合集 _ 多人情感对话、音色克隆、语音设计、_2063171776045215746.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1663

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/【合集】Qwen3 TTS 声音_2015689634474369026.json、音频生成/音频生成/【阿良绘】Qwen语音设计合集 _ 多人情感对话、音色克隆、语音设计、_2063171776045215746.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `FB_Qwen3TTSCustomVoice`
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClone`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceDesign`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `PreviewAny`
- `PreviewAudio`
- `Qwen2.5`
- `SaveAudio`
- `VRAMReserver`
- `WhisperSTT`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
