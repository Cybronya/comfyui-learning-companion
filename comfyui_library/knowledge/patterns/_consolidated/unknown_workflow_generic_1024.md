---
name: unknown_workflow_generic_1024
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.875
common_nodes: [Apply Whisper, AudioCrop, CR Text, FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, LayerUtility: PurgeVRAM V2, LoadAudio, SaveAudio, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/四角色千问TTS_2082497969068265473.json, 音频生成/音频生成/📻Qwen3 TTS多角色配音及克隆音色 📻_2018613919941660673.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1024

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/四角色千问TTS_2082497969068265473.json、音频生成/音频生成/📻Qwen3 TTS多角色配音及克隆音色 📻_2018613919941660673.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `Apply Whisper`
- `AudioCrop`
- `CR Text`
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `SaveAudio`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `FB_Qwen3TTSVoiceDesign` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
